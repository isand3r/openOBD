import RPi.GPIO as GPIO
import math
import os
import IOBDModeDict

def IReadOBDStream():
	#TODO: get I/O stream from firmware and spit out readable data
	#TODO: Create IOBDPacket class.

	return IOBDPacket

def IDetermineMode():
	#TODO: determine mode of opperation for OBD output i.e. ISO-15765
	#TODO: Create IOBDMode class

	return IOBDMode

def ISendOBDMessage():
	#TODO: Send PIDs to request messages from OBD/CANbus
	#TODO: Create IPIDPacket

	return IPIDPacket
