import abc 

class ILocation(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def getLatitude() :
        raise NotImplementedError

    @abc.abstractmethod
    def getLongitude() :
         raise NotImplementedError

    @abc.abstractmethod
    def getTime() :
         raise NotImplementedError

    @abc.abstractmethod
    def getAccuracy() :
        raise NotImplementedError    

