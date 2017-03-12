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
		if(message == "location"):
			return self.devicelist[DeviceConstants.DEVICE_GPS].read_location(message)

		#thermo
		elif(message == "temperature"):
			return self.devicelist[DeviceConstants.DEVICE_THERMO].read_temperature(message)

		#accel
		elif(message == "acceleration"):		
			return self.devicelist[DeviceConstants.DEVICE_ACCEL].read_acceleration(message)

		#obd
		elif(self.isOBDmsg(message)):
			return self.devicelist[DeviceConstants.DEVICE_OBD].read_current_data(message)

		else:
			return None

				
	def isOBDmsg(self, message) -> bool:
		for each in MeasureConstants:
			if(message == each):
				return True

		return False	





