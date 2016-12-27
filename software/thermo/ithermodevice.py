import abc

class IThermometerDevice(abc.ABC):

	@abc.abstractmethod
	def initialize(self):
		pass

	# check that the device is available and able to provide temperature measurements
	@abc.abstractproperty
	def ready(self):
		pass
		
	# create a new ITemperature
	@abc.abstractmethod
	def readTemperature(self):
		pass
