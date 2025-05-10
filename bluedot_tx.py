from bluedot import BlueDot
import time
import serial

ser = serial.Serial('/dev/ttyACM1')  # open serial port; port name may change if you disconnect

# The functions below sends commands to the serial port
# input: commands
# output: nothing
def stop():
    ser.write('0, 0\n'.encode('ascii'))

def send_dir(pos):
    # pos.distance is a float from 0 to 1.
    cmd = f'{int(pos.distance*100)}, {int(pos.angle)}\n' # REMEMBER: \n is CRITICAL. Vex hub NEEDS it.
    # print(cmd)
    ser.write(cmd.encode('ascii'))

dot = BlueDot()
dot.when_pressed = send_dir
dot.when_moved = send_dir
dot.when_released = stop

while True:
    time.sleep(0.3)
