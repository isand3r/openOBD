#Created by kiddo122

import RPi.GPIO as GPIO
import math
import os
import IOBDModeDict
import IOBDPIDDict

def IReadOBDStream():
	#TODO: get I/O stream from firmware and spit out readable data
	#TODO: Create IOBDPacket class.

	return IOBDPacket

def IGetMode(IOBDPacket):
	#TODO: determine mode of opperation for OBD output i.e. ISO-15765
	#TODO: Create IOBDMode class.

	return IOBDMode

def IGetOBDInfo(IOBDPacket)
	#TODO: Determine the inforom the OBD Stream
	#TODO: Create IOBDInfo Class.

	return IOBDInfo

def ISendOBDMessage(IPIDPacket):
	#TODO: Send PIDs to request messages from OBD/CANbus

	return 

def IConstructPIDMessage(PIDID, IOBDMode)
	#TODO: Construct message packet to send to OBD

	return IOBDPacket