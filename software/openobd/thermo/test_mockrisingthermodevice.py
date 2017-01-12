from thermo.mockrisingthermodevice import MockRisingThermoDevice
import datetime

def test_ready_before_initialize():
	device = MockRisingThermoDevice()
	assert not device.ready

def test_ready_after_initialize():
	device = MockRisingThermoDevice()
	device.initialize()
	assert device.ready

def test_read_temperature():
	device = MockRisingThermoDevice()
	device.initialize()
	temperature = device.read_temperature()
	assert temperature.value == device.INITIAL_VALUE
	assert temperature.units == device.MOCK_UNITS
	assert isinstance(temperature.time, datetime.datetime)
	temperature = device.read_temperature()
	assert temperature.value == device.INITIAL_VALUE + device.INCREMENT_VALUE
	temperature = device.read_temperature()
	assert temperature.value == device.INITIAL_VALUE + (2*device.INCREMENT_VALUE)
