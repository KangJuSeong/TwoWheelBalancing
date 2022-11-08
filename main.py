from .MotorDriver import Motor
from time import sleep


# 핀 정의
ENA = 26
IN1 = 19
IN2 = 13

ENB = 0
IN3 = 6
IN4 = 5

if __name__ == "__main__":
    left = Motor(ENA, IN1, IN2)
    right = Motor(ENB, IN3, IN4)
    
    left.controller(100, Motor.FORWARD)
    right.controller(100, Motor.FORWARD)
