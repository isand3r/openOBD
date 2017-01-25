from measure.measure import Measure
import abc

class IOBDDevice(abc.ABC):

	@abc.abstractmethod
	def initialize(self):
		pass

	@abc.abstractproperty
	def ready(self) -> bool:
		pass

	@abc.abstractmethod
	def read_obd(self):
		pass

	@abc.abstractmethod
	def send_obd(self):
		pass
	@abc.abstractmethod
	def close_bus(self):
		pass

	@abc.abstractmethod
	def init_pids(self):
		pass

	@abc.abstractmethod
	def get_obd_info(self):
		pass
