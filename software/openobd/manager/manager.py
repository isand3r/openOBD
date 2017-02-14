"""Automates reading from devices"""
from thermo.ithermodevice import IThermoDevice
from gps.igpsdevice import IGPSDevice
from accelerometer.iacceldevice import IAccelDevice
from obd.iobddevice import IOBDDevice
from measure.measure import Measure
from location.location import Location
import time
import os

# only handles temperature for now
class Manager():
	def __init__(self, thermoDevice: IThermoDevice, gpsDevice: IGPSDevice,
		accelDevice: IAccelDevice, obdDevice: IOBDDevice):
		assert isinstance(thermoDevice, IThermoDevice)
		self._thermoDevice = thermoDevice
		self._thermoDevice.initialize()
		assert isinstance(gpsDevice, IGPSDevice)
		self._gpsDevice = gpsDevice
		self._gpsDevice.initialize()
		assert isinstance(accelDevice, IAccelDevice)
		self._accelDevice = accelDevice
		self._accelDevice.initialize()
		assert isinstance(obdDevice, IOBDDevice)
		self._obdDevice = obdDevice
		self._obdDevice.initialize()

		# lists for calculating moving averages
		self._temperatures = list()
		self._locations = list()
		self._accelerations = list()
		self._rpms = list()
		self._speeds = list()

		self.SLEEP_TIME = 1
		self.MAX_LIST_LENGTH = 3

	def print_moving_averages(self):
			try:
				while(1):
					self.collect_readings()
					os.system('clear')
					print("MEASURE      | VALUE | UNITS | TIME")
					self.print_moving_average_temperature()
					self.print_moving_average_acceleration()
					self.print_moving_average_location()
					self.print_moving_average_rpm()
					self.print_moving_average_speeed()
					time.sleep(self.SLEEP_TIME)
			except KeyboardInterrupt:
				pass

	def print_moving_average_temperature(self):
		temperature = Measure.average_measure(self._temperatures)
		temperature_string = "Temperature     {}  {}  {}".format(
			round(temperature.value,2), temperature.units,
			temperature.time.time())
		print(temperature_string)

	def print_moving_average_acceleration(self):
		acceleration = Measure.average_measure(self._accelerations)
		acceleration_string = "Acceleration    {}  {}  {}".format(
			round(acceleration.value,2), acceleration.units,
			acceleration.time.time())
		print(acceleration_string)

	def print_moving_average_location(self):
		location = Location.average_location(self._locations)
		latitude_string = "Latitude        {}  {}  {}".format(
			round(location.latitude.value, 4), location.latitude.units,
			location.latitude.time.time())
		longitude_string = "Longitude     {}  {}  {}".format(
			round(location.longitude.value,4), location.longitude.units,
			location.longitude.time.time())
		altitude_string = "Altitude        {}  {}  {}".format(
			round(location.altitude.value,2), location.altitude.units,
			location.altitude.time.time())
		print(latitude_string)
		print(longitude_string)
		print(altitude_string)

	def print_moving_average_rpm(self):
		rpm = Measure.average_measure(self._rpms)
		rpm_string = "RPM     {}  {}  {}".format(
			round(rpm.value,2), rpm.units,
			rpm.time.time())
		print(rpm_string)

	def print_moving_average_speed(self):
		speed = Measure.average_measure(self._speeds)
		speed_string = "Speed     {}  {}  {}".format(
			round(speed.value,2), speed.units,
			speed.time.time())
		print(speed_string)

	def collect_readings(self):
		"""Collect all readings and update lists"""
		self.read_temperature()
		self.read_acceleration()
		self.read_location()
		self.read_rpm()
		self.read_speed()

	def read_temperature(self):
		self._temperatures.append(self._thermoDevice.read_temperature())
		if (len(self._temperatures) > self.MAX_LIST_LENGTH):
			self._temperatures.pop(0)

	def read_acceleration(self):
		self._accelerations.append(self._accelDevice.read_acceleration())
		if (len(self._accelerations) > self.MAX_LIST_LENGTH):
			self._accelerations.pop(0)

	def read_location(self):
		self._locations.append(self._gpsDevice.read_location())
		if (len(self._locations) > self.MAX_LIST_LENGTH):
			self._locations.pop(0)

	def read_rpm(self):
		self._rpms.append(self._obdDevice.get_obd_info('rpm', 0x01))
		if (len(self._rpms) > self.MAX_LIST_LENGTH):
			self._rpms.pop(0)

	def read_speed(self):
		self._speeds.append(self._obdDevice.get_obd_info('speed', 0x01))
		if (len(self._speeds) > self.MAX_LIST_LENGTH):
			self._speeds.pop(0)
