from software.gps.mockfixedgpsdevice import MockFixedGPSDevice

def test_read_fixed_location():
	device = MockFixedGPSDevice()
	assert not device.status
	device.initialize()
	assert device.status
	location1 = device.read_location()
	assert location1.latitude.value == device.MOCK_LATITUDE_VALUE
	assert location1.longitude.value == device.MOCK_LONGITUDE_VALUE
	assert location1.altitude.value == device.MOCK_ALTITUDE_VALUE
	location2 = device.read_location()
	assert location2.latitude.value == device.MOCK_LATITUDE_VALUE
	assert location2.longitude.value == device.MOCK_LONGITUDE_VALUE
	assert location2.altitude.value == device.MOCK_ALTITUDE_VALUE
	assert location1.altitude.time != location2.altitude.time
