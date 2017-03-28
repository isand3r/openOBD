from accelerometer.iacceldevice import IAccelDevice
from measure.measure import Measure
import math
import datetime

from mpu6050 import mpu6050

class MPUAccelDevice(IAccelDevice):
    """Accelerometer using MPU6050"""
    def __init__(self):
        self.accel  = {}
        self.gyro = 0
        self.accel_mag = 0
        self.init = None
        self._ready = False
        self.units = 'm/s^2'

    def initialize(self):
        self._ready = True
        self.init = mpu6050(0x68)
        self.accel = mpu6050.get_accel_data(self.init)

    @property
    def ready(self) -> bool:
        return self._ready

    def read_acceleration(self) -> Measure:
        assert self._ready
        time = datetime.datetime.now()
        accel = mpu6050.get_accel_data(self.init)
        x = accel['x'] - self.accel['x']
        y = accel['y'] - self.accel['y'] 
        z = accel['z'] - self.accel['z']
        self.accel_mag = self.calculate_magnitude(x, y, z)
        magnitude_measure = Measure(self.accel_mag,self.units, time)
        return magnitude_measure

    def calculate_magnitude(self, X, Y, Z):
        """Calculates the magnitude of a vector with 3 dimensions"""
        accel_array = math.sqrt(X**2 + Y**2 + Z**2)
        return accel_array

    def getX(self):
        time = datetime.datetime.now()
        return Measure(self.accel['x'],self.MOCK_UNITS, time)

    def getY(self):
        time = datetime.datetime.now()
        return Measure(self.accel['y'],self.MOCK_UNITS, time)

    def getZ(self):
        time = datetime.datetime.now()
        return Measure(self.accel['z'],self.MOCK_UNITS, time)
