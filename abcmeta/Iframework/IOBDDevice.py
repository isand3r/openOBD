import abc

class IOBDDevice(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def initialize(self) :
        """TODO"""
        return

    @abc.abstractmethod
    def sendOBDFrame(self) :
        """TODO"""
        return

    @abc.abstractmethod
    def printOBDStream(self) :
        """TODO"""
        return
