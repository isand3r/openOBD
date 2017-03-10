import abc

class IDeviceCollection(abc.ABC):

	@abc.abstractmethod
	def __init__(self, thermoDevice: IThermoDevice,
		gpsDevice: IGPSDevice, accelDevice: IAccelDevice, obdDevice: IOBDDevice):

	@abc.abstractmethod
	def read_current_data(self, message: str) -> Measure:
		pass

	@abc.abstractmethod
	def init_devices(self, self.devicelist):
		pass