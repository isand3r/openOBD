import thermo.ithermodevice
import measure.measure
import datetime

class MockThermoDevice(thermo.ithermodevice.IThermoDevice):
	"""Mock Thermometer that always gives readings with MOCK_VALUE and MOCK_UNITS"""

	def __init__(self):
		self.MOCK_VALUE = 22
		self.MOCK_UNITS = "celsius"
		self._ready = False


	def initialize(self):
		self._ready = True

	@property
	def ready(self):
		"""This mock device is always ready"""
		return self._ready

	def read_temperature(self):
		"""This mock thermometer always returns 22"""
		assert self._ready
		time = datetime.datetime.now()
		temperature = measure.measure.Measure(self.MOCK_VALUE, self.MOCK_UNITS, time)
		return temperature
