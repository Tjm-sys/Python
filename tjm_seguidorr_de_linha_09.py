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
from pybricks.parameters import Port, Stop, Direction, Color
from pybricks.tools import wait
from pybricks.robotics import DriveBase
from pybricks.hubs import EV3Brick
# pyright: ignore[reportMissingImports]

#Importo os sensores e os motores
motor_direita = Motor(Port.A) 
motor_esquerda = Motor(Port.B)
sensor_direita = ColorSensor(Port.S1)  #Corrigido: era "sensor_direira"
sensor_esquerda = ColorSensor(Port.S2)
sensor_giro = GyroSensor(Port.S3)
proximidade_sensor = UltrasonicSensor(Port.S4)

#Configurações iniciais
diametro_esteira = 55    #diametro da roda em mm
potencia_velocidade = 50 #Mudar se necessario
robot = DriveBase(motor_esquerda, motor_direita, wheel_diameter=diametro_esteira, axle_track=104)

def mover_bloco_sgiro(potencia, num_graus_distancia):
    sensor_giro.reset_angle(0)    #reseta valores
    motor_esquerda.reset_angle(0)
    motor_direita.reset_angle(0)

    while abs(motor_esquerda.angle()) < num_graus_distancia:   
        diferenca_bloco_mov = sensor_giro.angle()
        correcao_bloco_mov = diferenca_bloco_mov * 4.5   #Ajustar o valor "2" se necessario
        motor_esquerda.dc(potencia - correcao_bloco_mov)
        motor_direita.dc(potencia + correcao_bloco_mov)
    
    robot.stop()
    wait(100)

def virar_bloco_sgiro(graus_bloco_giro, direcao_bloco_giro, potencia_do_giro):
    robot.stop()
    wait(100)
    sensor_giro.reset_angle(0)    #reseta valor
    
    if direcao_bloco_giro == "direita":
        while abs(sensor_giro.angle()) < abs(graus_bloco_giro):
            robot.drive(potencia_do_giro, potencia_do_giro)
            #motor_esquerda.dc(potencia_do_giro)
            #motor_direita.dc(-potencia_do_giro)
            wait(10)

    elif direcao_bloco_giro == "esquerda":
        while abs(sensor_giro.angle()) < abs(graus_bloco_giro):
            robot.drive(potencia_do_giro, -potencia_do_giro)
            #motor_esquerda.dc(-potencia_do_giro)
            #motor_direita.dc(potencia_do_giro)
            wait(10)

    robot.stop()
    wait(100)

#Função para testes, mostrando os valores enquanto o código está rodando
def mostrar():
    cen_proximidade_sensor = proximidade_sensor.distance()
    cor_sensor_direita = sensor_direita.color()
    cor_sensor_esquerda = sensor_esquerda.color()
    ref_sensor_direita = sensor_direita.reflection()
    ref_sensor_esquerda = sensor_esquerda.reflection()
    
    print("Cor do sensor direito: {}".format(cor_sensor_direita))
    print("Cor do sensor esquerdo: {}".format(cor_sensor_esquerda))
    print("Reflexo do sensor direito: {}".format(ref_sensor_direita))
    print("Reflexo sensor esquerdo: {}".format(ref_sensor_esquerda))
    print("Proximidade de objetos (sensor): {}".format(cen_proximidade_sensor))


potencia = 80    #velocidade do robo em porcentagem no Seguidor de Linha
contador = 0

#Loop principal - começamos a seguir a linha:
while True:
    show = proximidade_sensor.distance()
    print(":{}".format(show))
    if proximidade_sensor.distance() < 120:  # Distância em mm
        virar_bloco_sgiro(90, "direita", 100)
        mover_bloco_sgiro(80, 100)
        virar_bloco_sgiro(90, "esquerda", 100)
        mover_bloco_sgiro(80, 240)
        virar_bloco_sgiro(90, "esquerda", 100)
        mover_bloco_sgiro(80, 200)
        virar_bloco_sgiro(90, "direita", 100)
    else:
        if sensor_direita.color() == Color.GREEN and sensor_esquerda.color() != Color.GREEN:
            print("verde na esquerda")
            virar_bloco_sgiro(85, "esquerda", 80)

        elif sensor_esquerda.color() == Color.GREEN and sensor_direita.color() != Color.GREEN:
            print("verde na direita")
            virar_bloco_sgiro(85, "direita", 80)

        elif sensor_direita.color() == Color.GREEN and sensor_esquerda.color() == Color.GREEN:
            #girar 180°
            print("verde nos dois")
            virar_bloco_sgiro(180, "direita", 80)    #angulos par, e potencia impar
        
        else:
            wait(10)
            #Seguidor de linha
            ref_sensor_direita = sensor_direita.reflection()
            ref_sensor_esquerda = sensor_esquerda.reflection()
            ref_sensores_diferenca = ref_sensor_direita - ref_sensor_esquerda
            correcao = 5.7 * ref_sensores_diferenca
    
            #Usa drive() para fazer o movimento
            velocidade_linear = potencia
            velocidade_angular = correcao
            robot.drive(velocidade_linear, velocidade_angular)
    #mostrar()