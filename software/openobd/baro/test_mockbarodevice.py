from baro.mockbarodevice import MockBaroDevice
import datetime

def test_ready_before_initialize():
	device = MockBaroDevice()
	assert not device.ready

def test_ready_after_initialize():
	device = MockBaroDevice()
	device.initialize()
	assert device.ready

def test_read_pressure():
	device = MockBaroDevice()
	device.initialize()
	pressure = device.read_pressure()
	assert pressure.value == device.INITIAL_VALUE
	assert pressure.units == device.MOCK_UNITS
	assert isinstance(pressure.time, datetime.datetime)
	pressure = device.read_pressure()
	assert pressure.value == device.INITIAL_VALUE + device.INCREMENT_VALUE
	pressure = device.read_pressure()
	assert pressure.value == device.INITIAL_VALUE + (2*device.INCREMENT_VALUE)
