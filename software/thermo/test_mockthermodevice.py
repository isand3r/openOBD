import mockthermodevice
import datetime

def test_ready_before_initialize():
	device = mockthermodevice.MockThermoDevice()
	assert not device.ready

def test_ready_after_initialize():
	device = mockthermodevice.MockThermoDevice()
	device.initialize()
	assert device.ready

def test_read_temperature():
	device = mockthermodevice.MockThermoDevice()
	device.initialize()
	temperature = device.read_temperature()
	assert temperature.value == MockThermoDevice.MOCK_TEMPERATURE
	assert temperature.units == MockThermoDevice.MOCK_UNITS
	assert isinstance(temperature.time, datetime.datetime)
