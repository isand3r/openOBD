"""Main app for openOBD"""

from .shell.Shell import Shell

from .gps.GPS3Device import GPS3Device
from .thermo.MPUThermoDevice import MPUThermoDevice

from . import __version__ as VERSION

class App():
	def __init__(self):
		self.gpsDevice = GPS3Device()
		self.thermoDevice = MPUThermoDevice()
		self.shell = openOBDShell(self.gpsDevice, self.thermoDevice)

if __name__ == '__main__':
	self.shell.cmdloop()
