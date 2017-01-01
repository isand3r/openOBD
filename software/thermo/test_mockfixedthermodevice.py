from software.thermo.mockfixedthermodevice import MockFixedThermoDevice
import datetime

def test_ready_before_initialize():
	device = MockFixedThermoDevice()
	assert not device.ready

def test_ready_after_initialize():
	device = MockFixedThermoDevice()
	device.initialize()
	assert device.ready

def test_read_temperature():
	device = MockFixedThermoDevice()
	device.initialize()
	temperature = device.read_temperature()
	assert temperature.value == device.MOCK_VALUE
	assert temperature.units == device.MOCK_UNITS
	assert isinstance(temperature.time, datetime.datetime)
