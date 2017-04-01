from volt.ivoltdevice import IVoltDevice
from measure.measure import Measure
import datetime

class MockVoltDevice(IVoltDevice):
	"""Mock voltmeter that gives rising readings"""

	def __init__(self):
		self.INITIAL_VALUE = 0
		self.INCREMENT_VALUE = 1
		self.MOCK_UNITS = "volts"
		self._ready = False
		self._value = self.INITIAL_VALUE

	def initialize(self):
		self._ready = True

	@property
	def ready(self) -> bool:
		return self._ready

	def read_voltage(self) -> Measure:
		"""This mock voltmeter returns an increasing voltage"""
		assert self._ready
		time = datetime.datetime.now()
		voltage = Measure(self._value, self.MOCK_UNITS, time)
		self._value = self._value + self.INCREMENT_VALUE
		return voltage
