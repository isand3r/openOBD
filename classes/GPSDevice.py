from gps3 import gps3
import sys
sys.path.append('.././')
import openobd.Iframework.IGPSDevice
from IGPSDevice import IGPSDevice
import os

class myGPSDevice(IGPS):
	def__init__(self):
		self.location = {}
		self.longtitude = 0
		self.latitude = 0
		self.altitude = 0
		self.gps_socket
		self.data_stream

	def init(self):
		self.gps_socket = gps3.GPSDSocket()
		self.data_stream = gps3.DataStream()
		self.gps_socket.connect()
		self.gps_socket.watch()

	def IgetAltitude(self):
	for new_data in gps_socket:
		try:
    	if new_data:
       		data_stream.unpack(new_data)
        	self.altitude = data_stream.TPV['alt']
        except Exception: e
        	return errorstatus()

    def errorstatus():
     	print "GPS not connected"

    def checkStatus(self):
    	return self

    def IgetLatitude(self)
	for new_data in gps_socket:
    	if new_data:
       		data_stream.unpack(new_data)
        	self.latitude =  data_stream.TPV['lat']

    def IgetLongtitude(self)
	for new_data in gps_socket:
    	if new_data:
       		data_stream.unpack(new_data)
        	self.longtitude = data_stream.TPV['long']

    def IgetLocation(self)
		for new_data in gps_socket:
    	if new_data:
       		data_stream.unpack(new_data)
        	longtitude = data_stream.TPV['long']
        	latitude = data_stream.TPV['lat']
        	altitude = data_stream.TPV['alt']

		location = {'longtitude' : longtitude, 'latitude' : latitude, 'altitude' : altitude}

		self.location  = location

