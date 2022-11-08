# -*- coding: utf-8 -*-
import RPi.GPIO as GPIO
from time import sleep


# 모터 상태
STOP  = 0
FORWARD  = 1
BACKWARD= 2

# 모터 채널
CH1 = 0
CH2 = 1

# PIN 입출력 설정
OUTPUT = 1
INPUT = 0

# PIN 설정
HIGH = 1
LOW = 0

# 실제 핀 정의
#PWM PIN
ENA = 26  #37 pin
ENB = 0   #27 pin

#GPIO PIN
IN1 = 19  #37 pin
IN2 = 13  #35 pin
IN3 = 6   #31 pin
IN4 = 5   #29 pin


class Motor:
    
    def __init__(self, en, ina, inb):
        self.pwm = self.setConfig(en, ina, inb)
        self.ina = ina
        self.inb = inb
        self.en = en
    
    @staticmethod
    def setConfig(en, ina, inb):
        GPIO.setup(en, GPIO.OUT)
        GPIO.setup(ina, GPIO.OUT)
        GPIO.setup(inb, GPIO.OUT)
        pwm = GPIO.PWM(en, 100)
        pwm.start(0)
        return pwm

    def controller(speed, stat):
        self.pwm.ChangeDutyCycle(speed)

        if stat == FORWARD:
            GPIO.output(self.ina, HIGH)
            GPIO.output(self.inb, LOW)
        elif stat == BACKWARD:
            GPIO.output(self.ina, LOW)
            GPIO.output(self.inb, HIGH)
        else:
            GPIO.output(self.ina, LOW)
            GPIO.output(self.inb, HIGH)

