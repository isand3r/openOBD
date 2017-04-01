from location.location import Location
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

def test_average_location():
	time0 = datetime.datetime.now()
	latitude_value0 = 49.00
	latitude_value1 = 49.03
	latitude_value2 = 49.12
	average_latitude_value = (latitude_value0+latitude_value1+latitude_value2)/3
	longitude_value0 = -123.00
	longitude_value1 = -123.03
	longitude_value2 = -123.09
	average_longitude_value = (longitude_value0+longitude_value1+longitude_value2)/3
	altitude_value0 = 70
	altitude_value1 = 70.5
	altitude_value2 = 71
	average_altitude_value = (altitude_value0+altitude_value1+altitude_value2)/3
	location0 = Location(latitude_value0, longitude_value0, altitude_value0, time0)
	location1 = Location(latitude_value1, longitude_value1, altitude_value1, time0)
	location2 = Location(latitude_value2, longitude_value2, altitude_value2, time0)
	locations = list()
	locations.append(location0)
	locations.append(location1)
	locations.append(location2)
	average_location = Location.average_location(locations)
	assert average_location.latitude.value == average_latitude_value
	assert average_location.longitude.value == average_longitude_value
	assert average_location.altitude.value == average_altitude_value
