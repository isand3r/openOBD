import abc

class ITemperature(metaclass=abc.ABCMeta)

    # return the temperature value
    @abc.abstractmethod
    def getValue() :
    	return

    # return the time of the measurement
    @abc.abstractmethod
    def getTime() :
    	return
