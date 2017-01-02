from software.measure.measure import Measure
import numbers

class Location():
	"""3D Location with coordinates in degrees and altitude in metres"""

	def __init__(self, latitude: numbers.Number, longitude: numbers.Number,
		altitude: numbers.Number, time: numbers.Number):
		self._latitude = Measure(latitude, 'degrees', time)
		self._longitude = Measure(longitude, 'degrees', time)
		self._altitude = Measure(altitude, 'metres', time)

	@property
	def latitude(self) -> Measure:
		return self._latitude

	@property
	def longitude(self) -> Measure:
		return self._longitude

	@property
	def altitude(self) -> Measure:
		return self._altitude
