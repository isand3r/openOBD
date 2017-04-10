from thermo.ithermodevice import IThermoDevice
from measure.measure import Measure
import datetime

from mpu6050 import mpu6050

class MPUThermoDevice(IThermoDevice):
    """Thermometer using MPU6050"""

    def __init__(self):
        self.temperature = 0
        self.units = 'Celsius'
        self._ready = False
        self.init = None


    def initialize(self):
        self.init = mpu6050(0x69)
        self._ready = True

    @property
    def ready(self) -> bool:
        return self._ready

    def read_temperature(self) -> Measure:
        assert self._ready
        time = datetime.datetime.now()
        self.temperature = mpu6050.get_temp(self.init)
        temp = Measure(self.temperature, self.units, time)
        return temp
