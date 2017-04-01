from thermo.ithermodevice import IThermoDevice
from gps.igpsdevice import IGPSDevice
from accelerometer.iacceldevice import IAccelDevice
from volt.ivoltdevice import IVoltDevice
from baro.ibarodevice import IBaroDevice
from obd.iobddevice import IOBDDevice
from measure.measure import Measure
from location.location import Location
from devicecollection.idevicecollection import IDeviceCollection
import constants.deviceconstants as DeviceConstants
import constants.measureconstants as MeasureConstants
import time
import os

class DeviceCollection(IDeviceCollection):
	def __init__(self, thermoDevice = None, gpsDevice = None, accelDevice = None,
		voltDevice = None, baroDevice = None, obdDevice = None):
		self._deviceList = dict()

		if(thermoDevice != None):
			assert isinstance(thermoDevice, IThermoDevice)
			self._deviceList[DeviceConstants.DEVICE_THERMO] = thermoDevice

		if(accelDevice != None):
			assert isinstance(accelDevice, IAccelDevice)
			self._deviceList[DeviceConstants.DEVICE_ACCEL] = accelDevice

		if(gpsDevice != None):
			assert isinstance(gpsDevice, IGPSDevice)
			self._deviceList[DeviceConstants.DEVICE_GPS] = gpsDevice

		if(voltDevice != None):
			assert isinstance(voltDevice, IVoltDevice)
			self._deviceList[DeviceConstants.DEVICE_VOLT] = voltDevice

		if(baroDevice != None):
			assert isinstance(baroDevice, IBaroDevice)
			self._deviceList[DeviceConstants.DEVICE_BARO] = baroDevice

		if(obdDevice != None):
			assert isinstance(obdDevice, IOBDDevice)
			self._deviceList[DeviceConstants.DEVICE_OBD] = obdDevice
		

	def init_devices(self):
		for key in self._deviceList:
			self._deviceList[key].initialize()

	def read_current_data(self, message: str):

		#gps
		if(message == DeviceConstants.DEVICE_GPS):
			assert isinstance(self._deviceList[DeviceConstants.DEVICE_GPS], IGPSDevice)
			return self._deviceList[DeviceConstants.DEVICE_GPS].read_location()

		#thermo
		elif(message == DeviceConstants.DEVICE_THERMO):
			assert isinstance(self._deviceList[DeviceConstants.DEVICE_THERMO], IThermoDevice)
			return self._deviceList[DeviceConstants.DEVICE_THERMO].read_temperature()

		#accel
		elif(message == DeviceConstants.DEVICE_ACCEL):		
			assert isinstance(self._deviceList[DeviceConstants.DEVICE_ACCEL], IAccelDevice)
			return self._deviceList[DeviceConstants.DEVICE_ACCEL].read_acceleration()

		#volt
		elif(message == DeviceConstants.DEVICE_VOLT):		
			assert isinstance(self._deviceList[DeviceConstants.DEVICE_VOLT], IVoltDevice)
			return self._deviceList[DeviceConstants.DEVICE_VOLT].read_voltage()

		#baro
		elif(message == DeviceConstants.DEVICE_BARO):		
			assert isinstance(self._deviceList[DeviceConstants.DEVICE_BARO], IBaroDevice)
			return self._deviceList[DeviceConstants.DEVICE_BARO].read_pressure()

		#obd
		elif(self.isOBDmsg(message)):
			assert isinstance(self._deviceList[DeviceConstants.DEVICE_OBD], IOBDDevice)
			return self._deviceList[DeviceConstants.DEVICE_OBD].read_current_data(message)

		else:
			print("Warning: Message Type Not Found")
			return None

				
	def isOBDmsg(self, message) -> bool:
		for attr, value in MeasureConstants.__dict__.items():
			if(message == value):
				return True
		return False	
