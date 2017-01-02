"""Configuration file parser for openOBD using configparser"""
from software.config.iconfiguration import IConfiguration
import configparser

class Configuration(IConfiguration):
	def __init__(self):
		self.DEVICE = 'device'
		self.GPS = 'gps'
		self.THERMO = 'thermo'
		self._config = configparser.ConfigParser()

	def read(self, filename: str):
		self._config.read(filename)

	@property
	def gps(self) -> str:
		return self._config[self.DEVICE][self.GPS]

	@property
	def thermo(self) -> str:
		return self._config[self.DEVICE][self.THERMO]
