"""Automates reading from devices"""
from thermo.ithermodevice import IThermoDevice
from measure.measure import Measure
import time
import os

# only handles temperature for now
class Manager():
	def __init__(self, thermoDevice: IThermoDevice):
		assert isinstance(thermoDevice, IThermoDevice)
		self._thermoDevice = thermoDevice
		self._thermoDevice.initialize()

		# lists for calculating moving averages
		self._temperatures = list()

		self.SLEEP_TIME = 1
		self.MAX_LIST_LENGTH = 3

	def print_moving_averages(self):
			try:
				while(1):
					self.collect_readings()
					moving_average = self.moving_average_temperature(self._temperatures)
					print(moving_average.value)
					time.sleep(self.SLEEP_TIME)
			except KeyboardInterrupt:
				pass

	def collect_readings(self):
		"""Collect all readings and update lists"""
		self.read_temperature()

	def read_temperature(self):
		self._temperatures.append(self._thermoDevice.read_temperature())
		if (len(self._temperatures) > self.MAX_LIST_LENGTH):
			self._temperatures.pop(0)

	def moving_average_temperature(self, list) -> Measure:
		sum_value = 0
		count = 0
		for temperature in list:
			sum_value += temperature.value
			count += 1
		average_value = sum_value / count
		# uses time from oldest reading
		return Measure(average_value, list[0].units, list[0].time)
