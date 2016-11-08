import abc

class ITemperature(metaclass=abc.ABCMeta)

    # return the temperature value
    @abc.abstractmethod
    def getValue() :
    	raise NotImplementedError

    # return the time of the measurement
    @abc.abstractmethod
    def getTime() :
    	raise NotImplementedError
