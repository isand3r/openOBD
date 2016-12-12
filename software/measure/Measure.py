import abc

class Measure():
	"""Measurement with a value, units, and time"""

	def __init__(self, value, units, time):
		self.value = value
		self.units = units
		self.time = time

	def getValue(self):
		"""Return the value of the measurement itself"""
		return self.value

	def getUnits(self):
		"""Return the units for the measurement"""
		return self.units

    def getTime(self):
    	"""Return the time that the measurement was taken"""
    	return self.time
