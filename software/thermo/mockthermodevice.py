import IThermoDevice
import .measure.Measure

class MockThermoDevice(IThermoDevice.IThermoDevice):
	"""Mock Thermometer"""

	def initialize():
		"""This mock device does not have anything to initialize"""
		return

	def ready():
		"""This mock device is always ready"""
		return True

	def readTemperature():
		"""This mock thermometer always returns 22"""
		return 
