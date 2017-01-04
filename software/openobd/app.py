"""Main app for openOBD"""

import sys
sys.path.append('../')

from config.iconfiguration import IConfiguration
from config.configuration import Configuration

from shell.shell import Shell

from gps.igpsdevice import IGPSDevice
from gps.mockfixedgpsdevice import MockFixedGPSDevice

from thermo.ithermodevice import IThermoDevice
from thermo.mockfixedthermodevice import MockFixedThermoDevice
from thermo.mockrisingthermodevice import MockRisingThermoDevice

class App():
	def __init__(self):
		self.CONFIG_FILENAME = 'config/config.ini'
		self._config = None
		self._gpsDevice = None
		self._thermoDevice = None
		self.read_configuration_file()
		self.configure_gps()
		self.configure_thermo()
		self.configure_shell()

	def read_configuration_file(self):
		self._config = Configuration()
		self._config.read(self.CONFIG_FILENAME)

	def configure_gps(self):
		if self._config.gps == "fixed_mock":
			self._gpsDevice = MockFixedGPSDevice()

	def configure_thermo(self):
		if self._config.thermo == 'fixed_mock':
			self._thermoDevice = MockFixedThermoDevice()
		elif self._config.thermo == 'rising_mock':
			self._thermoDevice = MockRisingThermoDevice()

	def configure_shell(self):
		self._shell = Shell(self._gpsDevice, self._thermoDevice)

	def run(self):
		self._shell.cmdloop()

if __name__ == '__main__':
	app = App()
	app.run()
