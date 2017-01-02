from software.thermo.ithermodevice import IThermoDevice
from software.measure.measure import Measure
import datetime

class MockFixedThermoDevice(IThermoDevice):
	"""Mock Thermometer that always gives readings with MOCK_VALUE and MOCK_UNITS"""

	def __init__(self):
		self.MOCK_VALUE = 22
		self.MOCK_UNITS = "celsius"
		self._ready = False


	def initialize(self):
		self._ready = True

	@property
	def ready(self) -> bool:
		return self._ready

	def read_temperature(self) -> Measure:
		"""This mock thermometer always returns 22 celsius"""
		assert self._ready
		time = datetime.datetime.now()
		temperature = Measure(self.MOCK_VALUE, self.MOCK_UNITS, time)
		return temperature
