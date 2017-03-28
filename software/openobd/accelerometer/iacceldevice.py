from measure.measure import Measure
import abc

class IAccelDevice(abc.ABC):

	@abc.abstractmethod
	def initialize(self):
		pass

	@abc.abstractproperty
	def ready(self) -> bool:
		pass

	@abc.abstractmethod
	def read_acceleration(self) -> Measure:
		pass
	
	@abc.abstractmethod
	def getX(self):
		pass

	@abc.abstractmethod
	def getY(self):
		pass

	@abc.abstractmethod
	def getZ(self):
		pass

