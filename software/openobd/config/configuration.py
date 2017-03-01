"""Configuration file parser for openOBD using configparser"""
from config.iconfiguration import IConfiguration
import configparser

class Configuration(IConfiguration):
	def __init__(self):
		self.DEVICE = 'device'
		self.INTERVAL = 'interval'
		self.MANAGER = 'manager'
		self.MOVING_AVERAGE_ITEMS = 'moving_average_items'
		self.PRINT_INTERVAL = 'print_interval'
		self.OBD = 'obd'
		self.RPM_INTERVAL = 'rpm_interval'
		self.SPEED_INTERVAL = 'speed_interval'
		self.GPS = 'gps'
		self.THERMO = 'thermo'
		self.ACCEL = 'accel'
		self._config = configparser.ConfigParser()

	def read(self, filename: str):
		self._config.read(filename)

	@property
	def manager_moving_average_items(self) -> str:
		return int(self._config[self.MANAGER][self.MOVING_AVERAGE_ITEMS])

	@property
	def manager_print_interval(self) -> str:
		return int(self._config[self.MANAGER][self.PRINT_INTERVAL])

	@property
	def obd_device(self) -> str:
		return self._config[self.OBD][self.DEVICE]

	@property
	def rpm_interval(self) -> str:
		return float(self._config[self.OBD][self.RPM_INTERVAL])

	@property
	def speed_interval(self) -> str:
		return float(self._config[self.OBD][self.SPEED_INTERVAL])

	@property
	def gps_device(self) -> str:
		return self._config[self.GPS][self.DEVICE]

	@property
	def gps_interval(self) -> str:
		return float(self._config[self.GPS][self.INTERVAL])

	@property
	def thermo_device(self) -> str:
		return self._config[self.THERMO][self.DEVICE]

	@property
	def thermo_interval(self) -> str:
		return float(self._config[self.THERMO][self.INTERVAL])

	@property
	def accel_device(self) -> str:
		return self._config[self.ACCEL][self.DEVICE]

	@property
	def accel_interval(self) -> str:
		return float(self._config[self.ACCEL][self.INTERVAL])
