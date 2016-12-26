import abc

class IGPSDevice(abc.ABC):
    """Abstract GPS device"""

    @abc.abstractmethod
    def initialize(self):
    	"""Initialize the device"""
    	return

    @abc.abstractmethod
    def getStatus(self):
        """Return the whether the device is ready"""
        return

    @abc.abstractmethod
    def getLocation(self):
    	"""Retrieve data from the GPS and return a Location"""
    	return
