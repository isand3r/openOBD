"""A shell to demo GPS for the Nov 15 meeting"""

from cmd import Cmd
from GPS3Device import GPS3Device

class GPSDemoShell(Cmd):
	def __init__(self):
		self.intro = 'GPS Demo Shell for Nov 15 Meeting. Type help to list commands.\n'
		self.prompt = '> '
		self.file = None
		super().__init__()
		self.myGPS3Device = GPS3Device()

	def do_initializeGPSDevice(self, args):
		"""initialize the GPS device"""
		self.myGPS3Device.initialize()

	def do_printGPSStream(self, args):
		"""print the GPS stream"""
		myGPSDevice.printGPSStream()

	def do_quit(self, args):
		"""quit the shell"""
		print("Quitting")
		raise SystemExit

if __name__ == '__main__':
	shell = GPSDemoShell()
	shell.cmdloop()
