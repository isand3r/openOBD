"""Configuration file parser for openOBD using configparser"""

import configparser

class Configuration(config.configuration.IConfiguration):
	SECTION = 'openOBD'
	GPS = 'gps'
	THERMO = 'thermo'

	def __init__(self):
		self._config = configparser.ConfigParser()

	def read(self, filename):
		self._config.read(filename)

	@property
	def gps(self):
		return self._config[SECTION][GPS]

	@property
	def thermo(self):
		return self._config[SECTION][THERMO]
