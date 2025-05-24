from picamera2 import Picamera2
import sys
import serial

ACM = sys.argv[1]
ser = serial.Serial(ACM)  # open serial port; port name may change if you disconnect
ser.write('1'.encode('ascii'))
