"""Main app for openOBD"""

import sys
sys.path.append('../')

from software.config.iconfiguration import IConfiguration
from software.config.configuration import Configuration

from software.shell.shell import Shell

from software.gps.igpsdevice import IGPSDevice
from software.gps.mockfixedgpsdevice import MockFixedGPSDevice

from software.thermo.ithermodevice import IThermoDevice
from software.thermo.mockfixedthermodevice import MockFixedThermoDevice
from software.thermo.mockrisingthermodevice import MockRisingThermoDevice

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
