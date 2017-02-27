from obd.mockobddevice import MockOBDDevice
import datetime

def test_initialize_ready():
	device = MockOBDDevice()
	assert not device.ready
	device.initialize()
	assert device.ready

def test_read_current_speed():
	device = MockOBDDevice()
	device.initialize()
	speed = device.read_current_data('speed')
	assert speed.value == device.MOCK_SPEED
	assert speed.units == 'km/h'


def test_read_current_rpm():
	device = MockOBDDevice()
	device.initialize()
	rpm = device.read_current_data('rpm')
	assert rpm.value == device.MOCK_RPM
	assert rpm.units == 'rpm'
