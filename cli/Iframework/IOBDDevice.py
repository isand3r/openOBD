import abc

class IOBDDevice(metaclass=abc.ABCMeta):

@abc.abstractmethon
    IInitializeOBD(self) :
    """Retrieve data from the GPS and return altitude."""
        return

    @abc.abstractmethod
    def IReadOBDStream(self) : 
    	"""Retrieve data from the GPS and return altitude."""
    	return

    @abc.abstractmethod
    def IGetMode(self) : 
    	"""Retrieve data from the GPS and return latitude."""
    	return

    @abc.abstractmethod
    def ISendOBDMessage(self) :
    	"""Retrieve data from the GPS and return longtitude."""
    	return