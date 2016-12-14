"""Command line interface for openOBD"""

from cmd import Cmd
import time
import os

class Shell(Cmd):
	def __init__(self, gpsDevice, thermoDevice):
		self.intro = 'openOBD shell. Type help to list commands.\n'
		self.prompt = '> '
		self.file = None
		super().__init__()
		self.gpsDevice = gpsDevice
		self.thermoDevice = thermoDevice

	def do_initDevices(self, args):
		"""initialize the devices"""
		self.gpsDevice.initialize()
		self.thermoDevice.initialize()

	def do_readgps(self, args):
		"""print the GPS stream"""
		print("openOBDShell do_readgps not implemented")

	def do_listen(self, args):
		"""listen to all devices constantly"""
		try:
			while(1):
				print("openOBDShell do_listen not implemented")
				time.sleep(1)
		except KeyboardInterrupt:
			pass

	def do_quit(self, args):
		"""quit the shell"""
		print("Quitting")
		raise SystemExit
