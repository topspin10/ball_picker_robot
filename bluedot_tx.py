from bluedot import BlueDot
import time
import serial

ser = serial.Serial('/dev/ttyACM1')  # open serial port; port name may change if you disconnect
cmd = None

def send_dir(pos):
    # pos.distance is a float from 0 to 1.
    cmd = f'{int(pos.distance*100)}, {int(pos.angle)}\n' # REMEMBER: \n is CRITICAL. Vex hub NEEDS it.
    # print(cmd)
    ser.write(cmd.encode('ascii'))

dot = BlueDot()
dot.when_moved = send_dir

while True:
    time.sleep(0.3)
