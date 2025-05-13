from bluedot import BlueDot
import time
import serial

ser = serial.Serial('/dev/ttyACM2')  # open serial port; port name may change if you disconnect
# success = 0

# The functions below sends commands to the serial port
# input: commands
# output: nothing
def stop():
    # while success == 0:
    try:
        ser.write('0, 0\n'.encode('ascii'))
    except:
        ser = serial.Serial('/dev/ttyACM2')
        ser.write('0, 0\n'.encode('ascii'))
        # else:
        #     success = 1


def send_dir(pos):
    # pos.distance is a float from 0 to 1.
    cmd = f'{int(pos.distance*100)}, {int(pos.angle)}\n' # REMEMBER: \n is CRITICAL. Vex hub NEEDS it.
    # print(cmd)
    # while success == 0:
    try:
        ser.write(cmd.encode('ascii'))
    except:
        ser = serial.Serial('/dev/ttyACM2')
        ser.write(cmd.encode('ascii'))
        # else:
        #     success = 1

dot = BlueDot()
dot.when_pressed = send_dir
dot.when_moved = send_dir
dot.when_released = stop

while True:
    time.sleep(0.3)
