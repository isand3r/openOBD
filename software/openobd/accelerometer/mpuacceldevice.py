from accelerometer.iacceldevice import IAccelDevice
from measure.measure import Measure
import math
import datetime

from mpu6050 import mpu6050

class MPUAccelDevice(IAccelDevice):
    """Thermometer using MPU6050"""
    def __init__(self):
        self.accel  = 0
        self.gyro = 0
        self.accel_mag = 0
        self.init = None
        self._ready = False
        self.units = 'm/s^2'

    def initialize(self):
        self._ready = True
        self.init = mpu6050(0x68)

    @property
    def ready(self) -> bool:
        return self._ready

    def read_accelerometer(self) -> Measure:
        assert self._ready
        time = datetime.datetime.now()
        self.accel = mpu6050.get_accel_data(self.init)
        x = self.accel['x']
        y = self.accel['y']
        z = self.accel['z']
        self.accel_mag = self.calc_magn(x, y, z)
        vector = Measure(self.accel_mag,self.units, time)
        return vector

    def calc_magn(self, X, Y, Z):
        """calculates the magnitude of the accel"""
        assert self._ready
        accel_array = math.sqrt(X**2 + Y**2 + Z**2)
        return accel_array