from .measure.Measure import Measure

class Location():
	"""3D Location"""

	def __init__(self, latitude, longitude, altitude, time):
		self.latitude = Measure(latitude, "degrees", time)
		self.longitude = Measure(longitude, "degrees", time)
		self.altitude = Measure(altitude, "metres", time)

	def getLatitude(self):
		return self.latitude

	def getLongitude(self):
		return self.longitude

	def getAltitude(self):
		return self.altitude
