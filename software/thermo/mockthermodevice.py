import ithermodevice
from ..measure import measure

class MockThermoDevice(ithermodevice.IThermoDevice):
	"""Mock Thermometer that always gives readings with MOCK_VALUE and MOCK_UNITS"""
	MOCK_VALUE = 22
	MOCK_UNITS = "celsius"

	def __init__(self):
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
		value = MOCK_VALUE
		units = MOCK_UNITS
		time = datetime.datetime.now()
		temperature = measure.Measure(value, units, time)
		return temperature
