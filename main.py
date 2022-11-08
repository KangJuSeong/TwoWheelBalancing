from MotorDriver import Motor 
from GyroDriver import Gyro
from time import sleep
import RPi.GPIO as GPIO


ENA = 26
IN1 = 19
IN2 = 13

ENB = 0
IN3 = 6
IN4 = 5

def MotorTest(ENA, IN1, IN2, ENB, IN3, IN4):
    left = Motor(ENA, IN1, IN2)
    right = Motor(ENB, IN3, IN4)
 
    left.controller(100, Motor.FORWARD)
    right.controller(100, Motor.FORWARD)
    sleep(6)
    left.controller(100, Motor.BACKWARD)
    right.controller(100, Motor.BACKWARD)
    sleep(6)
    left.controller(0, Mortr.STOP)
    right.controller(0, Motor.STOP)
    GPIO.cleanup()

def GyroTest():
    gyro = Gyro()
    while True:
        data = gyro.get_acc_data()
        print(gyro.get_y_slope(data['acc_x'], data['acc_y'], data['acc_z']))

if __name__ == "__main__":
    GyroTest()
    # MotorTest()

