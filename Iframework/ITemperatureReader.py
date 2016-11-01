#Created by kiddo122

import RPi.GPIO as GPIO
import math
import os
import ITemperatureDict

def IReadStream():
	#TODO: get I/O stream from firmware and spit out readable data
	#TODO: Create ITemperaturePacket class.

	return IGPSPacket

def IGetTemperatureInfo(ITemperaturePacket)
	#TODO: Determine the inforom the TEMP Stream
	#TODO: Create ITEMPInfo Class.

	return ITemperatureInfo

def ISendTemperatureMessage(ITemperaturePacket):
	#TODO: Send message to Temperature sensor

	return ITemperatureStream

def ITemperatureCalculation(ITemperaturePacket)
	#TODO: get one temperature reading

	return ITemperature

def ITemperatureAvgCalculation(ITemperaturePacket)
	#TODO: get average temperature reading for set time length

	return ITemperature

def ITemperatureIOConvert(ITemperaturePacket, ITemperatureUnit)
	#TODO: convert bit stream to readable temp either in  Celsius or Feirenheit