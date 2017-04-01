from volt.mockvoltdevice import MockVoltDevice
import datetime

def test_ready_before_initialize():
	device = MockVoltDevice()
	assert not device.ready

def test_ready_after_initialize():
	device = MockVoltDevice()
	device.initialize()
	assert device.ready

def test_read_voltage():
	device = MockVoltDevice()
	device.initialize()
	voltage = device.read_voltage()
	assert voltage.value == device.INITIAL_VALUE
	assert voltage.units == device.MOCK_UNITS
	assert isinstance(voltage.time, datetime.datetime)
	voltage = device.read_voltage()
	assert voltage.value == device.INITIAL_VALUE + device.INCREMENT_VALUE
	voltage = device.read_voltage()
	assert voltage.value == device.INITIAL_VALUE + (2*device.INCREMENT_VALUE)
