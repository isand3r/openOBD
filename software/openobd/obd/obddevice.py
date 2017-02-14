from obd.iobddevice import IOBDDevice
from measure.measure import Measure
import time
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
		PID_dict['pidsupport'] = [0x02, mode, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]
		PID_dict['monitor_status'] = [0x02, mode, 0x01, 0x00, 0x00, 0x00, 0x00, 0x00]
		PID_dict['freeze_dtc'] = [0x02, mode, 0x02, 0x00, 0x00, 0x00, 0x00, 0x00]
		PID_dict['fuel_system_status'] = [0x02, mode, 0x03, 0x00, 0x00, 0x00, 0x00, 0x00]
		PID_dict['engine_load'] = [0x02, mode, 0x04, 0x00, 0x00, 0x00, 0x00, 0x00]
		PID_dict['coolant_temp'] = [0x02, mode, 0x05, 0x00, 0x00, 0x00, 0x00, 0x00]
		PID_dict['sterm_fuel1'] = [0x02, mode, 0x06, 0x00, 0x00, 0x00, 0x00, 0x00]
		PID_dict['lterm_fuel1'] = [0x02, mode, 0x07, 0x00, 0x00, 0x00, 0x00, 0x00]
		PID_dict['sterm_fuel2'] = [0x02, mode, 0x08, 0x00, 0x00, 0x00, 0x00, 0x00]
		PID_dict['lterm_fuel2'] = [0x02, mode, 0x09, 0x00, 0x00, 0x00, 0x00, 0x00]
		PID_dict['fuel_pressure'] = [0x02, mode, 0x0A, 0x00, 0x00, 0x00, 0x00, 0x00]
		PID_dict['intake_manifold_pressure'] = [0x02, mode, 0x0B, 0x00, 0x00, 0x00, 0x00, 0x00]
		PID_dict['rpm'] = [0x02, mode, 0x0C, 0x00, 0x00, 0x00, 0x00, 0x00]
		PID_dict['speed'] = [0x02, mode, 0x0D, 0x00, 0x00, 0x00, 0x00, 0x00]
		PID_dict['timing_advance'] = [0x02, mode, 0x0E, 0x00, 0x00, 0x00, 0x00, 0x00]
		PID_dict['intake_air_temp'] = [0x02, mode, 0x0F, 0x00, 0x00, 0x00, 0x00, 0x00]
		PID_dict['MAF_flow'] = [0x02, mode, 0x10, 0x00, 0x00, 0x00, 0x00, 0x00]
		PID_dict['throttle_position'] = [0x02, mode, 0x11, 0x00, 0x00, 0x00, 0x00, 0x00]
		PID_dict['secondary_air_status'] = [0x02, mode, 0x12, 0x00, 0x00, 0x00, 0x00, 0x00]
		PID_dict['oxygen_present'] = [0x02, mode, 0x13, 0x00, 0x00, 0x00, 0x00, 0x00]
		PID_dict['oxy_b1_s1'] = [0x02, mode, 0x14, 0x00, 0x00, 0x00, 0x00, 0x00]
		PID_dict['oxy_b1_s2'] = [0x02, mode, 0x15, 0x00, 0x00, 0x00, 0x00, 0x00]
		PID_dict['oxy_b1_s3'] = [0x02, mode, 0x16, 0x00, 0x00, 0x00, 0x00, 0x00]
		PID_dict['oxy_b1_s4'] = [0x02, mode, 0x17, 0x00, 0x00, 0x00, 0x00, 0x00]
		PID_dict['oxy_b2_s1'] = [0x02, mode, 0x18, 0x00, 0x00, 0x00, 0x00, 0x00]
		PID_dict['oxy_b2_s2'] = [0x02, mode, 0x019, 0x00, 0x00, 0x00, 0x00, 0x00]
		PID_dict['oxy_b2_s3'] = [0x02, mode, 0x01A, 0x00, 0x00, 0x00, 0x00, 0x00]
		PID_dict['oxy_b2_s4'] = [0x02, mode, 0x01B, 0x00, 0x00, 0x00, 0x00, 0x00]
		PID_dict['obd_standard_id'] = [0x02, mode, 0x1C, 0x00, 0x00, 0x00, 0x00, 0x00]
		PID_dict['oxygen_sensor_present'] = [0x02, mode, 0x1D, 0x00, 0x00, 0x00, 0x00, 0x00]
		PID_dict['aux_input_status'] = [0x02, mode, 0x1E, 0x00, 0x00, 0x00, 0x00, 0x00]
		PID_dict['engine_run_time'] = [0x02, mode, 0x1F, 0x00, 0x00, 0x00, 0x00, 0x00]
		PID_dict['pids_suport_21_40'] = [0x02, mode, 0x20, 0x00, 0x00, 0x00, 0x00, 0x00]
		PID_dict['distance_traveled_MIL'] = [0x02, mode, 0x21, 0x00, 0x00, 0x00, 0x00, 0x00]
		PID_dict['fuel_rail_pressure'] = [0x02, mode, 0x22, 0x00, 0x00, 0x00, 0x00, 0x00]
		PID_dict['fuel_rail_pressure_diesel'] = [0x02, mode, 0x23, 0x00, 0x00, 0x00, 0x00, 0x00]
		PID_dict['VO2S1_WR_lambda'] = [0x02, mode, 0x24, 0x00, 0x00, 0x00, 0x00, 0x00]
		PID_dict['VO2S2_WR_lambda'] = [0x02, mode, 0x25, 0x00, 0x00, 0x00, 0x00, 0x00]
		PID_dict['VO2S3_WR_lambda'] = [0x02, mode, 0x26, 0x00, 0x00, 0x00, 0x00, 0x00]
		PID_dict['VO2S4_WR_lambda'] = [0x02, mode, 0x27, 0x00, 0x00, 0x00, 0x00, 0x00]
		PID_dict['VO2S5_WR_lambda'] = [0x02, mode, 0x28, 0x00, 0x00, 0x00, 0x00, 0x00]
		PID_dict['VO2S6_WR_lambda'] = [0x02, mode, 0x29, 0x00, 0x00, 0x00, 0x00, 0x00]
		PID_dict['VO2S7_WR_lambda'] = [0x02, mode, 0x2A, 0x00, 0x00, 0x00, 0x00, 0x00]
		PID_dict['VO2S8_WR_lambda'] = [0x02, mode, 0x2B, 0x00, 0x00, 0x00, 0x00, 0x00]
		PID_dict['ERG'] = [0x02, mode, 0x2C, 0x00, 0x00, 0x00, 0x00, 0x00]
		PID_dict['ERG_error'] = [0x02, mode, 0x2D, 0x00, 0x00, 0x00, 0x00, 0x00]
		PID_dict['evaporative_purge'] = [0x02, mode, 0x2E, 0x00, 0x00, 0x00, 0x00, 0x00]
		PID_dict['fuel_level'] = [0x02, mode, 0x2F, 0x00, 0x00, 0x00, 0x00, 0x00]
		PID_dict['warm_up_attemps_since_clear'] = [0x02, mode, 0x30, 0x00, 0x00, 0x00, 0x00, 0x00]
		PID_dict['distance_traveled_since_clear'] = [0x02, mode, 0x31, 0x00, 0x00, 0x00, 0x00, 0x00]
		PID_dict['evap_vapour_pressure'] = [0x02, mode, 0x32, 0x00, 0x00, 0x00, 0x00, 0x00]
		PID_dict['baromatic_pressure'] = [0x02, mode, 0x33, 0x00, 0x00, 0x00, 0x00, 0x00]
		PID_dict['CO2S1_WR_lambda'] = [0x02, mode, 0x34, 0x00, 0x00, 0x00, 0x00, 0x00]
		PID_dict['CO2S2_WR_lambda'] = [0x02, mode, 0x35, 0x00, 0x00, 0x00, 0x00, 0x00]
		PID_dict['CO2S3_WR_lambda'] = [0x02, mode, 0x36, 0x00, 0x00, 0x00, 0x00, 0x00]
		PID_dict['CO2S4_WR_lambda'] = [0x02, mode, 0x37, 0x00, 0x00, 0x00, 0x00, 0x00]
		PID_dict['CO2S5_WR_lambda'] = [0x02, mode, 0x38, 0x00, 0x00, 0x00, 0x00, 0x00]
		PID_dict['CO2S6_WR_lambda'] = [0x02, mode, 0x39, 0x00, 0x00, 0x00, 0x00, 0x00]
		PID_dict['CO2S7_WR_lambda'] = [0x02, mode, 0x3A, 0x00, 0x00, 0x00, 0x00, 0x00]
		PID_dict['CO2S8_WR_lambda'] = [0x02, mode, 0x3B, 0x00, 0x00, 0x00, 0x00, 0x00]
		PID_dict['catalyst_temp_B1S1'] = [0x02, mode, 0x3C, 0x00, 0x00, 0x00, 0x00, 0x00]
		PID_dict['catalyst_temp_B2S1'] = [0x02, mode, 0x3D, 0x00, 0x00, 0x00, 0x00, 0x00]
		PID_dict['catalyst_temp_B1S2'] = [0x02, mode, 0x3E, 0x00, 0x00, 0x00, 0x00, 0x00]
		PID_dict['catalyst_temp_B2S2'] = [0x02, mode, 0x3F, 0x00, 0x00, 0x00, 0x00, 0x00]
		PID_dict['pids_support_41_60'] = [0x02, mode, 0x40, 0x00, 0x00, 0x00, 0x00, 0x00]
		PID_dict['monitor_status_drive_cycle'] = [0x02, mode, 0x41, 0x00, 0x00, 0x00, 0x00, 0x00]
		PID_dict['control_module_voltage'] = [0x02, mode, 0x42, 0x00, 0x00, 0x00, 0x00, 0x00]
		PID_dict['absolute_load'] = [0x02, mode, 0x43, 0x00, 0x00, 0x00, 0x00, 0x00]
		PID_dict['command_equivalence_ratio'] = [0x02, mode, 0x44, 0x00, 0x00, 0x00, 0x00, 0x00]
		PID_dict['relative_throttle_position'] = [0x02, mode, 0x45, 0x00, 0x00, 0x00, 0x00, 0x00]
		PID_dict['ambient_air_temp'] = [0x02, mode, 0x46, 0x00, 0x00, 0x00, 0x00, 0x00]
		PID_dict['absolute_throttle_position_B'] = [0x02, mode, 0x47, 0x00, 0x00, 0x00, 0x00, 0x00]
		PID_dict['absolute_throttle_position_C'] = [0x02, mode, 0x48, 0x00, 0x00, 0x00, 0x00, 0x00]
		PID_dict['absolute_throttle_position_D'] = [0x02, mode, 0x49, 0x00, 0x00, 0x00, 0x00, 0x00]
		PID_dict['absolute_throttle_position_E'] = [0x02, mode, 0x4A, 0x00, 0x00, 0x00, 0x00, 0x00]
		PID_dict['absolute_throttle_position_F'] = [0x02, mode, 0x4B, 0x00, 0x00, 0x00, 0x00, 0x00]
		PID_dict['command_throttle_actuator'] = [0x02, mode, 0x4C, 0x00, 0x00, 0x00, 0x00, 0x00]
		PID_dict['time_run_with_MIL'] = [0x02, mode, 0x4D, 0x00, 0x00, 0x00, 0x00, 0x00]
		PID_dict['time_since_MIL_clear'] = [0x02, mode, 0x4E, 0x00, 0x00, 0x00, 0x00, 0x00]
		PID_dict['fuel_type'] = [0x02, mode, 0x51, 0x00, 0x00, 0x00, 0x00, 0x00]
		PID_dict['ethanol_fuel_percent'] = [0x02, mode, 0x52, 0x00, 0x00, 0x00, 0x00, 0x00]
		PID_dict['VIN'] = [0x02, 0x09, 0x02, 0x00, 0x00, 0x00, 0x00, 0x00]
		return PID_dict

	def listen_obd(self):
		"""This obd device to read CAN frames"""
		assert self._ready

		try:
			self.bus.set_filters(can_filters = [{"can_id": 0x7E8, "can_mask": 0x1FFFFFF8}])
			stream = self.bus.recv(timeout=2)
			self.bus.set_filters(can_filters = [{"can_id": 0x7E8, "can_mask": 0x1FFFFFF8}])
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
			self.bus.set_filters(can_filters = [{"can_id": 0x7E8, "can_mask": 0x1FFFFFF8}])
			stream = self.bus.recv(timeout=2)
			self.bus.set_filters(can_filters = [{"can_id": 0x7E8, "can_mask": 0x1FFFFFF8}])
			request = PID_dict[message]
			while(stream is not None):
				#print("Message recieved on {}".format(self.bus.channel_info))
				#print("The Message recieved is:{}".format(stream))

				"""matches response in the stream with the requesting pids"""
				
				if(len(stream.data)>2 and (stream.data[1] - 0x40) == request[1] and stream.data[2] == request[2]):
					if stream is not None:
						#print ("the response" + str(stream))
						result =  self.parse_obd_info(message, stream.data )
						return result
				
				stream = self.bus.recv(timeout=2)

		except can.CanError:
			print("Message could not be recieved")

	def send_obd(self, message, mode):
		"""This obd device to send CAN frames"""
		assert self._ready

		PID_dict = self.init_pids(mode)

		msg = can.Message(extended_id=False, arbitration_id=0x7DF,
			data=PID_dict[message])
		try:
			self.bus.send(msg)
			#print("The Message sent is:{}".format(msg))
			#print("Message sent on {}".format(self.bus.channel_info))
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
			time = datetime.datetime.now()
			result = Measure((int(response[3] )*100)/255, "%", time)
			return result

		elif(message == 'coolant_temp'):
			"""returns Celcius, A-40"""
			time = datetime.datetime.now()
			result = Measure(int(response[3] )-40, "Celcius", time)
			return result

		elif(message == 'sterm_fuel1'):
			"""returns %, (A-128) * 100/128"""
			time = datetime.datetime.now()
			result = Measure((int(response[3] )-128) * (100/128), "%", time)
			return result

		elif(message == 'lterm_fuel1'):
			"""returns %, (A-128) * 100/128"""
			time = datetime.datetime.now()
			result = Measure((int(response[3] )-128) * (100/128), "%", time)
			return result

		elif(message == 'sterm_fuel2'):
			"""returns %, (A-128) * 100/128"""
			time = datetime.datetime.now()
			result = Measure((int(response[3] )-128) * (100/128), "%", time)
			return result
		
		elif(message == 'lterm_fuel2'):
			"""returns %, (A-128) * 100/128"""
			time = datetime.datetime.now()
			result = Measure((int(response[3] )-128) * (100/128), "%", time)
			return result

		elif(message == 'fuel_pressure'):
			"""returns kPa, A"""
			time = datetime.datetime.now()
			result = Measure(int(response[3] ), "kPa", time)
			return result
		
		elif(message == 'intake_manifold_pressure'):
			"""returns kPa, A*3"""
			time = datetime.datetime.now()
			result = Measure(int(response[3] )*3, "kPa", time)
			return result
		
		elif(message == 'rpm'):
			"""returns rpm, ((A*256)+B)/4"""
			time = datetime.datetime.now()
			result = Measure((int(response[3])*256 + int(response[4] ))/4, "rpm", time )
			return result
		
		elif(message == 'speed'):
			"""returns km/h, A"""
			time = datetime.datetime.now()
			result = Measure(int(response[3]), "km/h", time )
			return result
		
		elif(message == 'timing_advance'):
			"""returns degress relative to cylinder 1, A/2 - 64"""
			time = datetime.datetime.now()
			result = Measure(int(response[3] )/2 - 64, "degree", time )
			return result
		
		elif(message == 'intake_air_temp'):
			"""returns Celcius, A-40"""
			time = datetime.datetime.now()
			result = Measure(int(response[3] )-40, "Celcius", time )
			return result
		
		elif(message == 'MAF_flow'):
			"""returns g/s, ((256*A)+B) / 100"""
			time = datetime.datetime.now()
			result = Measure(((256*int(response[3] )) + int(response[4] ))/100, "g/s", time )
			return result

		elif(message == 'throttle_position'):
			"""returns %, A*100/255"""
			time = datetime.datetime.now()
			result = Measure(int(response[3] )*100/255, "%", time )
			return result

		elif(message == 'secondary_air_status'):
			"""TODO: http://www.geekmyride.org/wiki/index.php/OBD-II_PIDs#Bitwise_encoded_PIDs"""
			return int(response[3] )

		elif(message == 'oxygen_present'):
			"""TODO: http://www.geekmyride.org/wiki/index.php/OBD-II_PIDs#Bitwise_encoded_PIDs"""
			return int(response[3] )

		elif(message == 'oxy_b1_s1'):
			"""TODO: http://www.geekmyride.org/wiki/index.php/OBD-II_PIDs#Bitwise_encoded_PIDs"""
			return int(response[3] )

		elif(message == 'oxy_b1_s2'):
			"""TODO: http://www.geekmyride.org/wiki/index.php/OBD-II_PIDs#Bitwise_encoded_PIDs"""
			return int(response[3] )

		elif(message == 'oxy_b1_s3'):
			"""TODO: http://www.geekmyride.org/wiki/index.php/OBD-II_PIDs#Bitwise_encoded_PIDs"""
			return int(response[3] )

		elif(message == 'oxy_b1_s4'):
			"""TODO: http://www.geekmyride.org/wiki/index.php/OBD-II_PIDs#Bitwise_encoded_PIDs"""
			return int(response[3] )

		elif(message == 'oxy_b2_s1'):
			"""TODO: http://www.geekmyride.org/wiki/index.php/OBD-II_PIDs#Bitwise_encoded_PIDs"""
			return int(response[3] )

		elif(message == 'oxy_b2_s3'):
			"""TODO: http://www.geekmyride.org/wiki/index.php/OBD-II_PIDs#Bitwise_encoded_PIDs"""
			return int(response[3] )

		elif(message == 'oxy_b2_s3'):
			"""TODO: http://www.geekmyride.org/wiki/index.php/OBD-II_PIDs#Bitwise_encoded_PIDs"""
			return int(response[3] )

		elif(message == 'oxy_b2_s4'):
			"""TODO: http://www.geekmyride.org/wiki/index.php/OBD-II_PIDs#Bitwise_encoded_PIDs"""
			return int(response[3] )

		elif(message == 'obd_standard_id'):
			"""TODO: http://www.geekmyride.org/wiki/index.php/OBD-II_PIDs#Bitwise_encoded_PIDs"""
			return int(response[3] )

		elif(message == 'oxygen_sensor_present'):
			"""TODO: http://www.geekmyride.org/wiki/index.php/OBD-II_PIDs#Bitwise_encoded_PIDs"""
			return int(response[3] )

		elif(message == 'aux_input_status'):
			"""returns T/F, A&4"""
			time = datetime.datetime.now()
			result = Measure(int(response[3] )&4, "T/F", time )
			return result

		elif(message == 'engine_run_time'):
			"""returns seconds, (A*256)+B"""
			time = datetime.datetime.now()
			result = Measure((int(response[3] )*256) + int(response[4] ), "seconds", time )
			return result	

		elif(message == 'pids_suport_21_40'):
			"""TODO: http://www.geekmyride.org/wiki/index.php/OBD-II_PIDs#Bitwise_encoded_PIDs"""
			return int(response[3] )

		elif(message == 'distance_traveled_MIL'):
			"""returns seconds, (A*256)+B"""
			time = datetime.datetime.now()
			result = Measure((int(response[3] )*256) + int(response[4] ), "seconds", time )
			return result	

		elif(message == 'fuel_rail_pressure'):
			"""returns kPA, ((A*256)+B)*0.079"""
			time = datetime.datetime.now()
			result = Measure(((int(response[3] )*256) + int(response[4] ))*0.079, "kPa", time )
			return result

		elif(message == 'fuel_rail_pressure_diesel'):
			"""returns kPa, ((A*256)+B)*10"""
			time = datetime.datetime.now()
			result = Measure(((int(response[3] )*256) + int(response[4] ))*10, "kPa", time )
			return result

		elif(message == 'VO2S1_WR_lambda'):
			"""TODO: http://www.geekmyride.org/wiki/index.php/OBD-II_PIDs#Bitwise_encoded_PIDs"""
			return int(response[3] )

		elif(message == 'VO2S2_WR_lambda'):
			"""TODO: http://www.geekmyride.org/wiki/index.php/OBD-II_PIDs#Bitwise_encoded_PIDs"""
			return int(response[3] )

		elif(message == 'VO2S3_WR_lambda'):
			"""TODO: http://www.geekmyride.org/wiki/index.php/OBD-II_PIDs#Bitwise_encoded_PIDs"""
			return int(response[3] )

		elif(message == 'VO2S4_WR_lambda'):
			"""TODO: http://www.geekmyride.org/wiki/index.php/OBD-II_PIDs#Bitwise_encoded_PIDs"""
			return int(response[3] )

		elif(message == 'VO2S5_WR_lambda'):
			"""TODO: http://www.geekmyride.org/wiki/index.php/OBD-II_PIDs#Bitwise_encoded_PIDs"""
			return int(response[3] )
		elif(message == 'VO2S6_WR_lambda'):
			"""TODO: http://www.geekmyride.org/wiki/index.php/OBD-II_PIDs#Bitwise_encoded_PIDs"""
			return int(response[3] )

		elif(message == 'VO2S7_WR_lambda'):
			"""TODO: http://www.geekmyride.org/wiki/index.php/OBD-II_PIDs#Bitwise_encoded_PIDs"""
			return int(response[3] )

		elif(message == 'VO2S8_WR_lambda'):
			"""TODO: http://www.geekmyride.org/wiki/index.php/OBD-II_PIDs#Bitwise_encoded_PIDs"""
			return int(response[3] )

		elif(message == 'ERG'):
			"""returns %, 100*A/255"""
			time = datetime.datetime.now()
			result = Measure(100 * int(response[3] ) / 255, "%", time )
			return result

		elif(message == 'ERG_error'):
			"""returns %, A*0.78125 - 100"""
			time = datetime.datetime.now()
			result = Measure(int(response[3] ) * 0.78125 - 100, "%", time )
			return result

		elif(message == 'evaporative_purge'):
			"""returns %, 100*A/255"""
			time = datetime.datetime.now()
			result = Measure(100* int(response[3] ) / 255, "%", time )
			return result

		elif(message == 'fuel_level'):
			"""returns %, 100*A/255"""
			time = datetime.datetime.now()
			result = Measure(100* int(response[3] ) / 255, "%", time )
			return result

		elif(message == 'warm_up_attemps_since_clear'):
			"""returns N/A, A"""
			time = datetime.datetime.now()
			result = Measure(int(response[3] ), "N/A", time )
			return result

		elif(message == 'distance_traveled_since_clear'):
			"""returns km, (A*256)+B"""
			time = datetime.datetime.now()
			result = Measure((int(response[3] ) * 256) + int(response[4] ), "km", time )
			return result

		elif(message == 'evap_vapour_pressure'):
			"""returns kPa, (A*256)+B)/4 - 8,192"""
			time = datetime.datetime.now()
			result = Measure(((int(response[3] ) * 256) + int(response[3],16))/4 - 8192, "kPa", time )
			return result

		elif(message == 'baromatic_pressure'):
			"""TODO: http://www.geekmyride.org/wiki/index.php/OBD-II_PIDs#Bitwise_encoded_PIDs"""
			return int(response[3] )
		elif(message == 'CO2S1_WR_lambda'):
			"""TODO: http://www.geekmyride.org/wiki/index.php/OBD-II_PIDs#Bitwise_encoded_PIDs"""
			return int(response[3] )

		elif(message == 'CO2S2_WR_lambda'):
			"""TODO: http://www.geekmyride.org/wiki/index.php/OBD-II_PIDs#Bitwise_encoded_PIDs"""
			return int(response[3] )
		elif(message == 'CO2S3_WR_lambda'):
			"""TODO: http://www.geekmyride.org/wiki/index.php/OBD-II_PIDs#Bitwise_encoded_PIDs"""
			return int(response[3] )

		elif(message == 'CO2S4_WR_lambda'):
			"""TODO: http://www.geekmyride.org/wiki/index.php/OBD-II_PIDs#Bitwise_encoded_PIDs"""
			return int(response[3] )
		elif(message == 'CO2S5_WR_lambda'):
			"""TODO: http://www.geekmyride.org/wiki/index.php/OBD-II_PIDs#Bitwise_encoded_PIDs"""
			return int(response[3] )

		elif(message == 'CO2S6_WR_lambda'):
			"""TODO: http://www.geekmyride.org/wiki/index.php/OBD-II_PIDs#Bitwise_encoded_PIDs"""
			return int(response[3] )
		elif(message == 'CO2S7_WR_lambda'):
			"""TODO: http://www.geekmyride.org/wiki/index.php/OBD-II_PIDs#Bitwise_encoded_PIDs"""
			return int(response[3] )

		elif(message == 'CO2S8_WR_lambda'):
			"""TODO: http://www.geekmyride.org/wiki/index.php/OBD-II_PIDs#Bitwise_encoded_PIDs"""
			return int(response[3] )
		elif(message == 'catalyst_temp_B1S1'):
			"""returns Celcius, ((A*256)+B)/10 - 40"""
			time = datetime.datetime.now()
			result = Measure(((int(response[3])*256)+ int(response[4]))/10 - 40, "Celcius", time )
			return result

		elif(message == 'catalyst_temp_B2S1'):
			"""returns Celsius, ((A*256)+B)/10 - 40"""
			time = datetime.datetime.now()
			result = Measure(((int(response[3])*256)+ int(response[4]))/10 - 40, "Celcius", time )
			return result

		elif(message == 'catalyst_temp_B1S2'):
			"""returns Celsius, ((A*256)+B)/10 - 40"""
			time = datetime.datetime.now()
			result = Measure(((int(response[3])*256)+ int(response[4]))/10 - 40, "Celcius", time )
			return result

		elif(message == 'catalyst_temp_B2S2'):
			"""returns Celsius, ((A*256)+B)/10 - 40"""
			time = datetime.datetime.now()
			result = Measure(((int(response[3])*256)+ int(response[4]))/10 - 40, "Celcius", time )
			return result

		elif(message == 'pids_support_41_60'):
			"""TODO: http://www.geekmyride.org/wiki/index.php/OBD-II_PIDs#Bitwise_encoded_PIDs"""
			return int(response[3] )
		elif(message == 'monitor_status_drive_cycle'):
			"""TODO: http://www.geekmyride.org/wiki/index.php/OBD-II_PIDs#Bitwise_encoded_PIDs"""
			return int(response[3] )
		elif(message == 'control_module_voltage'):
			"""returns Voltage, ((A*256)+B)/1000"""
			time = datetime.datetime.now()
			result = Measure(((int(response[3] )*256)+ int(response[4] ))/1000, "Voltage", time )
			return result

		elif(message == 'absolute_load'):
			"""returns %, ((A*256)+B)*100/255"""
			time = datetime.datetime.now()
			result = Measure(((int(response[3] )*256)+ int(response[4] )) * 100/255, "%", time )
			return result

		elif(message == 'command_equivalence_ratio'):
			"""returns N/A, ((A*256)+B)*0.0000305"""
			time = datetime.datetime.now()
			result = Measure((((int(response[3] )*256)+ int(response[4] )) * 0.0000305) * 100/255, "N/A", time )
			return result

		elif(message == 'relative_throttle_position'):
			"""returns %, A*100/255"""
			time = datetime.datetime.now()
			result = Measure(int(response[3] ) * 100/255, "%", time )
			return result

		elif(message == 'ambient_air_temp'):
			"""returns Celcius, A-40"""
			time = datetime.datetime.now()
			result = Measure(int(response[3] ) - 40, "Celcius", time )
			return result

		elif(message == 'absolute_throttle_position_B'):
			"""returns %, A*100/255"""
			time = datetime.datetime.now()
			result = Measure(int(response[3] ) * 100/255, "%", time )
			return result

		elif(message == 'absolute_throttle_position_C'):
			"""returns %, A*100/255"""
			time = datetime.datetime.now()
			result = Measure(int(response[3] ) * 100/255, "%", time )
			return result

		elif(message == 'absolute_throttle_position_D'):
			"""returns %, A*100/255"""
			time = datetime.datetime.now()
			result = Measure(int(response[3] ) * 100/255, "%", time )
			return result

		elif(message == 'absolute_throttle_position_E'):
			"""returns %, A*100/255"""
			time = datetime.datetime.now()
			result = Measure(int(response[3] ) * 100/255, "%", time )
			return result

		elif(message == 'absolute_throttle_position_F'):
			"""returns %, A*100/255"""
			time = datetime.datetime.now()
			result = Measure(int(response[3] ) * 100/255, "%", time )
			return result

		elif(message == 'command_throttle_actuator'):
			"""returns %, A*100/255"""
			time = datetime.datetime.now()
			result = Measure(int(response[3] ) * 100/255, "%", time )
			return result

		elif(message == 'time_run_with_MIL'):
			"""returns minutes, (A*256)+B"""
			time = datetime.datetime.now()
			result = Measure(((int(response[3] )*256)+ int(response[4] )),"Minutes", time )
			return result

		elif(message == 'time_since_MIL_clear'):
			"""returns minutes, (A*256)+B"""
			time = datetime.datetime.now()
			result = Measure(((int(response[3] )*256)+ int(response[4] )),"Minutes", time )
			return result

		elif(message == 'fuel_type'):
			"""TODO: http://www.geekmyride.org/wiki/index.php/OBD-II_PIDs#Bitwise_encoded_PIDs"""
			return int(response[3] )
		elif(message == 'ethanol_fuel_percent'):
			"""returns %, A*100/255"""
			time = datetime.datetime.now()
			result = Measure(int(response[3] ) * 100/255, "%", time )
			return result
			
		elif(message == 'VIN'):
			"""TODO: http://www.geekmyride.org/wiki/index.php/OBD-II_PIDs#Bitwise_encoded_PIDs"""
			A = response[3]
			B = response[4]
			C = response[5]
			D = response[6]
			E = response[7]
			return int(response[3] )


		return result

	def get_obd_info(self, message, mode) -> Measure:
		"""function handles sends and recieved messages and returns readable information"""
		time = datetime.datetime.now()
		self.send_obd(message, mode)
		result = self.read_obd(message, mode)
		if result is None:
			print("Error, no response, trying again.")
		else:
			#print ("message Received:" + str(result.value) + str(result.units))	
			return result

	def close_bus(self):
		self.bus.shutdown()
