from accelerometer.mockfixedacceldevice import MockFixedAccelDevice
import datetime

def test_ready_before_initialize():
	device = MockFixedAccelDevice()
	assert not device.ready

def test_ready_after_initialize():
	device = MockFixedAccelDevice()
	device.initialize()
	assert device.ready

def test_read_accelerometer():
	device = MockFixedAccelDevice()
	device.initialize()
	velocity = device.read_acceleration()
	assert velocity.value == device.MOCK_VALUE
	assert velocity.units == device.MOCK_UNITS
	assert isinstance(velocity.time, datetime.datetime)
