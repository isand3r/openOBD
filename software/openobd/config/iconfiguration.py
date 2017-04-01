"""Abstract configuration file parser for openOBD"""
import abc

class IConfiguration(abc.ABC):

	@abc.abstractmethod
	def read(self, filename: str):
		"""Read the given configuration file"""
		pass

	@abc.abstractproperty
	def manager_moving_average_items(self) -> int:
		pass

	@abc.abstractproperty
	def manager_print_interval(self) -> int:
		pass

	@abc.abstractproperty
	def obd_device(self) -> str:
		pass

	@abc.abstractproperty
	def rpm_interval(self) -> str:
		pass

	@abc.abstractproperty
	def speed_interval(self) -> str:
		pass

	@abc.abstractproperty
	def gps_device(self) -> str:
		pass

	@abc.abstractproperty
	def gps_interval(self) -> str:
		pass

	@abc.abstractproperty
	def thermo_device(self) -> str:
		pass

	@abc.abstractproperty
	def thermo_interval(self) -> str:
		pass

	@abc.abstractproperty
	def accel_device(self) -> str:
		pass

	@abc.abstractproperty
	def accel_interval(self) -> str:
		pass

	@abc.abstractproperty
	def baro_device(self) -> str:
		pass

	@abc.abstractproperty
	def baro_interval(self) -> str:
		pass

	@abc.abstractproperty
	def volt_device(self) -> str:
		pass

	@abc.abstractproperty
	def volt_interval(self) -> str:
		pass
