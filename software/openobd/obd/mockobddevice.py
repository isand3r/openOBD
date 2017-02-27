from obd.iobddevice import IOBDDevice
from measure.measure import Measure
import datetime

class MockOBDDevice(IOBDDevice):
	"""Mock OBD Device that only supports read_current_data for rpm and speed"""

	def __init__(self):
		self._ready = False
		self.MOCK_SPEED = 50
		self.MOCK_RPM = 1500

	def initialize(self):
		self._ready = True

	@property
	def ready(self) -> bool:
		return self._ready

	def read_current_data(self, message: str) -> Measure:
		time = datetime.datetime.now()
		if(message == 'speed'):
			return Measure(self.MOCK_SPEED, 'km/h', time)
		elif(message == 'rpm'):
			return Measure(self.MOCK_RPM, 'rpm', time)
		else:
			print("MockOBDDevice read_current_data not implemented for message: {}".format(message))
