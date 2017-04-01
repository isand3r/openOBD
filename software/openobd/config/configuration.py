"""Configuration file parser for openOBD using configparser"""
from config.iconfiguration import IConfiguration
import constants.deviceconstants as DeviceConstants
import configparser

class Configuration(IConfiguration):
	def __init__(self):
		self.DEVICE = 'device'
		self.INTERVAL = 'interval'
		self.MANAGER = 'manager'
		self.MOVING_AVERAGE_ITEMS = 'moving_average_items'
		self.PRINT_INTERVAL = 'print_interval'
		self.RPM_INTERVAL = 'rpm_interval'
		self.SPEED_INTERVAL = 'speed_interval'
		self._config = configparser.ConfigParser()

	def read(self, filename: str):
		self._config.read(filename)

	@property
	def manager_moving_average_items(self) -> str:
		return int(self._config[self.MANAGER][self.MOVING_AVERAGE_ITEMS])

	@property
	def manager_print_interval(self) -> str:
		return float(self._config[self.MANAGER][self.PRINT_INTERVAL])

	@property
	def obd_device(self) -> str:
		return self._config[DeviceConstants.DEVICE_OBD][self.DEVICE]

	@property
	def rpm_interval(self) -> str:
		return float(self._config[DeviceConstants.DEVICE_OBD][self.RPM_INTERVAL])

	@property
	def speed_interval(self) -> str:
		return float(self._config[DeviceConstants.DEVICE_OBD][self.SPEED_INTERVAL])

	@property
	def gps_device(self) -> str:
		return self._config[DeviceConstants.DEVICE_GPS][self.DEVICE]

	@property
	def gps_interval(self) -> str:
		return float(self._config[DeviceConstants.DEVICE_GPS][self.INTERVAL])

	@property
	def thermo_device(self) -> str:
		return self._config[DeviceConstants.DEVICE_THERMO][self.DEVICE]

	@property
	def thermo_interval(self) -> str:
		return float(self._config[DeviceConstants.DEVICE_THERMO][self.INTERVAL])

	@property
	def accel_device(self) -> str:
		return self._config[DeviceConstants.DEVICE_ACCEL][self.DEVICE]

	@property
	def accel_interval(self) -> str:
		return float(self._config[DeviceConstants.DEVICE_ACCEL][self.INTERVAL])

	@property
	def baro_device(self) -> str:
		return self._config[DeviceConstants.DEVICE_BARO][self.DEVICE]

	@property
	def baro_interval(self) -> str:
		return float(self._config[DeviceConstants.DEVICE_BARO][self.INTERVAL])

	@property
	def volt_device(self) -> str:
		return self._config[DeviceConstants.DEVICE_VOLT][self.DEVICE]

	@property
	def volt_interval(self) -> str:
		return float(self._config[DeviceConstants.DEVICE_VOLT][self.INTERVAL])
