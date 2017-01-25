from location.location import Location
import abc

class IGPSDevice(abc.ABC):
    """Abstract GPS device"""

    @abc.abstractmethod
    def initialize(self):
    	pass

    @abc.abstractproperty
    def status(self) -> bool:
        pass

    @abc.abstractmethod
    def read_location(self) -> Location:
        """Retrieve data from the GPS and return a Location"""
        pass
