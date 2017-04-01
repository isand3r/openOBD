from measure.measure import measure
import abc

class IVoltDevice(abc.ABC):

	@abc.abstractmethod
	def initialize(self):
		pass

	@abc.abstractproperty
	def ready(self) -> bool:
		pass

	@abc.abstractmethod
	def read_voltage(self) -> Measure:
		pass
