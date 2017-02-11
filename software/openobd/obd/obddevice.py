from obd.iobddevice import IOBDDevice
from measure.measure import Measure
import can
import os
import datetime

class OBDDevice(IOBDDevice):
	"""OBD Device that can send PIDs and read from the CAN bus"""

	def __init__(self):
		self._ready = False
		self.bus = None
		self.canlistener = None

	def initialize(self):
		os.system('sudo ip link set can0 type can bitrate 125000 triple-sampling on')
		os.system('sudo ifconfig can0 up')
		can.rc['interface'] = 'socketcan_native'
		self.bus = can.interface.Bus('can0')
		self._ready = True
	
	@property
	def ready(self) -> bool:
		return self._ready

	def init_pids(self, mode):
		PID_dict = {}
		PID_dict['pidsupport'] = [mode, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]
		PID_dict['monitor_status'] = [mode, 0x01, 0x00, 0x00, 0x00, 0x00, 0x00]
		PID_dict['freeze_dtc'] = [mode, 0x02, 0x00, 0x00, 0x00, 0x00, 0x00]
		PID_dict['fuel_system_status'] = [mode, 0x03, 0x00, 0x00, 0x00, 0x00, 0x00]
		PID_dict['engine_load'] = [mode, 0x04, 0x00, 0x00, 0x00, 0x00, 0x00]
		PID_dict['coolant_temp'] = [mode, 0x05, 0x00, 0x00, 0x00, 0x00, 0x00]
		PID_dict['sterm_fuel1'] = [mode, 0x06, 0x00, 0x00, 0x00, 0x00, 0x00]
		PID_dict['lterm_fuel1'] = [mode, 0x07, 0x00, 0x00, 0x00, 0x00, 0x00]
		PID_dict['sterm_fuel2'] = [mode, 0x08, 0x00, 0x00, 0x00, 0x00, 0x00]
		PID_dict['lterm_fuel2'] = [mode, 0x09, 0x00, 0x00, 0x00, 0x00, 0x00]
		PID_dict['fuel_pressure'] = [mode, 0x0A, 0x00, 0x00, 0x00, 0x00, 0x00]
		PID_dict['intake_manifold_pressure'] = [mode, 0x0B, 0x00, 0x00, 0x00, 0x00, 0x00]
		PID_dict['rpm'] = [mode, 0x0C, 0x00, 0x00, 0x00, 0x00, 0x00]
		PID_dict['speed'] = [mode, 0x0D, 0x00, 0x00, 0x00, 0x00, 0x00]
		PID_dict['timing_advance'] = [mode, 0x0E, 0x00, 0x00, 0x00, 0x00, 0x00]
		PID_dict['intake_air_temp'] = [mode, 0x0F, 0x00, 0x00, 0x00, 0x00, 0x00]
		PID_dict['MAF_flow'] = [mode, 0x10, 0x00, 0x00, 0x00, 0x00, 0x00]
		PID_dict['throttle_position'] = [mode, 0x11, 0x00, 0x00, 0x00, 0x00, 0x00]
		PID_dict['secondary_air_status'] = [mode, 0x12, 0x00, 0x00, 0x00, 0x00, 0x00]
		PID_dict['oxygen_present'] = [mode, 0x13, 0x00, 0x00, 0x00, 0x00, 0x00]
		PID_dict['oxy_b1_s1'] = [mode, 0x14, 0x00, 0x00, 0x00, 0x00, 0x00]
		PID_dict['oxy_b1_s2'] = [mode, 0x15, 0x00, 0x00, 0x00, 0x00, 0x00]
		PID_dict['oxy_b1_s3'] = [mode, 0x16, 0x00, 0x00, 0x00, 0x00, 0x00]
		PID_dict['oxy_b1_s4'] = [mode, 0x17, 0x00, 0x00, 0x00, 0x00, 0x00]
		PID_dict['oxy_b2_s1'] = [mode, 0x18, 0x00, 0x00, 0x00, 0x00, 0x00]
		PID_dict['oxy_b2_s2'] = [mode, 0x019, 0x00, 0x00, 0x00, 0x00, 0x00]
		PID_dict['oxy_b2_s3'] = [mode, 0x01A, 0x00, 0x00, 0x00, 0x00, 0x00]
		PID_dict['oxy_b2_s4'] = [mode, 0x01B, 0x00, 0x00, 0x00, 0x00, 0x00]
		PID_dict['obd_standard_id'] = [mode, 0x1C, 0x00, 0x00, 0x00, 0x00, 0x00]
		PID_dict['oxygen_sensor_present'] = [mode, 0x1D, 0x00, 0x00, 0x00, 0x00, 0x00]
		PID_dict['aux_input_status'] = [mode, 0x1E, 0x00, 0x00, 0x00, 0x00, 0x00]
		PID_dict['engine_run_time'] = [mode, 0x1F, 0x00, 0x00, 0x00, 0x00, 0x00]
		PID_dict['pids_suport_21_40'] = [mode, 0x20, 0x00, 0x00, 0x00, 0x00, 0x00]
		PID_dict['distance_traveled_MIL'] = [mode, 0x21, 0x00, 0x00, 0x00, 0x00, 0x00]
		PID_dict['fuel_rail_pressure'] = [mode, 0x22, 0x00, 0x00, 0x00, 0x00, 0x00]
		PID_dict['fuel_rail_pressure_diesel'] = [mode, 0x23, 0x00, 0x00, 0x00, 0x00, 0x00]
		PID_dict['VO2S1_WR_lambda'] = [mode, 0x24, 0x00, 0x00, 0x00, 0x00, 0x00]
		PID_dict['VO2S2_WR_lambda'] = [mode, 0x25, 0x00, 0x00, 0x00, 0x00, 0x00]
		PID_dict['VO2S3_WR_lambda'] = [mode, 0x26, 0x00, 0x00, 0x00, 0x00, 0x00]
		PID_dict['VO2S4_WR_lambda'] = [mode, 0x27, 0x00, 0x00, 0x00, 0x00, 0x00]
		PID_dict['VO2S5_WR_lambda'] = [mode, 0x28, 0x00, 0x00, 0x00, 0x00, 0x00]
		PID_dict['VO2S6_WR_lambda'] = [mode, 0x29, 0x00, 0x00, 0x00, 0x00, 0x00]
		PID_dict['VO2S7_WR_lambda'] = [mode, 0x2A, 0x00, 0x00, 0x00, 0x00, 0x00]
		PID_dict['VO2S8_WR_lambda'] = [mode, 0x2B, 0x00, 0x00, 0x00, 0x00, 0x00]
		PID_dict['ERG'] = [mode, 0x2C, 0x00, 0x00, 0x00, 0x00, 0x00]
		PID_dict['ERG_error'] = [mode, 0x2D, 0x00, 0x00, 0x00, 0x00, 0x00]
		PID_dict['evaporative_purge'] = [mode, 0x2E, 0x00, 0x00, 0x00, 0x00, 0x00]
		PID_dict['fuel_level'] = [mode, 0x2F, 0x00, 0x00, 0x00, 0x00, 0x00]
		PID_dict['warm_up_attemps_since_clear'] = [mode, 0x30, 0x00, 0x00, 0x00, 0x00, 0x00]
		PID_dict['distance_traveled_since_clear'] = [mode, 0x31, 0x00, 0x00, 0x00, 0x00, 0x00]
		PID_dict['evap_vapour_pressure'] = [mode, 0x32, 0x00, 0x00, 0x00, 0x00, 0x00]
		PID_dict['baromatic_pressure'] = [mode, 0x33, 0x00, 0x00, 0x00, 0x00, 0x00]
		PID_dict['CO2S1_WR_lambda'] = [mode, 0x34, 0x00, 0x00, 0x00, 0x00, 0x00]
		PID_dict['CO2S2_WR_lambda'] = [mode, 0x35, 0x00, 0x00, 0x00, 0x00, 0x00]
		PID_dict['CO2S3_WR_lambda'] = [mode, 0x36, 0x00, 0x00, 0x00, 0x00, 0x00]
		PID_dict['CO2S4_WR_lambda'] = [mode, 0x37, 0x00, 0x00, 0x00, 0x00, 0x00]
		PID_dict['CO2S5_WR_lambda'] = [mode, 0x38, 0x00, 0x00, 0x00, 0x00, 0x00]
		PID_dict['CO2S6_WR_lambda'] = [mode, 0x39, 0x00, 0x00, 0x00, 0x00, 0x00]
		PID_dict['CO2S7_WR_lambda'] = [mode, 0x3A, 0x00, 0x00, 0x00, 0x00, 0x00]
		PID_dict['CO2S8_WR_lambda'] = [mode, 0x3B, 0x00, 0x00, 0x00, 0x00, 0x00]
		PID_dict['catalyst_temp_B1S1'] = [mode, 0x3C, 0x00, 0x00, 0x00, 0x00, 0x00]
		PID_dict['catalyst_temp_B2S1'] = [mode, 0x3D, 0x00, 0x00, 0x00, 0x00, 0x00]
		PID_dict['catalyst_temp_B1S2'] = [mode, 0x3E, 0x00, 0x00, 0x00, 0x00, 0x00]
		PID_dict['catalyst_temp_B2S2'] = [mode, 0x3F, 0x00, 0x00, 0x00, 0x00, 0x00]
		PID_dict['pids_support_41_60'] = [mode, 0x40, 0x00, 0x00, 0x00, 0x00, 0x00]
		PID_dict['monitor_status_drive_cycle'] = [mode, 0x41, 0x00, 0x00, 0x00, 0x00, 0x00]
		PID_dict['control_module_voltage'] = [mode, 0x42, 0x00, 0x00, 0x00, 0x00, 0x00]
		PID_dict['absolute_load'] = [mode, 0x43, 0x00, 0x00, 0x00, 0x00, 0x00]
		PID_dict['command_equivalence_ratio'] = [mode, 0x44, 0x00, 0x00, 0x00, 0x00, 0x00]
		PID_dict['relative_throttle_position'] = [mode, 0x45, 0x00, 0x00, 0x00, 0x00, 0x00]
		PID_dict['ambient_air_temp'] = [mode, 0x46, 0x00, 0x00, 0x00, 0x00, 0x00]
		PID_dict['absolute_throttle_position_B'] = [mode, 0x47, 0x00, 0x00, 0x00, 0x00, 0x00]
		PID_dict['absolute_throttle_position_C'] = [mode, 0x48, 0x00, 0x00, 0x00, 0x00, 0x00]
		PID_dict['absolute_throttle_position_D'] = [mode, 0x49, 0x00, 0x00, 0x00, 0x00, 0x00]
		PID_dict['absolute_throttle_position_E'] = [mode, 0x4A, 0x00, 0x00, 0x00, 0x00, 0x00]
		PID_dict['absolute_throttle_position_F'] = [mode, 0x4B, 0x00, 0x00, 0x00, 0x00, 0x00]
		PID_dict['command_throttle_actuator'] = [mode, 0x4C, 0x00, 0x00, 0x00, 0x00, 0x00]
		PID_dict['time_run_with_MIL'] = [mode, 0x4D, 0x00, 0x00, 0x00, 0x00, 0x00]
		PID_dict['time_since_MIL_clear'] = [mode, 0x4E, 0x00, 0x00, 0x00, 0x00, 0x00]
		PID_dict['fuel_type'] = [mode, 0x51, 0x00, 0x00, 0x00, 0x00, 0x00]
		PID_dict['ethanol_fuel_percent'] = [mode, 0x52, 0x00, 0x00, 0x00, 0x00, 0x00]
		PID_dict['VIN'] = [0x09, 0x02, 0x00, 0x00, 0x00, 0x00, 0x00]
		return PID_dict

	def listen_obd(self):
		"""This obd device to read CAN frames"""
		assert self._ready

		try:
			stream = self.bus.recv(timeout=2)
			while(stream is not None):
				print("Message recieved on {}".format(self.bus.channel_info))
				print("The Message recieved is:{}".format(stream))
				return stream
		except can.CanError:
			print("Message could not be recieved")

	def read_obd(self, message, mode):
		"""to read CAN frames after a request. message = <string>, mode = <1,2> (1:current obd, 2: info at last diagnostic error code flag"""
		assert self._ready

		PID_dict = self.init_pids(mode)

		try:
			stream = self.bus.recv(timeout=2)
			request = PID_dict[message]
			while(stream is not None):
				print("Message recieved on {}".format(self.bus.channel_info))
				print("The Message recieved is:{}".format(stream))

				"""matches response in the stream with the requesting pids"""
				#if((stream.data[1] - 0x40) == request[1] and stream.data[2] == request[2]):
					return stream

		except can.CanError:
			print("Message could not be recieved")

	def send_obd(self, message, mode):
		"""This obd device to send CAN frames"""
		assert self._ready

		PID_dict = self.init_pids(mode)

		msg = can.Message(arbitration_id=0xc0ffee,
			data=PID_dict[message],
			extended_id=False)
		try:
			self.bus.send(msg)
			print("The Message sent is:{}".format(msg))
			print("Message sent on {}".format(self.bus.channel_info))
		except can.CanError:
			print("Message NOT sent")

	def parse_obd_info(self, message, response):
		"""Parses byte array from bus stream into readable info according to lookup table"""
		if(message == 'pidsupport'):
			"""TODO: http://www.geekmyride.org/wiki/index.php/OBD-II_PIDs#Bitwise_encoded_PIDs"""

		elif(message == 'monitor_status'):
			"""TODO: http://www.geekmyride.org/wiki/index.php/OBD-II_PIDs#Bitwise_encoded_PIDs"""

		elif(message == 'freeze_dtc'):
			print("Froze DTC")
			return

		elif(message == 'fuel_system_status'):
			"""TODO: http://www.geekmyride.org/wiki/index.php/OBD-II_PIDs#Bitwise_encoded_PIDs"""

		elif(message == 'engine_load'):
			"""returns %, A*100/255"""
			return (int(response[3], 16)*100)/255

		elif(message == 'coolant_temp'):
			"""returns Celcius, A-40"""
			return int(response[3], 16)-40

		elif(message == 'sterm_fuel1'):
			"""returns %, (A-128) * 100/128"""
			return (int(response[3], 16)-128) * (100/128)

		elif(message == 'lterm_fuel1'):
			"""returns %, (A-128) * 100/128"""
			return (int(response[3], 16)-128) * (100/128)

		elif(message == 'sterm_fuel2'):
			"""returns %, (A-128) * 100/128"""
			return (int(response[3], 16)-128) * (100/128)
		
		elif(message == 'lterm_fuel2'):
			"""returns %, (A-128) * 100/128"""
			return (int(response[3], 16)-128) * (100/128)
		
		elif(message == 'fuel_pressure'):
			"""returns kPa, A"""
			return int(response[3], 16)
		
		elif(message == 'intake_manifold_pressure'):
			"""returns kPa, A*3"""
			return int(response[3], 16)*3
		
		elif(message == 'rpm'):
			"""returns rpm, ((A*256)+B)/4"""
			return (int(response[3], 16)*256 + int(response[4], 16))/4
		
		elif(message == 'speed'):
			"""returns km/h, A"""
			return int(response[3], 16)
		
		elif(message == 'timing_advance'):
			"""returns degress relative to cylinder 1, A/2 - 64"""
			return int(response[3], 16)/2 - 64
		
		elif(message == 'intake_air_temp'):
			"""returns Celcius, A-40"""
			return int(response[3], 16)-40
		
		elif(message == 'MAF_flow'):
			"""returns g/s, ((256*A)+B) / 100"""
			return ((256*int(response[3], 16)) + int(response[4], 16))/100

		elif(message == 'throttle_position'):
			"""returns %, A*100/255"""
			return int(response[3], 16)*100/255

		elif(message == 'secondary_air_status'):
			"""TODO: http://www.geekmyride.org/wiki/index.php/OBD-II_PIDs#Bitwise_encoded_PIDs"""
			return int(response[3], 16)

		elif(message == 'oxygen_present'):
			"""TODO: http://www.geekmyride.org/wiki/index.php/OBD-II_PIDs#Bitwise_encoded_PIDs"""
			return int(response[3], 16)

		elif(message == 'oxy_b1_s1'):
			"""TODO: http://www.geekmyride.org/wiki/index.php/OBD-II_PIDs#Bitwise_encoded_PIDs"""
			return int(response[3], 16)

		elif(message == 'oxy_b1_s2'):
			"""TODO: http://www.geekmyride.org/wiki/index.php/OBD-II_PIDs#Bitwise_encoded_PIDs"""
			return int(response[3], 16)

		elif(message == 'oxy_b1_s3'):
			"""TODO: http://www.geekmyride.org/wiki/index.php/OBD-II_PIDs#Bitwise_encoded_PIDs"""
			return int(response[3], 16)

		elif(message == 'oxy_b1_s4'):
			"""TODO: http://www.geekmyride.org/wiki/index.php/OBD-II_PIDs#Bitwise_encoded_PIDs"""
			return int(response[3], 16)

		elif(message == 'oxy_b2_s1'):
			"""TODO: http://www.geekmyride.org/wiki/index.php/OBD-II_PIDs#Bitwise_encoded_PIDs"""
			return int(response[3], 16)

		elif(message == 'oxy_b2_s3'):
			"""TODO: http://www.geekmyride.org/wiki/index.php/OBD-II_PIDs#Bitwise_encoded_PIDs"""
			return int(response[3], 16)

		elif(message == 'oxy_b2_s3'):
			"""TODO: http://www.geekmyride.org/wiki/index.php/OBD-II_PIDs#Bitwise_encoded_PIDs"""
			return int(response[3], 16)

		elif(message == 'oxy_b2_s4'):
			"""TODO: http://www.geekmyride.org/wiki/index.php/OBD-II_PIDs#Bitwise_encoded_PIDs"""
			return int(response[3], 16)

		elif(message == 'obd_standard_id'):
			"""TODO: http://www.geekmyride.org/wiki/index.php/OBD-II_PIDs#Bitwise_encoded_PIDs"""
			return int(response[3], 16)

		elif(message == 'oxygen_sensor_present'):
			"""TODO: http://www.geekmyride.org/wiki/index.php/OBD-II_PIDs#Bitwise_encoded_PIDs"""
			return int(response[3], 16)

		elif(message == 'aux_input_status'):
			"""returns kPa, A&4"""
			return int(response[3], 16)&4

		elif(message == 'engine_run_time'):
			"""returns seconds, (A*256)+B"""
			return (int(response[3], 16)*256) + int(response[4], 16)

		elif(message == 'pids_suport_21_40'):
			"""TODO: http://www.geekmyride.org/wiki/index.php/OBD-II_PIDs#Bitwise_encoded_PIDs"""
			return int(response[3], 16)

		elif(message == 'distance_traveled_MIL'):
			"""returns seconds, (A*256)+B"""
			return (int(response[3], 16)*256) + int(response[4], 16)

		elif(message == 'fuel_rail_pressure'):
			"""returns kPA, ((A*256)+B)*0.079"""
			return ((int(response[3], 16)*256) + int(response[4], 16))*0.079

		elif(message == 'fuel_rail_pressure_diesel'):
			"""returns kPa, ((A*256)+B)*10"""
			return ((int(response[3], 16)*256) + int(response[4], 16))*10

		elif(message == 'VO2S1_WR_lambda'):
			"""TODO: http://www.geekmyride.org/wiki/index.php/OBD-II_PIDs#Bitwise_encoded_PIDs"""
			return int(response[3], 16)

		elif(message == 'VO2S2_WR_lambda'):
			"""TODO: http://www.geekmyride.org/wiki/index.php/OBD-II_PIDs#Bitwise_encoded_PIDs"""
			return int(response[3], 16)

		elif(message == 'VO2S3_WR_lambda'):
			"""TODO: http://www.geekmyride.org/wiki/index.php/OBD-II_PIDs#Bitwise_encoded_PIDs"""
			return int(response[3], 16)

		elif(message == 'VO2S4_WR_lambda'):
			"""TODO: http://www.geekmyride.org/wiki/index.php/OBD-II_PIDs#Bitwise_encoded_PIDs"""
			return int(response[3], 16)

		elif(message == 'VO2S5_WR_lambda'):
			"""TODO: http://www.geekmyride.org/wiki/index.php/OBD-II_PIDs#Bitwise_encoded_PIDs"""
			return int(response[3], 16)
		elif(message == 'VO2S6_WR_lambda'):
			"""TODO: http://www.geekmyride.org/wiki/index.php/OBD-II_PIDs#Bitwise_encoded_PIDs"""
			return int(response[3], 16)

		elif(message == 'VO2S7_WR_lambda'):
			"""TODO: http://www.geekmyride.org/wiki/index.php/OBD-II_PIDs#Bitwise_encoded_PIDs"""
			return int(response[3], 16)

		elif(message == 'VO2S8_WR_lambda'):
			"""TODO: http://www.geekmyride.org/wiki/index.php/OBD-II_PIDs#Bitwise_encoded_PIDs"""
			return int(response[3], 16)

		elif(message == 'ERG'):
			"""returns %, 100*A/255"""
			return 100 * int(response[3], 16) / 255

		elif(message == 'ERG_error'):
			"""returns %, A*0.78125 - 100"""
			return int(response[3], 16) * 0.78125 - 100

		elif(message == 'evaporative_purge'):
			"""returns %, 100*A/255"""
			return 100* int(response[3], 16) / 255

		elif(message == 'fuel_level'):
			"""returns %, 100*A/255"""
			return 100* int(response[3], 16) / 255

		elif(message == 'warm_up_attemps_since_clear'):
			"""returns N/A, A"""
			return int(response[3], 16)

		elif(message == 'distance_traveled_since_clear'):
			"""returns km, (A*256)+B"""
			return (int(response[3], 16) * 256) + int(response[4], 16)
		elif(message == 'evap_vapour_pressure'):
			"""returns kPa, (A*256)+B)/4 - 8,192"""
			return ((int(response[3], 16) * 256) + int(response[3],16))/4 - 8192

		elif(message == 'baromatic_pressure'):
			"""TODO: http://www.geekmyride.org/wiki/index.php/OBD-II_PIDs#Bitwise_encoded_PIDs"""
			return int(response[3], 16)
		elif(message == 'CO2S1_WR_lambda'):
			"""TODO: http://www.geekmyride.org/wiki/index.php/OBD-II_PIDs#Bitwise_encoded_PIDs"""
			return int(response[3], 16)

		elif(message == 'CO2S2_WR_lambda'):
			"""TODO: http://www.geekmyride.org/wiki/index.php/OBD-II_PIDs#Bitwise_encoded_PIDs"""
			return int(response[3], 16)
		elif(message == 'CO2S3_WR_lambda'):
			"""TODO: http://www.geekmyride.org/wiki/index.php/OBD-II_PIDs#Bitwise_encoded_PIDs"""
			return int(response[3], 16)

		elif(message == 'CO2S4_WR_lambda'):
			"""TODO: http://www.geekmyride.org/wiki/index.php/OBD-II_PIDs#Bitwise_encoded_PIDs"""
			return int(response[3], 16)
		elif(message == 'CO2S5_WR_lambda'):
			"""TODO: http://www.geekmyride.org/wiki/index.php/OBD-II_PIDs#Bitwise_encoded_PIDs"""
			return int(response[3], 16)

		elif(message == 'CO2S6_WR_lambda'):
			"""TODO: http://www.geekmyride.org/wiki/index.php/OBD-II_PIDs#Bitwise_encoded_PIDs"""
			return int(response[3], 16)
		elif(message == 'CO2S7_WR_lambda'):
			"""TODO: http://www.geekmyride.org/wiki/index.php/OBD-II_PIDs#Bitwise_encoded_PIDs"""
			return int(response[3], 16)

		elif(message == 'CO2S8_WR_lambda'):
			"""TODO: http://www.geekmyride.org/wiki/index.php/OBD-II_PIDs#Bitwise_encoded_PIDs"""
			return int(response[3], 16)
		elif(message == 'catalyst_temp_B1S1'):
			"""returns Celsius, ((A*256)+B)/10 - 40"""
			return ((int(response[3], 16)*256)+ int(response[4], 16))/10 - 40
		elif(message == 'catalyst_temp_B2S1'):
			"""returns Celsius, ((A*256)+B)/10 - 40"""
			return ((int(response[3], 16)*256)+ int(response[4], 16))/10 - 40

		elif(message == 'catalyst_temp_B1S2'):
			"""returns Celsius, ((A*256)+B)/10 - 40"""
			return ((int(response[3], 16)*256)+ int(response[4], 16))/10 - 40

		elif(message == 'catalyst_temp_B2S2'):
			"""returns Celsius, ((A*256)+B)/10 - 40"""
			return ((int(response[3], 16)*256)+ int(response[4], 16))/10 - 40

		elif(message == 'pids_support_41_60'):
			"""TODO: http://www.geekmyride.org/wiki/index.php/OBD-II_PIDs#Bitwise_encoded_PIDs"""
			return int(response[3], 16)
		elif(message == 'monitor_status_drive_cycle'):
			"""TODO: http://www.geekmyride.org/wiki/index.php/OBD-II_PIDs#Bitwise_encoded_PIDs"""
			return int(response[3], 16)
		elif(message == 'control_module_voltage'):
			"""returns Voltage, ((A*256)+B)/1000"""
			return ((int(response[3], 16)*256)+ int(response[4], 16))/1000

		elif(message == 'absolute_load'):
			"""returns %, ((A*256)+B)*100/255"""
			return ((int(response[3], 16)*256)+ int(response[4], 16)) * 100/255

		elif(message == 'command_equivalence_ratio'):
			"""returns N/A, ((A*256)+B)*0.0000305"""
			return ((int(response[3], 16)*256)+ int(response[4], 16)) * 0.0000305
		elif(message == 'relative_throttle_position'):
			"""returns %, A*100/255"""
			return int(response[3], 16) * 100/255
		elif(message == 'ambient_air_temp'):
			"""returns Celsius, A-40"""
			return int(response[3], 16) - 40
		elif(message == 'absolute_throttle_position_B'):
			"""returns %, A*100/255"""
			return int(response[3], 16)*100/255
		elif(message == 'absolute_throttle_position_C'):
			"""returns %, A*100/255"""
			return int(response[3], 16)*100/255
		elif(message == 'absolute_throttle_position_D'):
			"""returns %, A*100/255"""
			return int(response[3], 16)*100/255
		elif(message == 'absolute_throttle_position_E'):
			"""returns %, A*100/255"""
			return int(response[3], 16)*100/255
		elif(message == 'absolute_throttle_position_F'):
			"""returns %, A*100/255"""
			return int(response[3], 16)*100/255
		elif(message == 'command_throttle_actuator'):
			"""returns %, A*100/255"""
			return int(response[3], 16)*100/255
		elif(message == 'time_run_with_MIL'):
			"""returns minutes, (A*256)+B"""
			return ((int(response[3], 16)*256)+ int(response[4], 16))
		elif(message == 'time_since_MIL_clear'):
			"""returns minutes, (A*256)+B"""
			return ((int(response[3], 16)*256)+ int(response[4], 16))
		elif(message == 'fuel_type'):
			"""TODO: http://www.geekmyride.org/wiki/index.php/OBD-II_PIDs#Bitwise_encoded_PIDs"""
			return int(response[3], 16)
		elif(message == 'ethanol_fuel_percent'):
			"""returns %, A*100/255"""
			return int(response[3], 16)*100/255
		elif(message == 'VIN'):
			"""TODO: http://www.geekmyride.org/wiki/index.php/OBD-II_PIDs#Bitwise_encoded_PIDs"""
			A = response[3]
			B = response[4]
			C = response[5]
			D = response[6]
			E = response[7]
			return int(response[3], 16)


		return result

	def get_obd_info(self, message, mode) -> Measure:
		"""function handles sends and recieved messages and returns readable information"""
		time = datetime.datetime.now()
		self.send_obd(message, mode)
		hex_value = self.read_obd(message, mode)
		print (hex_value)
		parsed_value =  self.parse_obd_info(message, hex_value )

		print (parsed_value)	

	def close_bus(self):
		self.bus.shutdown()
