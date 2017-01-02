"""Abstract configuration file parser for openOBD"""

import abc

class IConfiguration(abc.ABC):

	@abc.abstractmethod
	def read(self, filename: str):
		"""Read the given configuration file"""
		pass

	@abc.abstractproperty
	def gps(self) -> str:
		pass

	@abc.abstractproperty
	def thermo(self) -> str:
		pass
