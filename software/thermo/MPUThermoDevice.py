"""MPU6050 Thermometer"""

from IThermoDevice import IThermoDevice

from mpu6050 import mpu6050

class MPUThermoDevice(IThermoDevice):
    def __init__(self):
        self.init = None

    def initialize(self):
        self.init = mpu6050(0x68)

    def getStatus(self):
        print("MPUThermoDevice getStatus not implemented")

    def getTemperature(self):
        return mpu6050.get_temp(self.init)
