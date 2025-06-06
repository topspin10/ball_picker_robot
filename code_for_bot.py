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
                ser = serial.Serial(ACM,timeout=1)
            # print(d, a)
            ser.write(f'{cmd}\n'.encode('ascii'))
            start = time.time_ns()
            """wait for cmd DONE at most 5 seconds"""
            response = f"{cmd} DONE"
            while time.time_ns()-start < 15000000001:
                received_response = ser.readline()
                if received_response == response:
                    break
                else:
                    print(f'received_response: {received_response}')
            print(time.time_ns() - start)
            break
        except:
            success = False
        num_of_tries = num_of_tries + 1

picam2 = Picamera2()
ACM = sys.argv[1]
ser = serial.Serial(ACM,timeout=1)  # open serial port; port name may change if you disconnect
config = picam2.create_still_configuration(main={"size": (4608, 2592)})
picam2.configure(config)
picam2.start()
for p in range(12):
    command_sender('t', 30)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"/home/wonwong/Projects/data/{timestamp}.jpg"
    picam2.capture_file(filename)
    print(p)
print("done")
picam2.stop()
