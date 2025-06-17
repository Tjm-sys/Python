#!/usr/bin/env pybricks-micropython

"""
Example LEGO® MINDSTORMS® EV3 Robot Educator Color Sensor Down Program
----------------------------------------------------------------------

This program requires LEGO® EV3 MicroPython v2.0.
Download: https://education.lego.com/en-us/support/mindstorms-ev3/python-for-ev3

Building instructions can be found at:
https://education.lego.com/en-us/support/mindstorms-ev3/building-instructions#robot
"""

from pybricks.ev3devices import Motor, ColorSensor, GyroSensor, UltrasonicSensor
from pybricks.parameters import Port
from pybricks.tools import wait
from pybricks.robotics import DriveBase
from pybricks.hubs import EV3Brick
from pybricks.parameters import Port, Stop, Direction, Color

#Importo os sensores e os motores
motor_direita = Motor(Port.A) 
motor_esquerda = Motor(Port.B)
sensor_direira = ColorSensor(Port.S1)
sensor_esquerda = ColorSensor(Port.S2)
sensor_giro = GyroSensor(Port.S3)
proximidade_sensor = UltrasonicSensor(Port.S4)
ref_sensor_direita = ColorSensor(Port.S1).reflection()
ref_sensor_esquerda = ColorSensor(Port.S2).reflection()   #puxa a informação do sensor

diametro_esteira = 30    #diametro da roda em cm
robot = DriveBase(motor_esquerda, motor_direita, wheel_diameter = diametro_esteira, axle_track=104)
potencia_velocidade = 50 #Mudar se necessario

def mover_bloco_giro(potencia, num_graus_distancia):

    sensor_giro.reset_angle(0)    #reseta valores
    motor_esquerda.reset_angle(0)
    motor_direita.reset_angle(0)

    while(abs(motor_esquerda.angle()) < num_graus_distancia):   #"abs" é o valor absoluto, ele é nessessario para fazer a ré nesta mesma condição
        diferenca_bloco_mov = sensor_giro.angle()
        correcao_bloco_mov = diferenca_bloco_mov * 2   #Ajustar o valor "2" se nessessario
    
        motor_esquerda.run_angle(5, potencia - correcao_bloco_mov, num_graus_distancia)  #*Sem ajustar a rota de acordo com o gyro
        motor_direita.run_angle(5, potencia + correcao_bloco_mov, num_graus_distancia)
    motor_esquerda.stop()
    motor_direita.stop()    #Depois de andar a distancia definida os motores precisão parar o movimento

def virar_bloco_giro(graus_bloco_giro, direcao_bloco_giro, potencia_do_giro):
    sensor_giro.reset_angle(0)    #reseta valor
    if(direcao_bloco_giro == "direita"):
        while(abs(graus_bloco_giro) > sensor_giro.angle()):
            motor_esquerda.run_angle(5, potencia_do_giro * (-1), graus_bloco_giro) #Inverter movimento dos motores para o robo virar e continuar no mesmo lugar
            motor_direita.run_angle(5, potencia_do_giro, graus_bloco_giro) # o "5" seriam o grau para andar, coloquei ali para não dar problema de sintaxe
        motor_esquerda.stop()
        motor_direita.stop()
    elif(direcao_bloco_giro == "esquerda"):
        while(abs(graus_bloco_giro) > sensor_giro.angle()):
            motor_esquerda.run_angle(5, potencia, graus_bloco_giro)
            motor_direita.run_angle(5, potencia * (-1), graus_bloco_giro)  #Inverter movimento dos motores para o robo virar e continuar no mesmo lugar
        motor_esquerda.stop()
        motor_direita.stop()

#começamos a seguir a linha:
while(True):
    if(proximidade_sensor.distance_centimeters() > 10):
        mover_bloco_giro(50, 15)
        virar_bloco_giro(90, "direita", 50)
    else:
        potencia = 30    #velocidade do robo em porcentagem no Seguidor de Linha   #TROQUE AQUI A VEL.
        ref_sensor_direita = sensor_direira.reflection()
        ref_sensor_esquerda = sensor_esquerda.reflection()    #puxa a informação do sensor
        ref_sensores_diferenca = ref_sensor_direita - ref_sensor_esquerda    #define  diferença entre os sensores
        correcao = 0.7 * ref_sensores_diferenca    #correcao = "ganho ou erro" * ref_diferenca
        mov_motor_direito = potencia - correcao
        mov_motor_esquerdo = potencia + correcao 
        robot.drive(potencia_velocidade, mov_motor_direito, mov_motor_esquerdo) #VERIFICAR ESTE COMANDO


#comando para testes, mostrando os valores enquanto o código está rodando
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
    time.sleep(5)   #espera 5 segundos para dar tempo de ler os valores