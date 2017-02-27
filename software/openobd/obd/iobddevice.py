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
	def read_current_data(self, message: str) -> Measure:
		pass
