class MockThermoDevice(IThermoDevice):
	"""Mock Thermometer"""

	def initialize():
		"""This mock device does not have anything to initialize"""
		return

	def getStatus():
		"""This mock device is always ready"""
		print("MockThermoDevice getStatus not implemented")

	def getTemperature():
		"""This mock thermometer always returns 22"""
		return 22
