"""Main app for openOBD"""

from openOBDShell import OpenOBDShell

from devices.GPS3Device import GPS3Device
from devices.OBDDevice import OBDDevice

from . import __version__ as VERSION


class openOBDApp():
	def __init__(self):
		self.gpsDevice = GPS3Device()
		self.obdDevice = OBDDevice()
		self.shell = openOBDShell(self.gpsDevice, self.obdDevice)

if __name__ == '__main__':
	shell = openOBDShell()
	shell.cmdloop()
