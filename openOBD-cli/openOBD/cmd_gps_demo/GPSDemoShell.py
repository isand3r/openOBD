"""A shell to demo GPS for the Nov 15 meeting"""

from cmd import Cmd
from GPS3Device import GPS3Device
import time
import os
from MPUDevice import MPUDevice

class openOBDShell(Cmd):
	def __init__(self):
		self.intro = 'GPS Demo Shell for Nov 15 Meeting. Type help to list commands.\n'
		self.prompt = '> '
		self.file = None
		super().__init__()
		self.myGPS3Device = GPS3Device()
		self.myMPUDevice = MPUDevice()

	def do_initDevices(self, args):
		"""initialize the GPS device"""
		self.myGPS3Device.initialize()
		self.myMPUDevice.initialize()

	def do_readgps(self, args):
		"""print the GPS stream"""
		self.myGPS3Device.printGPSStream()

	def do_readtemp(self, args):
		"""print the GPS stream"""
		self.myMPUDevice.printTempStream()

	def do_readaccel(self, args):
		"""print the GPS stream"""
		self.myMPUDevice.printAccelStream()

	def do_readgyro(self, args):
		"""print the GPS stream"""
		self.myMPUDevice.printGyroStream()

	def do_listen(self, args):
		try:
			while(1):
				self.myMPUDevice.printGyroStream()
				self.myMPUDevice.printAccelStream()
				self.myMPUDevice.printTempStream()
				self.myGPS3Device.printGPSStream()
				time.sleep(1)
				os.system('clear')
		except KeyboardInterrupt:
			pass

	def do_quit(self, args):
		"""quit the shell"""
		print("Quitting")
		raise SystemExit

if __name__ == '__main__':
	shell = openOBDShell()
	shell.cmdloop()
