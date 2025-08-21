#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor, InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
import time

# ===== CONFIGURAÇÕES GLOBAIS =====
# Constantes configuráveis para fácil ajuste
FATOR_CORRECAO_GIRO = 4.5
FATOR_CORRECAO_LINHA = 5.7
ANGULO_CURVA_VERDE = 85
ANGULO_MEIA_VOLTA = 180
VELOCIDADE_PADRAO = 80
POTENCIA_GIRO = 80
DEBOUNCE_VERDE_MS = 300
DISTANCIA_OBSTACULO_CM = 15
REFLEXAO_LINHA_PERDIDA = 80

# ===== INICIALIZAÇÃO DO HARDWARE =====
ev3 = EV3Brick()

# Motores
motor_direita = Motor(Port.A) 
motor_esquerda = Motor(Port.B)

# Sensores
sensor_direita = ColorSensor(Port.S1)
sensor_esquerda = ColorSensor(Port.S2)
sensor_giro = GyroSensor(Port.S3)
proximidade_sensor = UltrasonicSensor(Port.S4)

# Configuração do robô
robot = DriveBase(motor_esquerda, motor_direita, wheel_diameter=55.5, axle_track=104)

# ===== VARIÁVEIS DE CONTROLE =====
verde_detectado_tempo = 0
linha_perdida_contador = 0
MAX_LINHA_PERDIDA = 10  # Tentativas antes de parar

# ===== FUNÇÕES UTILITÁRIAS =====

def resetar_sensores():
    """Reseta todos os sensores para calibração inicial"""
    try:
        sensor_giro.reset_angle(0)
        motor_direita.reset_angle(0)
        motor_esquerda.reset_angle(0)
        print("Sensores resetados com sucesso")
    except Exception as e:
        print(f"Erro ao resetar sensores: {e}")
        ev3.speaker.beep()

def mostrar_status():
    """Exibe status atual dos sensores para debug"""
    print(f"Direita: Cor={sensor_direita.color()}, Reflexão={sensor_direita.reflection()}")
    print(f"Esquerda: Cor={sensor_esquerda.color()}, Reflexão={sensor_esquerda.reflection()}")
    print(f"Giroscópio: {sensor_giro.angle()}°")
    print(f"Distância: {proximidade_sensor.distance()}mm")
    print("---")

def verificar_obstaculo():
    """Verifica se há obstáculo à frente"""
    try:
        distancia = proximidade_sensor.distance()
        return distancia < DISTANCIA_OBSTACULO_CM * 10  # Converter para mm
    except:
        return False

def linha_perdida():
    """Detecta se a linha foi perdida (ambos sensores veem muito branco)"""
    return (sensor_direita.reflection() > REFLEXAO_LINHA_PERDIDA and 
            sensor_esquerda.reflection() > REFLEXAO_LINHA_PERDIDA)

def procurar_linha():
    """Procedimento para procurar a linha quando perdida"""
    print("LINHA PERDIDA! Procurando...")
    ev3.speaker.beep(frequency=1000, duration=200)
    
    # Parar e procurar girando
    robot.stop()
    wait(200)
    
    # Girar para a direita procurando linha
    for _ in range(20):  # Máximo 20 tentativas
        robot.drive(0, 50)  # Girar devagar
        wait(50)
        if not linha_perdida():
            print("Linha encontrada!")
            return True
    
    # Se não encontrou, girar para o outro lado
    for _ in range(40):  # Girar para esquerda
        robot.drive(0, -50)
        wait(50)
        if not linha_perdida():
            print("Linha encontrada!")
            return True
    
    print("ERRO: Linha não encontrada!")
    ev3.speaker.beep(frequency=500, duration=1000)
    return False

def mover_bloco_sgiro(distancia_bloco_mov, potencia_bloco_mov):
    """
    Move o robô em linha reta usando correção giroscópica
    
    Args:
        distancia_bloco_mov: Distância a percorrer em graus de rotação da roda
        potencia_bloco_mov: Potência dos motores (0-100)
    """
    try:
        resetar_sensores()
        
        while abs(motor_direita.angle()) < abs(distancia_bloco_mov):
            # Verificar obstáculo
            if verificar_obstaculo():
                print("OBSTÁCULO! Parando movimento.")
                robot.stop()
                ev3.speaker.beep(frequency=800, duration=500)
                return False
            
            # Calcular correção baseada no giroscópio
            diferenca_bloco_mov = sensor_giro.angle()
            correcao_bloco_mov = diferenca_bloco_mov * FATOR_CORRECAO_GIRO
            
            # Aplicar correção aos motores
            potencia_esquerda = potencia_bloco_mov - correcao_bloco_mov
            potencia_direita = potencia_bloco_mov + correcao_bloco_mov
            
            # Limitar potência entre -100 e 100
            potencia_esquerda = max(-100, min(100, potencia_esquerda))
            potencia_direita = max(-100, min(100, potencia_direita))
            
            motor_esquerda.run(potencia_esquerda)
            motor_direita.run(potencia_direita)
            wait(10)
        
        robot.stop()
        return True
        
    except Exception as e:
        print(f"Erro em mover_bloco_sgiro: {e}")
        robot.stop()
        return False

