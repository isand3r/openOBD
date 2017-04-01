from accumulator.iaccumulator import IAccumulator
from measure.measure import Measure
import threading

class Accumulator(IAccumulator):
	def __init__(self, name: str, capacity: int):
		assert isinstance(name, str)
		assert isinstance(capacity, int)
		self._name = name
		self._capacity = capacity
		self._measures = list()
		self._lock = threading.Lock()

	@property
	def name(self) -> str:
		return self._name

	@property
	def empty(self) -> bool:
		with self._lock:
			return self._isempty()

	def _isempty(self) -> bool:
		"""Given that the caller holds the lock,
		returns true if _measures is empty"""
		return (len(self._measures) == 0)

	def push(self, measure: Measure):
		with self._lock:
			self._measures.append(measure)
			if (len(self._measures) > self._capacity):
				self._measures.pop(0)

	def clear(self):
		with self._lock:
			self._measures.clear()

	def newest(self) -> Measure:
		"""Return the measure that was most recently pushed"""
		with self._lock:
			if (self._isempty()):
				return None
			return self._measures[len(self._measures)-1]

	def mean(self) -> Measure:
		with self._lock:
			if (self._isempty()):
				return None
			return Accumulator.mean_measure(self._measures)

	def mean_measure(measures) -> Measure:
		"""Given a non-empty list of Measures and given that the caller holds the lock,
		Return a Measure with the mean value and the units & time from the 0th entry"""
		sum_value = 0
		count = 0
		for measure in measures:
			sum_value += measure.value
			count += 1
		average_value = sum_value / count
		return Measure(average_value, measures[0].units, measures[0].time)

	def median(self) -> Measure:
		"""Returns the median (the upper middle measure if there are an 
		even number of measures)"""
		with self._lock:
			if (self._isempty()):
				return None
			median_list = sorted(self._measures, key=lambda x: x.value)
			middle_index = int(len(median_list)/2)
			return median_list[middle_index]

	def minimum(self) -> Measure:
		minimum = None
		with self._lock:
			if (self._isempty()):
				return None
			minimum = self._measures[0]
			for measure in self._measures:
				if (minimum.value > measure.value):
					minimum = measure
			return minimum

	def maximum(self) -> Measure:
		minimum = None
		with self._lock:
			if (self._isempty()):
				return None
			minimum = self._measures[0]
			for measure in self._measures:
				if (minimum.value < measure.value):
					minimum = measure
			return minimum
