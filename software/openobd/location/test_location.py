from ..location.location import Location
import datetime

def test_location():
	latitude_value = 49
	longitude_value = -123
	altitude_value = 70
	time = datetime.datetime.now()
	vancouver_location = Location(latitude_value, longitude_value,
		altitude_value, time)
	assert vancouver_location.latitude.value == latitude_value
	assert vancouver_location.latitude.units == 'degrees'
	assert vancouver_location.longitude.value == longitude_value
	assert vancouver_location.longitude.units == 'degrees'
	assert vancouver_location.altitude.value == altitude_value
	assert vancouver_location.altitude.units == 'metres'
