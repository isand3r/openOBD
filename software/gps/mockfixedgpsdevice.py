from software.location.location import Location
from software.gps.igpsdevice import IGPSDevice
import datetime

class MockFixedGPSDevice(IGPSDevice):
    """Mock GPS Device with that reads a fixed location"""
    def __init__(self):
        self.MOCK_LATITUDE_VALUE = 49
        self.MOCK_LONGITUDE_VALUE = -123
        self.MOCK_ALTITUDE_VALUE = 70
        self._status = False

    def initialize(self):
        self._status = True

    @property
    def status(self) -> bool:
        return self._status

    def read_location(self) -> Location:
        """Return the same location each time"""
        time = datetime.datetime.now()
        vancouver_location = Location(self.MOCK_LATITUDE_VALUE,
            self.MOCK_LONGITUDE_VALUE, self.MOCK_ALTITUDE_VALUE, time)
        return vancouver_location
