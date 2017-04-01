from devicecollection.devicecollection import DeviceCollection
from volt.mockvoltdevice import MockVoltDevice
import constants.deviceconstants as DeviceConstants
import datetime

def test_read_voltage():
	voltdevice = MockVoltDevice()
	voltdevice.initialize()
	devicecollection = DeviceCollection(voltDevice = voltdevice)
	voltage = devicecollection.read_current_data(DeviceConstants.DEVICE_VOLT)
	assert voltage.value == voltdevice.INITIAL_VALUE
	assert voltage.units == voltdevice.MOCK_UNITS
	assert isinstance(voltage.time, datetime.datetime)
	voltage = devicecollection.read_current_data(DeviceConstants.DEVICE_VOLT)
	assert voltage.value == voltdevice.INITIAL_VALUE + voltdevice.INCREMENT_VALUE
	voltage = devicecollection.read_current_data(DeviceConstants.DEVICE_VOLT)
	assert voltage.value == voltdevice.INITIAL_VALUE + (2*voltdevice.INCREMENT_VALUE)
