"""Abstract configuration file parser for openOBD"""

import abc

class IConfiguration(abc.ABC):

	@abc.abstractmethod
	def read(self, filename):
		"""Read the given configuration file"""
		pass

	@abc.abstractproperty
	def gps(self):
		pass

	@abc.abstractproperty
	def thermo(self):
		pass
