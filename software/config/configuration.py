"""Configuration file parser for openOBD using configparser"""
from software.config.iconfiguration import IConfiguration
import configparser

class Configuration(IConfiguration):
	def __init__(self):
		self.SECTION = 'openOBD'
		self.GPS = 'gps'
		self.THERMO = 'thermo'
		self._config = configparser.ConfigParser()

	def read(self, filename):
		self._config.read(filename)

	@property
	def gps(self):
		return self._config[self.SECTION][self.GPS]

	@property
	def thermo(self):
		return self._config[self.SECTION][self.THERMO]
