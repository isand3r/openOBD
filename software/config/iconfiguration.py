"""Abstract configuration file parser for openOBD"""

import abc

class IConfiguration(abc.ABC):

	# read the given configuration file
	@abc.abstractmethod
	def read(self, filename):
		pass

	# return the gps to use
	@abc.abstractproperty
	def gps(self):
		pass

	# return the thermometer to use
	@abc.abstractproperty
	def thermo(self):
		pass
