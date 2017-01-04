from accelerometer.iacceldevice import IAccelDevice
from measure.measure import Measure

from mpu6050 import mpu6050

class MPUThermoDevice(IThermoDevice):
    """Thermometer using MPU6050"""

    def __init__(self):
        pass

    def initialize(self):
        print("MPUThermoDevice initialize() method not implemented")

    @property
    def ready(self) -> bool:
        print("MPUThermoDevice ready property not implemented")

    def read_temperature(self) -> Measure:
    	print("MPUThermoDevice read_temperature() method not implemented")
