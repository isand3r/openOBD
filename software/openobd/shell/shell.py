"""Command line interface for openOBD"""
from api.api import Api
from gps.igpsdevice import IGPSDevice
from thermo.ithermodevice import IThermoDevice
from obd.iobddevice import IOBDDevice
from accelerometer.iacceldevice import IAccelDevice
from manager.manager import Manager
from cmd import Cmd
import time
import os

class Shell(Cmd):
	def __init__(self, gpsDevice: IGPSDevice, thermoDevice: IThermoDevice, accelDevice: IAccelDevice, api: Api, obdDevice: IOBDDevice):
		self.intro = 'openOBD shell. Type help to list commands.\n'
		self.prompt = '> '
		self.file = None
		super().__init__()
		assert isinstance(gpsDevice, IGPSDevice)
		self._gpsDevice = gpsDevice
		self._gpsDevice.initialize()
		assert isinstance(thermoDevice, IThermoDevice)
		self._thermoDevice = thermoDevice
		self._thermoDevice.initialize()
		assert isinstance(accelDevice, IAccelDevice)
		self._accelDevice = accelDevice
		self._accelDevice.initialize()
		assert isinstance(api, Api)
		self._api = api
		self._api.get_auth()
		assert isinstance(obdDevice, IOBDDevice)
		self._obdDevice = obdDevice
		self._obdDevice.initialize()
		self._manager = Manager(thermoDevice, gpsDevice, accelDevice, obdDevice)

	def do_manager_print_moving_averages(self, args):
		self._manager.print_moving_averages()

	def do_api_call_test(self, args):
		"""Calls Moj.io API and returns current user"""
		self._api.get_me()

	def do_single_obd_read(self, args):
		"""Single read on obd device"""
		self._obdDevice.listen_obd()

	def do_multiple_obd_read(self, args):
		"""Multiple reads once obd device, Usage: <pid request> <mode of pid>"""
		arguements = args.split()
		length = len(arguements)
		if( length < 2):
			print("Usage: list:<pid request> <mode of pid>")
		else:
			try:	
				while(1):
					for each in range(length-1):
						self._obdDevice.get_obd_info(arguements[each], arguements[length-1])
					time.sleep(1)
			except KeyboardInterrupt:
				pass

	def do_obd_send_test(self, args):
		"""Sends obd device"""
		self._obdDevice.get_obd_info('speed', 0x01)

	def do_multiple_all_readings(self, args):
		"""Repeatedly read from all devices"""
		try:
			while(1):
				self.print_temperature_reading()
				self.print_location_reading()
				self.print_accelerometer_reading()
				self.print_obd_reading()
				time.sleep(1)
		except KeyboardInterrupt:
			pass

	def do_single_all_readings(self, args):
		"""Read from all devices once"""
		self.print_temperature_reading()
		self.print_location_reading()
		self.print_accelerometer_reading
		self.print_obd_reading()

	def do_multiple_temperature_readings(self, args):
		"""Repeatedly read from the device"""
		try:
			while(1):
				self.print_temperature_reading()
				time.sleep(1)
		except KeyboardInterrupt:
			pass

	def do_single_temperature_reading(self, args):
		"""Read from the device once"""
		self.print_temperature_reading()

	def do_multiple_location_readings(self, args):
		"""Repeatedly read from the device"""
		try:
			while(1):
				self.print_location_reading()
				time.sleep(1)
		except KeyboardInterrupt:
			pass

	def do_single_location_reading(self, args):
		"""Read from the device once"""
		self.print_location_reading()

	def do_quit(self, args):
		"""Quit the shell"""
		print("Quitting")
		raise SystemExit

	def print_obd_reading(self):
		self._obdDevice.listen_obd()

	def print_temperature_reading(self):
		"""Print a new temperature reading"""
		temperature = self._thermoDevice.read_temperature()
		temperature_string = "TEMPERATURE | Value: {} | Units: {} | Time: {}".format(
			temperature.value, temperature.units, temperature.time)
		print(temperature_string)

	def print_location_reading(self):
		"""Print a new location reading"""
		location = self._gpsDevice.read_location()
		latitude_string = "LATITUDE | Value: {} | Units: {} | Time: {}".format(
			location.latitude.value, location.latitude.units, location.latitude.time)
		longitude_string = "LONGITUDE | Value: {} | Units: {} | Time: {}".format(
			location.longitude.value, location.longitude.units, location.longitude.time)
		altitude_string = "ALTITUDE | Value: {} | Units: {} | Time: {}".format(
			location.altitude.value, location.altitude.units, location.altitude.time)
		print(latitude_string)
		print(longitude_string)
		print(altitude_string)

	def print_accelerometer_reading(self):
		"""Print a new temperature reading"""
		velocity = self._accelDevice.read_accelerometer()
		velocity_string = "ACCELERATION | Value: {} | Units: {} | Time: {}".format(
			velocity.value, velocity.units, velocity.time)
		print(velocity_string)
