"""Automates reading from devices"""
from api.api import Api
from gps.igpsdevice import IGPSDevice
from thermo.ithermodevice import IThermoDevice
from obd.iobddevice import IOBDDevice
from accelerometer.iacceldevice import IAccelDevice

class Manager():
	def __init__(self, gpsDevice: IGPSDevice, thermoDevice: IThermoDevice,
		accelDevice: IAccelDevice, api: Api, obdDevice: IOBDDevice):
		assert isinstance(gpsDevice, IGPSDevice)
		self._gpsDevice = gpsDevice
		self._gpsDevice.initialize()
		assert isinstance(thermoDevice, IThermoDevice)
		self._thermoDevice = thermoDevice
		self._thermoDevice.initialize()
		assert isinstance(accelDevice, IAccelDevice)
		self._accelDevice = accelDevice
		self._accelDevice.initialize()
		assert isinstance(api, Api)
		self._api = api
		self._api.get_auth()
		assert isinstance(obdDevice, IOBDDevice)
		self._obdDevice = obdDevice
		self._obdDevice.initialize()
