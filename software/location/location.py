from software.measure.measure import Measure

class Location():
	"""3D Location with coordinates in degrees and altitude in metres"""

	def __init__(self, latitude, longitude, altitude, time):
		self._latitude = Measure(latitude, "degrees", time)
		self._longitude = Measure(longitude, "degrees", time)
		self._altitude = Measure(altitude, "metres", time)

	@property
	def latitude(self):
		return self._latitude

	@property
	def longitude(self):
		return self._longitude

	@property
	def altitude(self):
		return self._altitude
