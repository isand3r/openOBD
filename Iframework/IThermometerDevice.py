import abc

class IThermometerDevice(metaclass=abc.ABCMeta):

	@abc.abstractmethod
	def initialize() :
		raise NotImplementedError

	# check that the device is available and able to provide temperature measurements
	@abc.abstractmethod
	def getStatus() :
		raise NotImplementedError

	# create a new ITemperature
	@abc.abstractmethod
	def getTemperature() :
		raise NotImplementedError