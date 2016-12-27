import ithermodevice
import .measure.Measure

class MockThermoDevice(IThermoDevice.IThermoDevice):
	"""Mock Thermometer"""

	def __init__(self):
		self._ready = False

	def initialize(self):
		"""This mock device does not have anything to initialize"""
		self._ready = True

	@property
	def ready(self):
		"""This mock device is always ready"""
		return self._ready

	def readTemperature(self):
		"""This mock thermometer always returns 22"""
		assert self._ready
		value = 22
		units = "celsius"
		time = datetime.datetime.now()
		temperature = measure.Measure(value, units, time)
		return temperature
