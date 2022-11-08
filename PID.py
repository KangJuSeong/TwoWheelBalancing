from MotorDriver import Motor
from GyroDriver import Gyro

ENA = 26
IN1 = 19
IN2 = 13

ENB = 0
IN3 = 6
IN4 = 5

class PID:
    def __init__(self, kp, ki, kd, goal):
        self.P_term = 0.0
        self.I_term = 0.0
        self.D_term = 0.0
        self.kp = kp
        self.ki = ki
        self.kd = kd
        self.dt = 0.1
        self.err = 0.0
        self.prev_err = 0.0
        self.output = 0
        self.goal = goal
        self.gyro = Gyro()
        self.left = Motor(ENA, IN1, IN2)
        self.right = Motor(ENB, IN3, IN4)

    def controller(self):
        data = self.gyro.get_acc_data()
        x, y, z = data['acc_x'], data['acc_y'], data['acc_z']
        y_slope = self.gyro.get_y_slope(x, y, z)
        
        self.err = self.goal - y_slope
        self.P_term = self.kp * self.err
        self.I_term += self.ki * self.err * self.dt
        self.D_term = self.kd * (self.err - self.prev_err) / self.dt
        self.prev_err = self.err
        if self.I_term > 1000:
            self.I_term = 1000
        elif self.I_term < -1000:
            self.I_term = -1000
        print("P_term : %f, I_term : %f, D_term : %f" % (self.P_term, self.I_term, self.D_term))
        output = self.P_term + self.I_term + self.D_term
        print("output : %d" % int(output))
        return output

    def balancing(self, output):
        speed = output / 100
        direction = Motor.FORWARD
        if speed < 0:
            speed = abs(speed)
            direction = Motor.BACKWARD
        if speed > 100:
            speed = 100
        print("speed : %d dir : %d" % (speed, direction))
        self.left.controller(speed, direction)
        self.right.controller(speed, direction)

