import types

class Measure():
	"""Measurement with a numerical value, units, and time"""

	def __init__(self, value, units, time):
		assert isinstance(value, TODO), "value is not a TODO: %TODO", % value
		assert isinstance(units, types.StringType), "units is not a string: %r" % units
		assert isinstance(time, TODO), "time is not a TODO: %TODO", % time
		self.value = value
		self.units = units
		self.time = time

	def getValue(self):
		"""Return the numerical value of the measurement itself"""
		return self.value

	def getUnits(self):
		"""Return the units for the numerical value"""
		return self.units

	def getTime(self):
		"""Return the time that the measurement was taken"""
		return self.time
