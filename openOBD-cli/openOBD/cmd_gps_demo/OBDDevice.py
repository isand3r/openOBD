"""The OBD command."""

import spidev
import sys
import time
import os

class OBDDevice():
    def __init__(self):
        self.spi = spidev.SpiDev()
        self.mode = None
        self.pid = None
        self.buff = bytes([0x02, 0x01, 0x05, 0x00, 0x00, 0x00, 0x00, 0x00])
        self.recv = bytes([0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00])

    def initialize():
        self.spi.open(0, 0)
        self.spi.max_speed_hz = 500000

    def sendOBDFrame(self):
        self.spi.writebytes(buff)

    def printOBDStream(self):
        self.recv = self.spi.readbytes(8)
        print("OBD:", self.recv)



        

