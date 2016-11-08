import abc

class IGPSDevice(metaclass=abc.ABCMeta):

	@abc.abstractmethod
	def initialize() :
		raise NotImplementedError

	# check that the device is available, connected, and able to provide location data
	@abc.abstractmethod
	def getStatus() :
		raise NotImplementedError

	# create a new ILocation
	@abc.abstractmethod
	def getLocation() :
		raise NotImplementedError
