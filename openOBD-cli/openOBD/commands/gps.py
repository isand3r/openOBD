"""The gps command."""

from gps3 import gps3
import sys
import time
from .base import Base
import os

class GPS(Base):
    def __init__(self, options):
        super(GPS, self).__init__(options)
        self.location = {'longitude' : 0, 'latitude' : 0, 'altitude' : 0}
        self.gps_socket = None
        self.data_stream = None

    def init(self):
        self.gps_socket = gps3.GPSDSocket()
        self.data_stream = gps3.DataStream()
        self.gps_socket.connect()
        self.gps_socket.watch()

    def IgetAltitude(self):
        return self.location['altitude']

    def IgetLatitude(self):
        return self.location['latitude']

    def IgetLongitude(self):
        return self.location['longitude']

    def IgetLocation(self):
        return self.location

    def IreadGPSStream(self):
        if new_data in self.gps_socket:
            self.data_stream.unpack(new_data)
            location = {'longitude' : self.data_stream.TPV['lon'], 'latitude' : self.data_stream.TPV['lat'], 'altitude' : self.data_stream.TPV['alt']}
            self.location  = location
            print "Location:" + str(self.location)   

    def run(self):
        print "GPS Running..."
        while(1):
            self.IreadGPSStream()
            time.sleep(1) 



        

