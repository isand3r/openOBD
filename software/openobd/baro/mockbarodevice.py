from baro.ibarodevice import IBaroDevice
from measure.measure import Measure
import datetime

class MockBaroDevice(IBaroDevice):
	"""Mock barometer that gives rising readings"""

	def __init__(self):
		self.INITIAL_VALUE = 100
		self.INCREMENT_VALUE = 1
		self.MOCK_UNITS = "kPa"
		self._ready = False
		self._value = self.INITIAL_VALUE

	def initialize(self):
		self._ready = True

	@property
	def ready(self) -> bool:
		return self._ready

	def read_pressure(self) -> Measure:
		"""This mock barometer returns an increasing pressure"""
		assert self._ready
		time = datetime.datetime.now()
		pressure = Measure(self._value, self.MOCK_UNITS, time)
		self._value = self._value + self.INCREMENT_VALUE
		return pressure
