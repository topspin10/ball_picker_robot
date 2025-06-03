from picamera2 import Picamera2
import sys
import serial
import time
from datetime import datetime


def command_sender(*args):
    global ser
    success = True
    cmd = ','.join(map(str, args))
    num_of_tries = 0
    while num_of_tries < 4:
        try:
            if not success:
                ser = serial.Serial(ACM)
            # print(d, a)
            ser.write(f'{cmd}\n'.encode('ascii'))
            # TODO wait for okay
            while ser.readlines() == None:
                time.sleep(0.1)
            # TODO wait for done to make sure the vex robot has turned (consider waiting a max amount of secs)
            while ser.readlines() == None:
                time.sleep(0.1)
            break
        except:
            success = False
        num_of_tries = num_of_tries + 1

picam2 = Picamera2()
picam2.start()
ACM = sys.argv[1]
ser = serial.Serial(ACM)  # open serial port; port name may change if you disconnect
for p in range(12):
    command_sender('t', 30)
    time.sleep(3)
    config = picam2.create_still_configuration(main={"size": (4608, 2592)})
    picam2.configure(config)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"/home/wonwong/Projects/data/{timestamp}.jpg"
    picam2.capture_file(filename)
