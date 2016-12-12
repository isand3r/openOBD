class MockGPSDevice(IGPSDevice):
    """Mock GPS Device"""

    def initialize(self) :
    	"""This mock GPS device does not need to be initialized"""
    	return

    def getStatus(self):
        """This mock device is always ready"""
        print("MockGPSDevice getStatus not implemented")

    def getLocation(self) :
    	"""Retrieve data from the GPS and return location."""
    	print("MockGPSDevice getLocation not implemented")
