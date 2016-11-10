import sys
sys.path.append('.././')
import openobd.Iframework.IOBDDevice
import serial

class OBDDevice:
	def__init__(self, OBDStandard):
		threading.Thread.__init__(self)
		self.port
		self.pid = 0
		self.mode = 0
		self.stream = "" 

	def IInitializeOBD(self):
		self.port = serial.Serial("/dev/ttyAMA0", baudrate=1000000, timeout=3.0)

	def IReadOBDStream(self):
	#TODO: get I/O stream from firmware and spit out readable data
	recieved = ""
    while True:
        char = self.port.read()
        recieved += char
        if char =='\r' or char=='':
            self.stream = recieved

	def IGetMode(self):
	#TODO: determine mode of opperation for OBD output i.e. ISO-15765

		self.IOBDMode = mode

	def ISendOBDMessage(self, msg):
		#TODO: Send PIDs to request messages from OBD/CANbus
		OBDrequest = self.mode + self.pid + msg
		port.write(OBDrequest)