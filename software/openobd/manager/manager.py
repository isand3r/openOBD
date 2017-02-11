"""Automates reading from devices"""
from thermo.ithermodevice import IThermoDevice
from gps.igpsdevice import IGPSDevice
from measure.measure import Measure
from location.location import Location
import time
import os

# only handles temperature for now
class Manager():
	def __init__(self, thermoDevice: IThermoDevice, gpsDevice: IGPSDevice):
		assert isinstance(thermoDevice, IThermoDevice)
		self._thermoDevice = thermoDevice
		self._thermoDevice.initialize()
		assert isinstance(gpsDevice, IGPSDevice)
		self._gpsDevice = gpsDevice
		self._gpsDevice.initialize()

		# lists for calculating moving averages
		self._temperatures = list()
		self._locations = list()

		self.SLEEP_TIME = 1
		self.MAX_LIST_LENGTH = 3

	def print_moving_averages(self):
			try:
				while(1):
					self.collect_readings()
					self.print_moving_average_temperature()
					self.print_moving_average_location()
					time.sleep(self.SLEEP_TIME)
			except KeyboardInterrupt:
				pass

	def print_moving_average_temperature(self):
		temperature = Measure.average_measure(self._temperatures)
		temperature_string = "TEMPERATURE | Value: {} | Units: {} | Time: {}".format(
			temperature.value, temperature.units, temperature.time)
		print(temperature_string)

	def print_moving_average_location(self):
		location = Location.average_location(self._locations)
		latitude_string = "LATITUDE | Value: {} | Units: {} | Time: {}".format(
			location.latitude.value, location.latitude.units, location.latitude.time)
		longitude_string = "LONGITUDE | Value: {} | Units: {} | Time: {}".format(
			location.longitude.value, location.longitude.units, location.longitude.time)
		altitude_string = "ALTITUDE | Value: {} | Units: {} | Time: {}".format(
			location.altitude.value, location.altitude.units, location.altitude.time)
		print(latitude_string)
		print(longitude_string)
		print(altitude_string)

	def collect_readings(self):
		"""Collect all readings and update lists"""
		self.read_temperature()
		self.read_location()

	def read_temperature(self):
		self._temperatures.append(self._thermoDevice.read_temperature())
		if (len(self._temperatures) > self.MAX_LIST_LENGTH):
			self._temperatures.pop(0)

	def read_location(self):
		self._locations.append(self._gpsDevice.read_location())
		if (len(self._locations) > self.MAX_LIST_LENGTH):
			self._locations.pop(0)
