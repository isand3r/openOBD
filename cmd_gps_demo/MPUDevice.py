"""The MPU command."""

from mpu6050 import mpu6050
import sys
import time
import os

class MPUDevice():
    def __init__(self):
        self.temperature = 0
        self.accel  = 0
        self.gyro = 0
        self.velocity = 0
        self.init = None

    def initialize(self):
        self.init = mpu6050(0x68)

    def getTemp(self):
        self.temperature = mpu6050.get_temp(self.init)

    def getGyro(self):
        self.gyro = mpu6050.get_gyro_data(self.init)

    def getAccel(self):
        self.accel = mpu6050.get_accel_data(self.init) 

    def printTempStream(self):
        self.getTemp()
        print("Temperature:", self.temperature, " Celsius")

    def printAccelStream(self):
        self.getAccel()
        print("Accelerometer:", self.accel)

    def printGyroStream(self):
        self.getGyro()
        print("Gyroscope:", self.gyro)


        

