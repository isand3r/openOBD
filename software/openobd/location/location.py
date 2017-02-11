from measure.measure import Measure
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

	def average_location(locations):
		"""Given a non-empty list of Locations,
		Return a Location with mean lon/lat/alt values and time from the 0th entry"""
		sum_latitude_value = 0
		sum_longitude_value = 0
		sum_altitude_value = 0
		count = 0
		for location in locations:
			sum_latitude_value += location.latitude.value
			sum_longitude_value += location.longitude.value
			sum_altitude_value += location.altitude.value
			count += 1
		average_latitude_value = sum_latitude_value / count
		average_longitude_value = sum_longitude_value / count
		average_altitude_value = sum_altitude_value / count
		return Location(average_latitude_value, average_longitude_value,
			average_altitude_value, locations[0].latitude.time)


