from picamera2 import Picamera2
import sys
import serial
import time
from datetime import datetime

picam2 = Picamera2()
picam2.start()
ACM = sys.argv[1]
ser = serial.Serial(ACM)  # open serial port; port name may change if you disconnect
while not p < 13:
    ser.write('30\n'.encode('ascii'))
    time.sleep(3)
    config = picam2.create_still_configuration(main={"size": (4608, 2592)})
    picam2.configure(config)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"/home/wonwong/Projects/data/{timestamp}.jpg"
    picam2.capture_file(filename)
    p = p + 1
