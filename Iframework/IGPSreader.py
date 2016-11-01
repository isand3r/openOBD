#Created by kiddo122

import RPi.GPIO as GPIO
import math
import os

def IReadGPSStream():
	#TODO: get I/O stream from firmware and spit out readable data
	#TODO: Create IOBDPacket class.

	return IGPSPacket

def IGetGPSInfo(IGPSPacket)
	#TODO: Determine the inforom the OBD Stream
	#TODO: Create IOBDInfo Class.

	return IGPSInfo

def ISendGPSMessage(IGPSPacket):
	#TODO: Send PIDs to request messages from OBD/CANbus

	return IGPSStream

def IGPSCalculation(IGPSPacket)
	#TODO: Construct GPS long,lat from IGPSPacket

	return IGPSCoord

def IGPSAvgCalculation(IGPSPacket)
	#TODO: Construct AVG GPS long,lat from IGPSPacket

	return IGPSCoord