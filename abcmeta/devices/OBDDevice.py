"""TODO Implementation of IOBDDevice"""
import abc
from ../Iframework/IOBDDevice import IOBDDevice
import spidev
import RPi.GPIO as GPIO
import sys
import time
import os

class OBDDevice(IOBDDevice):
    def __init__(self):
        self.spi = spidev.SpiDev()
        self.mode = None
        self.pid = None
        self.mcp2515 = bytes([0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00])
        self.buff = bytes([0x02, 0x01, 0x05, 0x00, 0x00, 0x00, 0x00, 0x00])
        self.recv = bytes([0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00])

    def initialize():
        self.spi.open(0, 0)
        self.spi.max_speed_hz = 500000
        self.spi.writebytes(self.mcp2515)

    def sendOBDFrame(self):
        self.spi.writebytes(self.buff)

    def printOBDStream(self):
        self.recv = self.spi.readbytes(8)
        print("OBD:", self.recv)
