from config.iconfiguration import IConfiguration
from location.location import Location
from accumulator.accumulator import Accumulator
from devicecollection.idevicecollection import IDeviceCollection
from measure.measure import Measure
from location.location import Location
import constants.deviceconstants as DeviceConstants
import constants.measureconstants as MeasureConstants
import threading
import time
import os

class Manager():	
	"""Automates reading from devices"""
	
	def __init__(self, config: IConfiguration, deviceCollection: IDeviceCollection):
		assert isinstance(config, IConfiguration)
		self._config = config
		assert isinstance(deviceCollection, IDeviceCollection)
		self._deviceCollection = deviceCollection
		self._deviceCollection.init_devices()

		self.GPS_INTERVAL = self._config.gps_interval
		self.THERMO_INTERVAL = self._config.thermo_interval
		self.ACCEL_INTERVAL = self._config.accel_interval
		self.VOLT_INTERVAL = self._config.volt_interval
		self.BARO_INTERVAL = self._config.baro_interval
		self.RPM_INTERVAL = self._config.rpm_interval
		self.SPEED_INTERVAL = self._config.speed_interval
		self.PRINT_INTERVAL = self._config.manager_print_interval
		self.MOVING_AVERAGE_ITEMS = self._config.manager_moving_average_items

		self._longtitudes = Accumulator("Longitude", self.MOVING_AVERAGE_ITEMS)
		self._latitudes = Accumulator("Latitude", self.MOVING_AVERAGE_ITEMS)
		self._altitudes = Accumulator("Altitude", self.MOVING_AVERAGE_ITEMS)
		self._temperatures = Accumulator("Temperature", self.MOVING_AVERAGE_ITEMS)
		self._accelerations = Accumulator("Acceleration", self.MOVING_AVERAGE_ITEMS)
		self._voltages = Accumulator("Voltage", self.MOVING_AVERAGE_ITEMS)
		self._pressures = Accumulator("Pressure", self.MOVING_AVERAGE_ITEMS)
		self._rpms = Accumulator("RPM", self.MOVING_AVERAGE_ITEMS)
		self._speeds = Accumulator("Speed", self.MOVING_AVERAGE_ITEMS)

		self.DEFAULT_ROUNDING_DIGITS = 2
		self.LATITUDE_ROUNDING_DIGITS = 4

		self._workerList = list()
		self.create_workers()
		self.start_workers()

	def print_all_accumulator_means(self):
		while(True):
			os.system('clear')
			print("MEASURE | VALUE | UNITS | TIME")
			self.print_accumulator_mean(self._longtitudes)
			self.print_accumulator_mean(self._latitudes, self.LATITUDE_ROUNDING_DIGITS)
			self.print_accumulator_mean(self._altitudes)
			self.print_accumulator_mean(self._temperatures)
			self.print_accumulator_mean(self._accelerations)
			self.print_accumulator_mean(self._voltages)
			self.print_accumulator_mean(self._pressures)
			self.print_accumulator_mean(self._rpms)
			self.print_accumulator_mean(self._speeds)
			time.sleep(self.PRINT_INTERVAL)

	def print_accumulator_mean(self, accumulator, roundDigits = None):
		if (roundDigits == None):
			roundDigits = self.DEFAULT_ROUNDING_DIGITS
		mean = accumulator.mean()
		if (mean != None):
			string = accumulator.name + " {} {} {}".format(
				round(mean.value, roundDigits), mean.units, mean.time.time())
			print(string)

	def create_workers(self):
		self.create_gps_worker_thread()
		self.create_worker_thread(self._temperatures, DeviceConstants.DEVICE_THERMO, self.THERMO_INTERVAL)
		self.create_worker_thread(self._accelerations, DeviceConstants.DEVICE_ACCEL, self.ACCEL_INTERVAL)
		self.create_worker_thread(self._voltages, DeviceConstants.DEVICE_VOLT, self.VOLT_INTERVAL)
		self.create_worker_thread(self._pressures, DeviceConstants.DEVICE_BARO, self.BARO_INTERVAL)
		self.create_worker_thread(self._rpms, MeasureConstants.RPM, self.RPM_INTERVAL)
		self.create_worker_thread(self._speeds, MeasureConstants.SPEED, self.SPEED_INTERVAL)

	def create_worker_thread(self, accumulator, measureString, interval):
		thread = threading.Thread(name = measureString, target=self.measure_worker,
			args=(accumulator, measureString, interval), daemon=True)
		self._workerList.append(thread)

	def measure_worker(self, accumulator, measureString, interval):
		while(True):
			self.read_measure(accumulator, measureString)
			time.sleep(interval)

	def read_measure(self, accumulator, measureString):
		accumulator.push(self._deviceCollection.read_current_data(measureString))

	def create_gps_worker_thread(self):
		# gps is a special case because location consists of three measures
		gps_thread = threading.Thread(name = DeviceConstants.DEVICE_GPS, target=self.location_worker, daemon=True)
		self._workerList.append(gps_thread)

	def location_worker(self):
		while(True):
			self.read_location()
			time.sleep(self.GPS_INTERVAL)

	def read_location(self):
		location = self._deviceCollection.read_current_data(DeviceConstants.DEVICE_GPS)
		self._latitudes.push(location.latitude)
		self._longtitudes.push(location.longitude)
		self._altitudes.push(location.altitude)

	def start_workers(self):
		for each in self._workerList:
			each.start()
