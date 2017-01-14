from location.location import Location
from gps.igpsdevice import IGPSDevice
from gps3 import gps3
import os
import datetime

class GPS3Device(IGPSDevice):
    """Concrete GPS device using gps3"""

    def __init__(self):
        self.location = None
        self.longitude = None
        self.latitude = None
        self.altitude = None
        self.gps_socket = None
        self.data_stream = None
        self._ready = False

    def initialize(self):
        os.system('sudo gpsd /dev/ttyAMA0 -F /var/run/gpsd.sock')
        self.gps_socket = gps3.GPSDSocket()
        self.data_stream = gps3.DataStream()
        self.gps_socket.connect()
        self.gps_socket.watch()
        self._ready = True

    @property
    def status(self) -> bool:
        return self._ready

    def getDataStream(self):
        for new_data in self.gps_socket:
            if(new_data):
                self.data_stream.unpack(new_data)
                self.longitude = self.data_stream.TPV['lon']
                self.latitude = self.data_stream.TPV['lat']
                self.altitude = self.data_stream.TPV['alt']

    def read_location(self) -> Location:
        """Return the same location each time"""
        self.getDataStream()
        print(self.longitude)
        ?*if(self.longitude == 'n/a'):
    """ self.longitude = 0.0
        if(self.latitude == 'n/a'):
            self.latitude = 0.0
        if(self.altitude == 'n/a'):
            self.altitude = 0.0
        print(self.longitude)"""
        time = datetime.datetime.now()
        self.location = Location(float(self.latitude), float(self.longitude), float(self.altitude), time)
        return self.location

            
            

