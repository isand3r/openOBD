import openobd as obd
import temp as temp
from Iframework.IGPSDevice import IGPSDevice
from Iframework.IOBDDevice import IOBDDevice
from classes.GPSDevice import GPSDevice
from classes.OBDDevice import OBDDevice

def GPSthread(IGPSDevice):
	IGPS.IgetLocation()
	IGPS.IgetLontitude()
	IGPS.IgetLatitude()
	IGPS.IgetAltitude()

def OBDthread(IOBDDevice):
	OBDDevice.IReadOBDStream()
	OBDDevice.IGetMode()

def main():
	device_list = {}
	#Initialize the Devices
	GPSDevice = myGPSDevice()
	OBDDevice = myOBDDevice()

	#Wait for userRequest
	while(userRequest(device_list) == None)


	thread = Thread(target = OBDthread(OBDDevice))
    thread2 = Thread(target = GPSthread(GPSDevice))

    thread.start();
    thread2.start();
    thread.join();
    thread2.join();

def userRequest(device_list):
	print('[Usage]: <devicename> [all, obd, gps, temp, accell] \n Please enter Device you want to look at: ')
	buf = input()
	device_list = buf
	return 	buf

if __name__ == "__main__":
    main() 