from MotorDriver import Motor 
from GyroDriver import Gyro
from PID import PID
from time import sleep
import RPi.GPIO as GPIO


ENA = 26
IN1 = 19
IN2 = 13

ENB = 0
IN3 = 5 # 5
IN4 = 6 # 6

def MotorTest(ENA, IN1, IN2, ENB, IN3, IN4):
    left = Motor(ENB, IN1, IN2)
    right = Motor(ENA, IN3, IN4)
 
    left.controller(100, Motor.FORWARD)
    right.controller(100, Motor.FORWARD)
    sleep(6)
    left.controller(100, Motor.BACKWARD)
    right.controller(100, Motor.BACKWARD)
    sleep(6)
    left.controller(0, Motor.STOP)
    right.controller(0, Motor.STOP)
    GPIO.cleanup()

def GyroTest():
    gyro = Gyro()
    while True:
        data = gyro.get_acc_data()
        print(gyro.get_y_slope(data['acc_x'], data['acc_y'], data['acc_z']))

def PIDTest():
    # 1600 3500 50 12
    pid = PID(1700.0, 3600.0, 45.0, 11)
    while True:
        output = pid.controller()
        pid.balancing(output)

if __name__ == "__main__":
    # GyroTest()
    # MotorTest(ENA, IN1, IN2, ENB, IN3, IN4)
    PIDTest()


