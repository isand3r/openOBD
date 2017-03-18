from measure.measure import Measure
import abc

class IAccumulator(abc.ABC):
	"""Used for calculating moving averages for measures"""

	@abc.abstractmethod
	def __init__(self, name: str, capacity: int):
		pass

	@abc.abstractproperty
	def name(self) -> str:
		pass

	@abc.abstractproperty
	def empty(self) -> bool:
		pass

	@abc.abstractmethod
	def push(self, measure: Measure):
		pass

	@abc.abstractmethod
	def clear(self):
		pass

	@abc.abstractmethod
	def newest(self) -> Measure:
		pass

	@abc.abstractmethod
	def mean(self) -> Measure:
		pass

	@abc.abstractmethod
	def median(self) -> Measure:
		pass

	@abc.abstractmethod
	def minimum(self) -> Measure:
		pass

	@abc.abstractmethod
	def maximum(self) -> Measure:
		pass
