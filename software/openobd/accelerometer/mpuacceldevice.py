from accelerometer.iacceldevice import IAccelDevice
from measure.measure import Measure
import math
import datetime

from mpu6050 import mpu6050

class MPUAccelDevice(IAccelDevice):
    """Accelerometer using MPU6050"""
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

    def read_acceleration(self) -> Measure:
        assert self._ready
        time = datetime.datetime.now()
        self.accel = mpu6050.get_accel_data(self.init)
        x = self.accel['x']
        y = self.accel['y']
        z = self.accel['z']
        self.accel_magnitude = self.calculate_magnitude(x, y, z)
        magnitude_measure = Measure(self.accel_mag,self.units, time)
        return magnitude_measure

    def calculate_magnitude(self, X, Y, Z):
        """Calculates the magnitude of a vector with 3 dimensions"""
        accel_array = math.sqrt(X**2 + Y**2 + Z**2)
        return accel_array