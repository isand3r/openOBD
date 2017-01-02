"""Command line interface for openOBD"""

from software.thermo.ithermodevice import IThermoDevice
from cmd import Cmd
import time
import os

class Shell(Cmd):
	def __init__(self, thermoDevice: IThermoDevice):
		self.intro = 'openOBD shell. Type help to list commands.\n'
		self.prompt = '> '
		self.file = None
		super().__init__()
		assert isinstance(thermoDevice, IThermoDevice)
		self._thermoDevice = thermoDevice
		self._thermoDevice.initialize()

	def do_multiple_readings(self, args):
		"""Repeatedly read from the device"""
		try:
			while(1):
				self.print_temperature_reading()
				time.sleep(1)
		except KeyboardInterrupt:
			pass

	def do_single_reading(self, args):
		"""Read from the device once"""
		self.print_temperature_reading()

	def do_quit(self, args):
		"""Quit the shell"""
		print("Quitting")
		raise SystemExit

	def print_temperature_reading(self):
		"""Print a new temperature reading"""
		temperature = self._thermoDevice.read_temperature()
		temperature_string = "Value: {} | Units: {} | Time: {}".format(
			temperature.value, temperature.units, temperature.time)
		print(temperature_string)
