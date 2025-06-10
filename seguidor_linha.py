#Importo as bibliotécas
from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_B, SpeedPercent, MoveTank
from ev3dev2.sensor import INPUT_1, INPUT_2, INPUT_3, INPUT_4
from ev3dev2.sensor.lego import UltrasonicSensor, GyroSensor, ColorSensor
import time

#Importo os sensores e os motores
motor_direita = LargeMotor(OUTPUT_A)
motor_esquerda = LargeMotor(OUTPUT_B)
proximidade_sensor = UltrasonicSensor(INPUT_1)
sensor_giro = GyroSensor(INPUT_2)
sensor_direita = ColorSensor(INPUT_3)
sensor_esquerda = ColorSensor(INPUT_4)

def mover_bloco_giro(potencia, distancia):
    diametro_da_roda = 10    #diametro da roda em cm
    perimetro_da_roda = 3.14159265359 * diametro_da_roda

    num_graus_distancia = (distancia * 360) / perimetro_da_roda

    sensor_giro.reset_angle(0)    #reseta valores
    motor_esquerda.reset_angle(0)
    motor_direita.reset_angle(0)

    while(abs(motor_esquerda.angle()) < num_graus_distancia):   #"abs" é o valor absoluto, ele é nessessario para fazer a ré nesta mesma condição
        diferenca_bloco_mov = sensor_giro.angle()
        correcao_bloco_mov = diferenca_bloco_mov * 2   #Ajustar o valor "2" se nessessario
    
        motor_esquerda.run_angle(potencia - correcao_bloco_mov, num_graus_distancia)  #*Sem ajustar a rota de acordo com o gyro
        motor_direita.run_angle(potencia + correcao_bloco_mov, num_graus_distancia)
    motor_esquerda.stop()
    motor_direita.stop()    #Depois de andar a distancia definida os motores precisão parar o movimento

def virar_bloco_giro(graus_bloco_giro, direcao_bloco_giro, potencia_do_giro):
    sensor_giro.reset_angle(0)    #reseta valor
    if(direcao_bloco_giro == "direita"):
        while(abs(graus_bloco_giro) > sensor_giro.angle()):
            motor_esquerda.run_angle(potencia_do_giro * (-1), graus_bloco_giro) #Inverter movimento dos motores para o robo virar e continuar no mesmo lugar
            motor_direita.run_angle(potencia_do_giro, graus_bloco_giro)
        motor_esquerda.stop()
        motor_direita.stop()
    elif(direcao_bloco_giro == "esquerda"):
        while(abs(graus_bloco_giro) > sensor_giro.angle()):
            motor_esquerda.run_angle(potencia, graus_bloco_giro)
            motor_direita.run_angle(potencia * (-1), graus_bloco_giro)  #Inverter movimento dos motores para o robo virar e continuar no mesmo lugar
        motor_esquerda.stop()
        motor_direita.stop()

while(True):
    if(proximidade_sensor.distance_centimeters() > 10):
        mover_bloco_giro(50, 15)
        virar_bloco_giro(90, "direita", 50)
    else:
        potencia = 30    #velocidade do robo em porcentagem no Seguidor de Linha   #TROQUE AQUI A VEL.
        ref_sensor_direita = sensor_direita.reflection()
        ref_sensor_esquerda = sensor_esquerda.reflection()    #puxa a informação do sensor
        ref_diferenca = ref_sensor_direita - ref_sensor_esquerda    #define  diferença entre os sensores
        correcao = 0.7 * ref_diferenca    #correcao = "ganho ou erro" * ref_diferenca
        potencia_motor_direito = potencia - correcao
        potencia_motor_esquerdo = potencia + correcao 




def mostrar():
    cen_proximidade_sensor = proximidade_sensor.distance_centimeters()
    cor_sensor_direita = sensor_direita.color()
    cor_sensor_esquerda = sensor_esquerda.color()
    ref_sensor_direita = sensor_direita.reflection()
    ref_sensor_esquerda = sensor_esquerda.reflection()
    print(f"Cor do sensor direito:{cor_sensor_direita}")
    print(f"Cor do sensor esquerdo:{cor_sensor_esquerda}" )
    print(f"Reflexo do sensor direito:{ref_sensor_direita}")
    print(f"Reflexo sensor esquerdo:{ref_sensor_esquerda}" )
    print(f"Proximidade de obejetos (sensor):{cen_proximidade_sensor}" )
    time.sleep(3)