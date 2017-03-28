from accelerometer.iacceldevice import IAccelDevice
from measure.measure import Measure
import datetime
import math

class MockFixedAccelDevice(IAccelDevice):
	"""Mock Thermometer that always gives the same reading"""

	def __init__(self):
		self.accel  = {'x' : 2.2, 'y' : -3.1, 'z' : -0.2}
		self.MOCK_UNITS = "m/s^2"
		self.MOCK_VALUE = None
		self._ready = False

	def initialize(self):
		self._ready = True
		self.MOCK_VALUE = self.calculate_magnitude(self.accel['x'], self.accel['y'],
			self.accel['z'])

	@property
	def ready(self) -> bool:
		return self._ready

	def read_acceleration(self) -> Measure:
		"""This mock accelerometer """
		assert self._ready
		time = datetime.datetime.now()
		magnitude_measure = Measure(self.MOCK_VALUE,self.MOCK_UNITS, time)
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
