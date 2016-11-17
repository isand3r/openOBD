"""Main app for openOBD"""

from openOBDShell import OpenOBDShell



class openOBDApp():
	def __init__(self):
		self.gpsDevice = GPS3Device()
		self.obdDevice = OBDDevice()
		self.shell = openOBDShell(GPS3Device, OBDDevice)

if __name__ == '__main__':
	shell = openOBDShell()
	shell.cmdloop()
