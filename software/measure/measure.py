import numbers
import datetime

class Measure():
	"""Measurement with a numerical value, units, and time"""

	def __init__(self, value, units, time):
		assert isinstance(value, numbers.Number)
		assert isinstance(units, str)
		assert isinstance(time, datetime.datetime)
		self._value = value
		self._units = units
		self._time = time

	@property
	def value(self):
		"""Return the numerical value of the measurement itself"""
		return self._value

	@property
	def units(self):
		"""Return the units for the numerical value"""
		return self._units

	@property
	def time(self):
		"""Return the time that the measurement was taken"""
		return self._time
