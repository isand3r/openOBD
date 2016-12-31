"""Main app for openOBD"""

import config.configuration
import shell.shell
import gps.igpsdevice
import gps.mockgpsdevice
import thermo.ithermodevice
import thermo.mockthermodevice

class App():
	CONFIG_FILENAME = TODO

	def __init__(self):
		self._config = config.configuration.Configuration
		self._gpsDevice = None
		self._thermoDevice = None
		self.configure_devices()
		self._shell = openOBDShell(self.gpsDevice, self.thermoDevice)

	def configure_devices(self):
		self._config.read(CONFIG_FILENAME)
		self._gpsDevice = TODO
		self._thermoDevice = TODO

if __name__ == '__main__':
	self._shell.cmdloop()
