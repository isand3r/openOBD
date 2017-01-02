from software.measure.measure import Measure
import abc

class IThermoDevice(abc.ABC):

	@abc.abstractmethod
	def initialize(self):
		pass

	@abc.abstractproperty
	def ready(self) -> bool:
		pass

	@abc.abstractmethod
	def read_temperature(self) -> Measure:
		pass
