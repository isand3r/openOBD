import mockthermodevice
import datetime

def test_readyBeforeInitialize():
	device = mockthermodevice.MockThermoDevice()
	assert not device.ready

def test_readyAfterInitialize():
	device = mockthermodevice.MockThermoDevice()
	device.initialize()
	assert device.ready

def test_readTemperature():
	device = mockthermodevice.MockThermoDevice()
	device.initialize()
	temperature = device.readTemperature()
	assert temperature.value == 22
