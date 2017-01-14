from obd.iobddevice import IOBDDevice
from measure.measure import Measure
import can
import datetime

class OBDDevice(IOBDDevice):
	"""Mock Thermometer that always gives readings with MOCK_VALUE and MOCK_UNITS"""

	def __init__(self):
		self._ready = False
		self.bus = None
		self.canlistener = None


	def initialize(self):
	    can.rc['interface'] = 'socketcan_native'
	    self.bus = can.interface.Bus('can0')
	    self._ready = True
	    
	@property
	def ready(self) -> bool:
		return self._ready

	def read_obd(self) -> Measure:
		"""This obd device to read CAN frames"""
		assert self._ready
		time = datetime.datetime.now()

		try:
			stream = self.bus.recv(timeout=2)
			while(stream is not None):
				print("Message recieved on {}".format(self.bus.channel_info))
				print("The Message recieved is:{}".format(stream))
				return stream
		except can.CanError:
			print("Message could not be recieved")

	def send_obd(self):
		"""This obd device to send CAN frames"""
		assert self._ready
		time = datetime.datetime.now()
		msg = can.Message(arbitration_id=0xc0ffee,
			data=[0, 25, 0, 1, 3, 1, 4, 1],
			extended_id=False)
		try:
			self.bus.send(msg)
			print("Message sent on {}".format(self.bus.channel_info))
		except can.CanError:
			print("Message NOT sent")

	def close_bus(self):
		self.bus.shutdown()
