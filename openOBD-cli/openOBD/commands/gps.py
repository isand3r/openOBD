"""The gps command."""

from gps3 import gps3
import sys
import time
from .base import Base
import os

class GPS(Base):
    def __init__(self, options):
        super(GPS, self).__init__(options)
        self.location = {}
        self.longitude =  0
        self.latitude = 0
        self.altitude = 0
        self.gps_socket = gps3.GPSDSocket()
        self.data_stream = gps3.DataStream()

    def init(self):
        self.gps_socket.connect()
        self.gps_socket.watch()

    def IgetAltitude(self):
        for new_data in gps_socket:
            if new_data:
                data_stream.unpack(new_data)
                self.altitude = data_stream.TPV['alt']

    def IgetLatitude(self):
        for new_data in gps_socket:
            if new_data:
                data_stream.unpack(new_data)
                self.latitude =  data_stream.TPV['lat']

    def IgetLongitude(self):
        for new_data in gps_socket:
            if new_data:
                data_stream.unpack(new_data)
                self.longitude = data_stream.TPV['long']

    def IgetLocation(self):
        for new_data in gps_socket:
            if new_data:
                data_stream.unpack(new_data)
                self.longitude = data_stream.TPV['long']
                self.latitude = data_stream.TPV['lat']
                self.altitude = data_stream.TPV['alt']
        location = {'longitude' : self.longitude, 'latitude' : self.latitude, 'altitude' : self.altitude}
        self.location  = location

    def run(self):
        print "GPS Running..."
        self.init()
        while(1):
            print "Location:" + str(self.IgetLocation())
            print "Longitude:" + str(self.IgetLongitude())
            print "Latitude:" + str(self.IgetLatitude())
            print "Altitude:" + str(self.IgetAltitude())
            time.sleep(1)


        

