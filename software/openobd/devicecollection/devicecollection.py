from thermo.ithermodevice import IThermoDevice
from gps.igpsdevice import IGPSDevice
from accelerometer.iacceldevice import IAccelDevice
from obd.iobddevice import IOBDDevice
from measure.measure import Measure
from location.location import Location
from devicecollection.idevicecollection import IDeviceCollection
import constants.deviceconstants as DeviceConstants
import constants.measureconstants as MeasureConstants
import time
import os

class DeviceCollection(IDeviceCollection):
	def __init__(self, thermoDevice = None, gpsDevice = None, accelDevice = None, obdDevice = None):
		self.devicelist = dict()

		if(thermoDevice != None):
			assert isinstance(thermoDevice, IThermoDevice)
			self.devicelist[DeviceConstants.DEVICE_THERMO] = thermoDevice

		if(accelDevice != None):
			assert isinstance(accelDevice, IAccelDevice)
			self.devicelist[DeviceConstants.DEVICE_ACCEL] = accelDevice

		if(gpsDevice != None):
			assert isinstance(gpsDevice, IGPSDevice)
			self.devicelist[DeviceConstants.DEVICE_GPS] = gpsDevice

		if(obdDevice != None):
			assert isinstance(obdDevice, IOBDDevice)
			self.devicelist[DeviceConstants.DEVICE_OBD] = obdDevice
		

	def init_devices(self):
		for key in self.devicelist:
			self.devicelist[key].initialize()

	def read_current_data(self, message: str):

		#gps
		if(message == DeviceConstants.DEVICE_GPS):
			assert isinstance(self.devicelist[DeviceConstants.DEVICE_GPS], IGPSDevice)
			return self.devicelist[DeviceConstants.DEVICE_GPS].read_location()

		#thermo
		elif(message == DeviceConstants.DEVICE_THERMO):
			assert isinstance(self.devicelist[DeviceConstants.DEVICE_THERMO], IThermoDevice)
			return self.devicelist[DeviceConstants.DEVICE_THERMO].read_temperature()

		#accel
		elif(message == DeviceConstants.DEVICE_ACCEL):		
			assert isinstance(self.devicelist[DeviceConstants.DEVICE_ACCEL], IAccelDevice)
			return self.devicelist[DeviceConstants.DEVICE_ACCEL].read_acceleration()

		#accelx
		elif(message == DeviceConstants.DEVICE_ACCELX):		
			assert isinstance(self.devicelist[DeviceConstants.DEVICE_ACCEL], IAccelDevice)
			return self.devicelist[DeviceConstants.DEVICE_ACCEL].getX()
		#accely
		elif(message == DeviceConstants.DEVICE_ACCELY):		
			assert isinstance(self.devicelist[DeviceConstants.DEVICE_ACCEL], IAccelDevice)
			return self.devicelist[DeviceConstants.DEVICE_ACCEL].getY()
		#accelz
		elif(message == DeviceConstants.DEVICE_ACCELZ):		
			assert isinstance(self.devicelist[DeviceConstants.DEVICE_ACCEL], IAccelDevice)
			return self.devicelist[DeviceConstants.DEVICE_ACCEL].getZ()

		#obd
		elif(self.isOBDmsg(message)):
			assert isinstance(self.devicelist[DeviceConstants.DEVICE_OBD], IOBDDevice)
			return self.devicelist[DeviceConstants.DEVICE_OBD].read_current_data(message)

		else:
			print("Warning: Message Type Not Found")
			return None

	def get_device(self, key):
		return self.devicelist[key]

	def get_all_devices(self):
		return self.devicelist
				
	def isOBDmsg(self, message) -> bool:
		for attr, value in MeasureConstants.__dict__.items():
			if(message == value):
				return True

		return False	





