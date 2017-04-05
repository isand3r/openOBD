from config.iconfiguration import IConfiguration
from location.location import Location
from accumulator.accumulator import Accumulator #TODO should instead depend on IAccumulator
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

		self.THERMO_INTERVAL = self._config.thermo_interval
		self.ACCEL_INTERVAL = self._config.accel_interval
		self.GPS_INTERVAL = self._config.gps_interval
		self.VOLT_INTERVAL = self._config.volt_interval
		self.BARO_INTERVAL = self._config.baro_interval
		self.RPM_INTERVAL = self._config.rpm_interval
		self.SPEED_INTERVAL = self._config.speed_interval
		self.PRINT_INTERVAL = self._config.manager_print_interval
		self.MOVING_AVERAGE_ITEMS = self._config.manager_moving_average_items

		# lists for calculating moving averages
		self._temperatures = Accumulator("Temperature", self.MOVING_AVERAGE_ITEMS)
		self._longtitudes = Accumulator("Longitude", self.MOVING_AVERAGE_ITEMS)
		self._latitudes = Accumulator("Latitude", self.MOVING_AVERAGE_ITEMS)
		self._altitudes = Accumulator("Altitude", self.MOVING_AVERAGE_ITEMS)
		self._accelerations = Accumulator("Acceleration", self.MOVING_AVERAGE_ITEMS)
		self._voltages = Accumulator("Voltage", self.MOVING_AVERAGE_ITEMS)
		self._pressures = Accumulator("Pressure", self.MOVING_AVERAGE_ITEMS)
		self._rpms = Accumulator("RPM", self.MOVING_AVERAGE_ITEMS)
		self._speeds = Accumulator("Speed", self.MOVING_AVERAGE_ITEMS)

		self._workerList = list()
		self.start_workers()

	def print_moving_averages(self):
		while(True):
			os.system('clear')
			print("MEASURE | VALUE | UNITS | TIME")
			self.print_accumulator_mean(self._longtitudes, 2)
			self.print_accumulator_mean(self._latitudes, 4)
			self.print_accumulator_mean(self._altitudes, 2)
			self.print_accumulator_mean(self._temperatures, 2)
			self.print_accumulator_mean(self._accelerations, 2)
			self.print_accumulator_mean(self._voltages, 2)
			self.print_accumulator_mean(self._pressures, 2)
			self.print_accumulator_mean(self._rpms, 2)
			self.print_accumulator_mean(self._speeds, 2)
			time.sleep(self.PRINT_INTERVAL)

	def print_accumulator_mean(self, accumulator, roundDigits):
		mean = accumulator.mean()
		if (mean != None):
			string = accumulator.name + " {} {} {}".format(
				round(mean.value, roundDigits), mean.units, mean.time.time())
			print(string)

	def start_workers(self):
		thermo_thread = threading.Thread(name = DeviceConstants.DEVICE_THERMO, target=self.worker,
			args=(self.read_temperature, self.THERMO_INTERVAL), daemon=True)
		self._workerList.append(thermo_thread)

		accel_thread = threading.Thread(name = DeviceConstants.DEVICE_ACCEL, target=self.worker,
			args=(self.read_acceleration, self.ACCEL_INTERVAL), daemon=True)
		self._workerList.append(accel_thread)

		gps_thread = threading.Thread(name = DeviceConstants.DEVICE_GPS, target=self.worker,
			args=(self.read_location, self.GPS_INTERVAL), daemon=True)
		self._workerList.append(gps_thread)

		volt_thread = threading.Thread(name = DeviceConstants.DEVICE_VOLT, target=self.worker,
			args=(self.read_voltage, self.VOLT_INTERVAL), daemon=True)
		self._workerList.append(volt_thread)

		baro_thread = threading.Thread(name = DeviceConstants.DEVICE_BARO, target=self.worker,
			args=(self.read_pressure, self.BARO_INTERVAL), daemon=True)
		self._workerList.append(baro_thread)

		rpm_thread = threading.Thread(name = MeasureConstants.RPM, target=self.worker,
			args=(self.read_rpm, self.RPM_INTERVAL), daemon=True)
		self._workerList.append(rpm_thread)

		speed_thread = threading.Thread(name = MeasureConstants.SPEED, target=self.worker,
			args=(self.read_speed, self.SPEED_INTERVAL), daemon=True)
		self._workerList.append(speed_thread)

		for each in self._workerList:
			each.start()

	def worker(self, read_method, interval):
		while(True):
			read_method()
			time.sleep(interval)

	def read_temperature(self):
		self._temperatures.push(self._deviceCollection.read_current_data(DeviceConstants.DEVICE_THERMO))

	def read_acceleration(self):
		self._accelerations.push(self._deviceCollection.read_current_data(DeviceConstants.DEVICE_ACCEL))

	def read_location(self):
		location = self._deviceCollection.read_current_data(DeviceConstants.DEVICE_GPS)
		self._latitudes.push(location.latitude)
		self._longtitudes.push(location.longitude)
		self._altitudes.push(location.altitude)

	def read_voltage(self):
		self._voltages.push(self._deviceCollection.read_current_data(DeviceConstants.DEVICE_VOLT))

	def read_pressure(self):
		self._pressures.push(self._deviceCollection.read_current_data(DeviceConstants.DEVICE_BARO))

	def read_rpm(self):
		self._rpms.push(self._deviceCollection.read_current_data(MeasureConstants.RPM))

	def read_speed(self):
		self._speeds.push(self._deviceCollection.read_current_data(MeasureConstants.SPEED))
