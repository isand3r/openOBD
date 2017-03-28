from config.iconfiguration import IConfiguration
from location.location import Location
from accumulator.accumulator import Accumulator #TODO should instead depend on IAccumulator
from devicecollection.idevicecollection import IDeviceCollection
from measure.measure import Measure
from location.location import Location
from udp.udp import UDP
from datetime import datetime, timezone

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
		self.RPM_INTERVAL = self._config.rpm_interval
		self.SPEED_INTERVAL = self._config.speed_interval
		self.PRINT_INTERVAL = self._config.manager_print_interval
		self.MOVING_AVERAGE_ITEMS = self._config.manager_moving_average_items

		self.workerlist = list()

		# lists for calculating moving averages
		self._temperatures = Accumulator("temperature", self.MOVING_AVERAGE_ITEMS)
		self._longtitudes = Accumulator("longtitudes", self.MOVING_AVERAGE_ITEMS)
		self._latitudes = Accumulator("latitudes", self.MOVING_AVERAGE_ITEMS)
		self._altitudes = Accumulator("altitudes", self.MOVING_AVERAGE_ITEMS)
		self._accelerations = Accumulator("acceleration", self.MOVING_AVERAGE_ITEMS)
		self._rpms = Accumulator("rpm", self.MOVING_AVERAGE_ITEMS)
		self._speeds = Accumulator("speed", self.MOVING_AVERAGE_ITEMS)

		self._udp = UDP('staging-tcu.moj.io', 9001)
		self._udp.connect()
		
		self.start_workers()

	def stop_workers(self):
		for each in self.workerlist:
			each.join()

	def print_moving_averages(self):
		while(True):

			os.system('clear')
			print("MEASURE      | VALUE | UNITS | TIME")
			for key in self._deviceCollection.get_all_devices():
				if(key == DeviceConstants.DEVICE_THERMO):
					self.print_moving_average_temperature()
				elif(key == DeviceConstants.DEVICE_GPS):
					self.print_moving_average_location()
				elif(key == DeviceConstants.DEVICE_ACCEL):
					self.print_moving_average_acceleration()
				elif(key == DeviceConstants.DEVICE_OBD):
					self.print_moving_average_rpm()
					self.print_moving_average_speed()
			time.sleep(self.PRINT_INTERVAL)
				

	def print_moving_average_temperature(self):
		temperature = self._temperatures.mean()
		temperature_string = "Temperature     {}  {}  {}".format(
			round(temperature.value,2), temperature.units,
			temperature.time.time())
		print(temperature_string)

	def print_moving_average_acceleration(self):
		acceleration = self._accelerations.mean()
		acceleration_string = "Acceleration    {}  {}  {}".format(
			round(acceleration.value,2), acceleration.units,
			acceleration.time.time())
		print(acceleration_string)

	def print_moving_average_location(self):
		longitude = self._longtitudes.mean()
		latitude = self._latitudes.mean()
		altitude = self._altitudes.mean()
		latitude_string = "Latitude        {}  {}  {}".format(
			round(latitude.value, 4), latitude.units,
			latitude.time.time())
		longitude_string = "Longitude     {}  {}  {}".format(
			round(longitude.value,4), longitude.units,
			longitude.time.time())
		altitude_string = "Altitude        {}  {}  {}".format(
			round(altitude.value,2), altitude.units,
			altitude.time.time())
		print(latitude_string)
		print(longitude_string)
		print(altitude_string)

	def print_moving_average_rpm(self):
		rpm = self._rpms.mean()
		rpm_string = "RPM     {}  {}  {}".format(
			round(rpm.value,2), rpm.units,
			rpm.time.time())
		print(rpm_string)

	def print_moving_average_speed(self):
		speed = self._speeds.mean()
		speed_string = "Speed     {}  {}  {}".format(
			round(speed.value,2), speed.units,
			speed.time.time())
		print(speed_string)

	def start_workers(self):

		udp_thread = threading.Thread(name = "UDP", target = self.udp_worker, daemon = True)
		self.workerlist.append(udp_thread)

		for key in self._deviceCollection.get_all_devices():
			if(key == DeviceConstants.DEVICE_THERMO):
				thermo_thread = threading.Thread(name = DeviceConstants.DEVICE_THERMO, target=self.thermo_worker, daemon=True)
				self.workerlist.append(thermo_thread)

			elif(key == DeviceConstants.DEVICE_ACCEL):
				accel_thread = threading.Thread(name = DeviceConstants.DEVICE_ACCEL, target=self.accel_worker, daemon=True)
				self.workerlist.append(accel_thread)

			elif(key == DeviceConstants.DEVICE_GPS):
				gps_thread = threading.Thread(name = DeviceConstants.DEVICE_GPS, target=self.gps_worker, daemon=True)
				self.workerlist.append(gps_thread)

			elif(key == DeviceConstants.DEVICE_OBD):
				rpm_thread = threading.Thread(name = MeasureConstants.RPM, target=self.rpm_worker, daemon=True)
				self.workerlist.append(rpm_thread)
				speed_thread = threading.Thread(name = MeasureConstants.SPEED, target=self.speed_worker, daemon=True)
				self.workerlist.append(speed_thread)

		for each in self.workerlist:
			each.start()

	def thermo_worker(self):
		while(True):
			self.read_temperature()
			time.sleep(self.THERMO_INTERVAL)

	def accel_worker(self):
		while(True):
			self.read_acceleration()
			time.sleep(self.ACCEL_INTERVAL)

	def gps_worker(self):
		while(True):
			self.read_location()
			time.sleep(self.GPS_INTERVAL)

	def rpm_worker(self):
		while(True):
			self.read_rpm()
			time.sleep(self.RPM_INTERVAL)

	def speed_worker(self):
		while(True):
			self.read_speed()
			time.sleep(self.SPEED_INTERVAL)

	def udp_worker(self):
		while(True):

			self._udp.update_info('D', datetime.now(timezone.utc).strftime("%Y%m%d"))
			self._udp.update_info('T', datetime.now(timezone.utc).strftime("%H%M%S"))
			self._udp.update_info('AX', 1.2)
			self._udp.update_info('AY', 1.2)
			self._udp.update_info('AZ', 1.2)
			self._udp.update_info('LT', 49.27884)
			self._udp.update_info('LN', -123.12586)
			self._udp.update_info('AL', 64)
			self._udp.update_info('SP', 0)
			self._udp.update_info('RP', 0)
			self._udp.update_info('SP', 0)
			self._udp.update_info('BV', 12)
			self._udp.update_info('IG', 1)

			self._udp.send(6011)
			time.sleep(2)

	def read_temperature(self):
		self._temperatures.push(self._deviceCollection.read_current_data(DeviceConstants.DEVICE_THERMO))

	def read_acceleration(self):
		self._accelerations.push(self._deviceCollection.read_current_data(DeviceConstants.DEVICE_ACCEL))

	def read_location(self):
		location = self._deviceCollection.read_current_data(DeviceConstants.DEVICE_GPS)
		self._latitudes.push(location.latitude)
		self._longtitudes.push(location.longitude)
		self._altitudes.push(location.altitude)


	def read_rpm(self):
		self._rpms.push(self._deviceCollection.read_current_data(MeasureConstants.RPM))

	def read_speed(self):
		self._speeds.push(self._deviceCollection.read_current_data(MeasureConstants.SPEED))



