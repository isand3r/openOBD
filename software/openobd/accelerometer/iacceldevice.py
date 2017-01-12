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
	def read_accelerometer(self) -> Measure:
		pass

	@abc.abstractmethod
	def calc_magn(self, X, Y, Z):
		pass