def virar_bloco_sgiro(graus_bloco_giro, direcao_bloco_giro, potencia_do_giro):
    """
    Faz o robô girar um ângulo específico usando o giroscópio
    
    Args:
        graus_bloco_giro: Ângulo a girar em graus
        direcao_bloco_giro: "direita" ou "esquerda"
        potencia_do_giro: Potência do giro (0-100)
    """
    try:
        print(f"Girando {graus_bloco_giro}° para {direcao_bloco_giro}")
        
        robot.stop()
        wait(100)
        sensor_giro.reset_angle(0)
        
        # Determinar direção do giro
        velocidade_angular = potencia_do_giro if direcao_bloco_giro == "direita" else -potencia_do_giro
        
        # Executar giro
        while abs(sensor_giro.angle()) < abs(graus_bloco_giro):
            robot.drive(0, velocidade_angular)  # Velocidade linear = 0, só gira
            wait(10)
        
        robot.stop()
        wait(200)  # Pausa para estabilizar
        print(f"Giro concluído. Ângulo final: {sensor_giro.angle()}°")
        
    except Exception as e:
        print(f"Erro em virar_bloco_sgiro: {e}")
        robot.stop()

def detectar_verde_com_debounce():
    """
    Detecta marcadores verdes com debounce para evitar múltiplas detecções
    
    Returns:
        tuple: (verde_direita, verde_esquerda, pode_processar)
    """
    global verde_detectado_tempo
    
    verde_direita = sensor_direita.color() == Color.GREEN
    verde_esquerda = sensor_esquerda.color() == Color.GREEN
    
    # Se detectou verde
    if verde_direita or verde_esquerda:
        tempo_atual = time.time() * 1000  # Converter para ms
        
        # Se é a primeira detecção ou passou o tempo de debounce
        if verde_detectado_tempo == 0 or (tempo_atual - verde_detectado_tempo) > DEBOUNCE_VERDE_MS:
            verde_detectado_tempo = tempo_atual
            return verde_direita, verde_esquerda, True
        else:
            return verde_direita, verde_esquerda, False
    else:
        # Reset do timer quando não há verde
        if verde_detectado_tempo != 0:
            verde_detectado_tempo = 0
        return False, False, False

def seguir_linha():
    """Algoritmo principal de seguimento de linha"""
    try:
        # Calcular diferença de reflexão entre sensores
        ref_sensor_direita = sensor_direita.reflection()
        ref_sensor_esquerda = sensor_esquerda.reflection()
        ref_sensores_diferenca = ref_sensor_direita - ref_sensor_esquerda
        
        # Aplicar correção proporcional
        correcao = FATOR_CORRECAO_LINHA * ref_sensores_diferenca
        
        # Mover com correção
        velocidade_linear = VELOCIDADE_PADRAO
        velocidade_angular = correcao
        
        robot.drive(velocidade_linear, velocidade_angular)
        
    except Exception as e:
        print(f"Erro no seguimento de linha: {e}")
        robot.stop()

# ===== PROGRAMA PRINCIPAL =====

def main():
    """Função principal do programa"""
    global linha_perdida_contador
    
    print("=== ROBÔ SEGUIDOR DE LINHA INICIADO ===")
    ev3.speaker.beep(frequency=1000, duration=200)
    
    # Calibração inicial
    resetar_sensores()
    wait(1000)
    
    print("Iniciando loop principal...")
    
    try:
        while True:
            # Mostrar status a cada 100 iterações (debug)
            if linha_perdida_contador % 100 == 0:
                mostrar_status()
            
            # 1. VERIFICAR OBSTÁCULOS
            if verificar_obstaculo():
                print("OBSTÁCULO DETECTADO! Parando...")
                robot.stop()
                ev3.speaker.beep(frequency=500, duration=1000)
                wait(2000)  # Esperar 2 segundos
                continue
            
            # 2. VERIFICAR SE LINHA FOI PERDIDA
            if linha_perdida():
                linha_perdida_contador += 1
                if linha_perdida_contador > MAX_LINHA_PERDIDA:
                    if not procurar_linha():
                        print("ERRO CRÍTICO: Não foi possível encontrar a linha!")
                        break
                    linha_perdida_contador = 0
                continue
            else:
                linha_perdida_contador = 0
            
            # 3. DETECTAR MARCADORES VERDES
            verde_direita, verde_esquerda, pode_processar = detectar_verde_com_debounce()
            
            if pode_processar:
                if verde_direita and verde_esquerda:
                    # Verde nos dois lados = meia volta
                    print("Verde detectado em AMBOS os lados - Fazendo meia volta")
                    ev3.speaker.beep(frequency=1500, duration=300)
                    virar_bloco_sgiro(ANGULO_MEIA_VOLTA, "direita", POTENCIA_GIRO)
                    
                elif verde_direita and not verde_esquerda:
                    # Verde só na direita = virar para esquerda
                    print("Verde detectado na DIREITA - Virando para esquerda")
                    ev3.speaker.beep(frequency=1200, duration=200)
                    virar_bloco_sgiro(ANGULO_CURVA_VERDE, "esquerda", POTENCIA_GIRO)
                    
                elif verde_esquerda and not verde_direita:
                    # Verde só na esquerda = virar para direita
                    print("Verde detectado na ESQUERDA - Virando para direita")
                    ev3.speaker.beep(frequency=1200, duration=200)
                    virar_bloco_sgiro(ANGULO_CURVA_VERDE, "direita", POTENCIA_GIRO)
                
                # Pequena pausa após processar verde
                wait(200)
            else:
                # 4. SEGUIR LINHA NORMALMENTE
                seguir_linha()
            
            # Pequeno delay para não sobrecarregar o processador
            wait(10)
            
    except KeyboardInterrupt:
        print("Programa interrompido pelo usuário")
    except Exception as e:
        print(f"Erro crítico no programa principal: {e}")
        ev3.speaker.beep(frequency=300, duration=1000)
    finally:
        # Cleanup
        robot.stop()
        print("Robô parado. Programa finalizado.")
        ev3.speaker.beep(frequency=800, duration=500)

# Executar programa principal
if __name__ == "__main__":
    main()
