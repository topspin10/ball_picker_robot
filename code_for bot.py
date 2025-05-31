from picamera2 import Picamera2
import sys
import serial
import time
from datetime import datetime


def command_sender(*args):
    global ser
    success = True
    cmd = ','.join(map(str, args))
    while True:
        # TODO only try to connect again a certain amount of times
        try:
            if not success:
                ser = serial.Serial(ACM)
            # print(d, a)
            ser.write(f'{cmd}\n'.encode('ascii'))
            # TODO wait for okay
            # TODO wait for done to make sure the vex robot has turned (consider waiting a max amount of secs
            break
        except:
            success = False

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
