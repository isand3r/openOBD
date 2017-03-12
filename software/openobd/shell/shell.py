from config.iconfiguration import IConfiguration
from gps.igpsdevice import IGPSDevice
from thermo.ithermodevice import IThermoDevice
from obd.iobddevice import IOBDDevice
from accelerometer.iacceldevice import IAccelDevice
from manager.manager import Manager
from devicecollection.devicecollection import DeviceCollection
from cmd import Cmd
import time
import os

class Shell(Cmd):
	"""Command line interface for openOBD"""
	def __init__(self, config: IConfiguration, gpsDevice: IGPSDevice,
		thermoDevice: IThermoDevice, accelDevice: IAccelDevice, obdDevice: IOBDDevice):
		self.intro = 'openOBD shell. Type help to list commands.\n'
		self.prompt = '> '
		self.file = None
		super().__init__()
		assert isinstance(config, IConfiguration)
		self._config = config
		assert isinstance(gpsDevice, IGPSDevice)
		self._gpsDevice = gpsDevice
		self._gpsDevice.initialize()
		assert isinstance(thermoDevice, IThermoDevice)
		self._thermoDevice = thermoDevice
		self._thermoDevice.initialize()
		assert isinstance(accelDevice, IAccelDevice)
		self._accelDevice = accelDevice
		self._accelDevice.initialize()
		assert isinstance(obdDevice, IOBDDevice)
		self._obdDevice = obdDevice
		self._obdDevice.initialize()

		self._deviceList = DeviceCollection(thermoDevice = self._thermoDevice, gpsDevice = self._gpsDevice, accelDevice = self._accelDevice, obdDevice = self._obdDevice)

	def do_manager_print_moving_averages(self, args):
		manager = Manager(self._config, self._deviceList)
		manager.print_moving_averages()

	def do_multiple_obd_read(self, args):
		"""Multiple reads once obd device, Usage: <pid request> <mode of pid>"""
		arguments = args.split()
		length = len(arguments)
		if( length != 1):
			print("Usage: multiple_obd_reading <pid request> (eg 'rpm' or 'speed')")
		else:
			message = arguments[0]
			try:	
				while(1):
					self.print_obd_data(message)
					time.sleep(1)
			except KeyboardInterrupt:
				pass

	def do_single_obd_reading(self, args):
		"""Sends obd device"""
		arguments = args.split()
		length = len(arguments)
		if( length != 1):
			print("Usage: single_obd_reading <pid request> (eg 'rpm' or 'speed')")
		else:
			message = arguments[0]
			self.print_obd_data(message)

	def print_obd_data(self, message):
		obd_data = self._obdDevice.read_current_data(message)
		obd_data_string = "OBD Data {} {} {}".format(
		round(obd_data.value,2), obd_data.units, obd_data.time.time())
		print(obd_data_string)

	def do_multiple_all_readings(self, args):
		"""Repeatedly read from all devices"""
		try:
			while(1):
				self.single_all_readings()
				time.sleep(1)
		except KeyboardInterrupt:
			pass

	def do_single_all_readings(self, args):
		"""Read from all devices once"""
		self.single_all_readings()

	def single_all_readings(self):
		self.print_temperature_reading()
		self.print_location_reading()
		self.print_accelerometer_reading()
		self.print_obd_data('rpm')
		self.print_obd_data('speed')

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
		velocity = self._accelDevice.read_acceleration()
		velocity_string = "ACCELERATION | Value: {} | Units: {} | Time: {}".format(
			velocity.value, velocity.units, velocity.time)
		print(velocity_string)
