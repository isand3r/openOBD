from software.thermo.ithermodevice import IThermoDevice
from software.measure.measure import Measure
import datetime

class MockRisingThermoDevice(IThermoDevice):
	"""Mock thermometer that gives readings starting at INITIAL_VALUE that increase by INCREMENT_VALUE"""

	def __init__(self):
		self.INITIAL_VALUE = 0
		self.INCREMENT_VALUE = 1
		self.MOCK_UNITS = "celsius"
		self._ready = False
		self._value = self.INITIAL_VALUE


	def initialize(self):
		self._ready = True

	@property
	def ready(self):
		return self._ready

	def read_temperature(self):
		"""This mock thermometer returns an increasing temperature"""
		assert self._ready
		time = datetime.datetime.now()
		temperature = Measure(self._value, self.MOCK_UNITS, time)
		self._value = self._value + self.INCREMENT_VALUE
		return temperature
