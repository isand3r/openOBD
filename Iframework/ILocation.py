from abc import ABCMeta

class ILocation(metaclass=ABCMeta):

    @abstractmethod
    def getLatitude() : raise NotImplementedError

    @abstractmethod
    def getLongitude() : raise NotImplementedError

    @abstractmethod
    def getTime() : raise NotImplementedError

    @abstractmethod
    def getAccuracy() : raise NotImplementedError    

