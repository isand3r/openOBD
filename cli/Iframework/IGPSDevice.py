import abc

class IGPSDevice(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def IgetAltitude(self) : 
    	"""Retrieve data from the GPS and return altitude."""
    	return

    @abc.abstractmethod
    def IgetLatitude(self) : 
    	"""Retrieve data from the GPS and return latitude."""
    	return

    @abc.abstractmethod
    def IgetLongtitude(self) :
    	"""Retrieve data from the GPS and return longtitude."""
    	return

    @abc.abstractmethod
    def IgetLocation(self) :
    	"""Retrieve data from the GPS and return location."""
    	return
    
    