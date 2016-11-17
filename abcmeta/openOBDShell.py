"""Command line interface for openOBD"""

from cmd import Cmd
import time
import os

from . import __version__ as VERSION

class openOBDShell(Cmd):
	def __init__(self, gpsDevice, obdDevice):
		self.intro = 'openOBD shell. Type help to list commands.\n'
		self.prompt = '> '
		self.file = None
		super().__init__()
		self.gpsDevice = gpsDevice
		self.obdDevice = obdDevice

	def do_initDevices(self, args):
		"""initialize the GPS device"""
		self.gpsDevice.initialize()
		self.obdDevice.initialize()

	def do_readgps(self, args):
		"""print the GPS stream"""
		self.gpsDevice.printGPSStream()

	def do_listen(self, args):
		"""listen to all devices constantly"""
		try:
			while(1):
				self.gpsDevice.printGPSStream()
				self.obdDevice.printOBDStream()
				time.sleep(1)
		except KeyboardInterrupt:
			pass

	def do_version(self, args):
		"""Prints the Version of Build"""
		print (VERSION)

	def do_quit(self, args):
		"""quit the shell"""
		print("Quitting")
		raise SystemExit
