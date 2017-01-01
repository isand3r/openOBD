"""Main app for openOBD"""

import sys
sys.path.append('../')

from software.config.iconfiguration import IConfiguration
from software.config.configuration import Configuration

from software.shell.shell import Shell

from software.thermo.ithermodevice import IThermoDevice
from software.thermo.mockfixedthermodevice import MockFixedThermoDevice
from software.thermo.mockrisingthermodevice import MockRisingThermoDevice

class App():
	def __init__(self):
		self.CONFIG_FILENAME = 'config/config.ini'
		self._config = Configuration()
		self._thermoDevice = None
		self.configure_thermo()
		self._shell = Shell(self._thermoDevice)

	def configure_thermo(self):
		self._config.read(self.CONFIG_FILENAME)
		if self._config.thermo == 'fixed_mock':
			self._thermoDevice = MockFixedThermoDevice()
		elif self._config.thermo == 'rising_mock':
			self._thermoDevice = MockRisingThermoDevice()

if __name__ == '__main__':
	app = App()
	app._shell.cmdloop()
