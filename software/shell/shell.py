"""Command line interface for openOBD"""

from cmd import Cmd
import time
import os

class Shell(Cmd):
	def __init__(self, thermoDevice):
		self.intro = 'openOBD shell. Type help to list commands.\n'
		self.prompt = '> '
		self.file = None
		super().__init__()
		self._thermoDevice = thermoDevice

	def do_initDevices(self, args):
		"""initialize the devices"""
		self._thermoDevice.initialize()

	def do_listen(self, args):
		"""listen to all devices constantly"""
		try:
			while(1):
				temperature = self._thermoDevice.read_temperature()
				print(temperature.value)
				time.sleep(1)
		except KeyboardInterrupt:
			pass

	def do_quit(self, args):
		"""quit the shell"""
		print("Quitting")
		raise SystemExit
