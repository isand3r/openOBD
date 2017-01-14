from location.location import Location
from gps.igpsdevice import IGPSDevice
from gps3 import gps3
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

    def initialize(self):
        self.gps_socket = gps3.GPSDSocket()
        self.data_stream = gps3.DataStream()
        self.gps_socket.connect()
        self.gps_socket.watch()

    def getLocation(self):
        return self.location

    def getAltitude(self):
        return self.location['altitude']

    def getLatitude(self):
        return self.location['latitude']

    def getLongitude(self):
        return self.location['longitude']

    def getDataStream(self):
        for new_data in self.gps_socket:
            if(new_data):
                self.data_stream.unpack(new_data)
                self.longitude = self.data_stream.TPV['lon']
                self.latitude = self.data_stream.TPV['lat']
                self.altitude = self.data_stream.TPV['alt']
                return

    def read_location(self) -> Location:
        """Return the same location each time"""
        time = datetime.datetime.now()
        self.location = Location(self.latitude, self.longitude, self.altitude, time)
        return self.location

            
            

