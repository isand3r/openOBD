"""TODO Abstract GPS device"""

import abc

class IGPSDevice(metaclass=abc.ABCMeta):

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
