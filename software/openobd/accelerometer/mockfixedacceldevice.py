from accelerometer.iacceldevice import IAccelDevice
from measure.measure import Measure
import datetime
import numpy as np

class MockFixedAccelDevice(IAccelDevice):
	"""Mock Thermometer that always gives readings with MOCK_VALUE and MOCK_UNITS"""

	def __init__(self):
		self.MOCK_X = 2.2
		self.MOCK_Y = -3.1
		self.MOCK_Z = -0.2
		self.MOCK_UNITS = "m/s"
		self.MOCK_MAG = None
		self._ready = False


	def initialize(self):
		self._ready = True
		self.MOCK_MAG = self.calc_magn(self.MOCK_X, self.MOCK_Y, self.MOCK_Z)

	@property
	def ready(self) -> bool:
		return self._ready

	def read_accelerometer(self) -> Measure:
		"""This mock accelerometer """
		assert self._ready
		time = datetime.datetime.now()
		vector = Measure(self.MOCK_MAG,self.MOCK_UNITS, time)
		return vector

	def calc_magn(self, X, Y, Z):
		"""calculates the magnitude of the velocity"""
		assert self._ready
		accel_array = np.array([X, Y, Z])
		return np.linalg.norm(accel_array)
