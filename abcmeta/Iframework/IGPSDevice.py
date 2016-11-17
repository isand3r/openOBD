"""TODO Abstract GPS device"""

import abc

class IGPSDevice(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def initialize(self) :
    	"""TODO"""
    	return

    @abc.abstractmethod
    def getLocation(self) :
    	"""Retrieve data from the GPS and return location."""
    	return


    @abc.abstractmethod
    def getAltitude(self) :
    	"""TODO necessary? Retrieve data from the GPS and return altitude."""
    	return

    @abc.abstractmethod
    def getLatitude(self) :
    	"""TODO necessary? Retrieve data from the GPS and return latitude."""
    	return

    @abc.abstractmethod
    def getLongtitude(self) :
    	"""TODO necessary? Retrieve data from the GPS and return longtitude."""
    	return

    @abc.abstractmethod
    def printGPSStream(self) :
    	"""TODO this class should not print?"""
    	return
