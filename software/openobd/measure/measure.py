import numbers
import datetime

class Measure():
	"""Measurement with a numerical value, units, and time"""

	def __init__(self, value: numbers.Number, units: str, time: datetime.datetime):
		assert isinstance(value, numbers.Number)
		assert isinstance(units, str)
		assert isinstance(time, datetime.datetime)
		self._value = value
		self._units = units
		self._time = time

	@property
	def value(self) -> numbers.Number:
		"""Return the numerical value of the measurement itself"""
		return self._value

	@property
	def units(self) -> str:
		"""Return the units for the numerical value"""
		return self._units

	@property
	def time(self) -> datetime.datetime:
		"""Return the time that the measurement was taken"""
		return self._time

	def average_measure(measures):
		"""Given a non-empty list of Measures,
		Return a Measure with the mean value and the units & time from the 0th entry"""
		sum_value = 0
		count = 0
		average_value = 0
		
		for measure in measures:
			sum_value += measure.value
			count += 1
			average_value = sum_value / count
		return Measure(average_value, measures[0].units, measures[0].time)
