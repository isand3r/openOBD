#Created by kiddo122

import RPi.GPIO as GPIO
import math
import os

def IReadGPSStream(GPSStream):
	#TODO: get I/O stream from firmware and spit out readable data
	#TODO: Create IOBDPacket class.

	return IGPSPacket


def ISendGPSMessage(IGPSRequest):
	#TODO: Send request to get messages from GPS
	#TODO: Create IPIDPacket

	return 

def ICalculateLocation(IGPSPacket):
	#TODO: parse packet and do trianglation

	return IGPSLocation

def ICalculateAvgLocation(IGPSPacket):
	#TODO: parse packet and do trianglation with average location

	return IGPSLocation
