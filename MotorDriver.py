import RPi.GPIO as GPIO


OUTPUT = 1
INPUT = 0

HIGH = 1
LOW = 0


class Motor:

    STOP  = 0
    FORWARD  = 1
    BACKWARD= 2

    def __init__(self, en, ina, inb):
        GPIO.setmode(GPIO.BCM)
        self.pwm = self.setConfig(en, ina, inb)
        self.ina = ina
        self.inb = inb
        self.en = en
    
    def setConfig(self, en, ina, inb):
        GPIO.setup(en, GPIO.OUT)
        GPIO.setup(ina, GPIO.OUT)
        GPIO.setup(inb, GPIO.OUT)
        pwm = GPIO.PWM(en, 100)
        pwm.start(0)
        return pwm

    def controller(self, speed, stat):
        self.pwm.ChangeDutyCycle(speed)

        if stat == Motor.FORWARD:
            GPIO.output(self.ina, HIGH)
            GPIO.output(self.inb, LOW)
        elif stat == Motor.BACKWARD:
            GPIO.output(self.ina, LOW)
            GPIO.output(self.inb, HIGH)
        elif stat == Motor.STOP:
            GPIO.output(self.ina, LOW)
            GPIO.output(self.inb, LOW)

