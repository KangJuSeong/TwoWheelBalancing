import smbus			#import SMBus module of I2C
from time import sleep          #import


class Gyro:

    PWR_MGMT_1   = 0x6B
    SMPLRT_DIV   = 0x19
    CONFIG       = 0x1A
    GYRO_CONFIG  = 0x1B
    INT_ENABLE   = 0x38
    ACCEL_XOUT_H = 0x3B
    ACCEL_YOUT_H = 0x3D
    ACCEL_ZOUT_H = 0x3F
    GYRO_XOUT_H  = 0x43
    GYRO_YOUT_H  = 0x45
    GYRO_ZOUT_H  = 0x47
    Device_Address = 0x68
    	
    def __init__(self):
        self.bus = smbus.SMBus(1) 
    	self.bus.write_byte_data(Device_Address, SMPLRT_DIV, 7)
    	self.bus.write_byte_data(Device_Address, PWR_MGMT_1, 1)
    	self.bus.write_byte_data(Device_Address, CONFIG, 0)
    	self.bus.write_byte_data(Device_Address, GYRO_CONFIG, 24)
    	self.bus.write_byte_data(Device_Address, INT_ENABLE, 1)

    def read_raw_data(self, addr):
        high = self.bus.read_byte_data(Device_Address, addr)
        low = self.bus.read_byte_data(Device_Address, addr+1)
        
        value = ((high << 8) | low)
            
        if(value > 32768):
            value = value - 65536
        return value

    def get_acc_data(self):
        return {
                    'acc_x' : read_raw_data(ACCEL_XOUT_H)/16384.0,
                    'acc_y' : read_raw_data(ACCEL_YOUT_H)/16384.0,
                    'acc_z' : read_raw_data(ACCEL_ZOUT_H)/16384.0
                }

    def get_gyro_data(self):
        return {
                    'gyro_x' : read_raw_data(GYRO_XOUT_H)/131,
                    'gyro_y' : read_raw_data(GYRO_YOUT_H)/131,
                    'gyro_z' : read_raw_data(GYRO_ZOUT_H)/131
                }
    
