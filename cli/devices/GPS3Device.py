"""A concrete GPS device class for the Nov 15 meeting"""
from gps3 import gps3
import sys
import time
import os

class GPS3Device():
    def __init__(self):
        self.location = {'longitude' : 0, 'latitude' : 0, 'altitude' : 0}
        self.gps_socket = None
        self.data_stream = None

    def initialize(self):
        self.gps_socket = gps3.GPSDSocket()
        self.data_stream = gps3.DataStream()
        self.gps_socket.connect()
        self.gps_socket.watch()

    def getAltitude(self):
        return self.location['altitude']

    def getLatitude(self):
        return self.location['latitude']

    def getLongitude(self):
        return self.location['longitude']

    def getLocation(self):
        return self.location

    def printGPSStream(self):
        for new_data in self.gps_socket:
            if(new_data):
                self.data_stream.unpack(new_data)
                location = {'longitude' : self.data_stream.TPV['lon'], 'latitude' : self.data_stream.TPV['lat'], 'altitude' : self.data_stream.TPV['alt']}
                self.location  = location
                print("Location:" + str(self.location))
                return
            
            

