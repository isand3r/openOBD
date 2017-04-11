from location.location import Location
from gps.igpsdevice import IGPSDevice
#from gps3 import gps3
import os
import datetime
import serial
import time

class GPS3Device(IGPSDevice):
    """Concrete GPS device using gps3"""

    def __init__(self):
        self.location = None
        self.longitude = None
        self.latitude = None
        self.altitude = None
        self.modem = None
        self.GPSStatus = None
        #self.gps_socket = None
        #self.data_stream = None
        self._ready = False

    def initialize(self):
        self.modem = serial.Serial("/dev/ttyAMA0", baudrate=115200)
        powerup = "AT+CGNSPWR=1\r"
        self.modem.write(powerup.encode())
        self.modem.readline()
        self.GPSStatus = self.modem.readline()
        time.sleep(2)
        #os.system('sudo gpsd /dev/ttyAMA0 -F /var/run/gpsd.sock')
        #self.gps_socket = gps3.GPSDSocket()
        #self.data_stream = gps3.DataStream()
        #self.gps_socket.connect()
        #self.gps_socket.watch()
        self._ready = True

    @property
    def status(self) -> bool:
        return self._ready

    def getDataStream(self):
        request = "AT+CGNSINF\r"
        self.modem.write(request.encode())
        self.modem.readline()
        data = self.modem.readline().decode()
        if data.startswith("+CGNSINF"):
            data = data.split(",")
            print(data)
            if data[3]=='':
                print ("GPS Error")
            else:
                #Latitude ±dd.dddddd [-90.000000,90.000000]
                self.latitude = data[3].strip()
                #Longitude ±ddd.dddddd [-180.000000,180.000000]
                self.longitude = data[4].strip()
                #Altitude 0-120m
                self.altitude = data[5].strip()

    def read_location(self) -> Location:
        """Return the same location each time"""
        self.getDataStream()
        while(self.longitude == None):
            self.getDataStream()
        time = datetime.datetime.now()
        self.location = Location(float(self.latitude), float(self.longitude), float(self.altitude), time)
        return self.location
