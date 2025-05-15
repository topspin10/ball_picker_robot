from bluedot import BlueDot
import time
import serial

ACM = '/dev/ttyACM1'
ser = serial.Serial(ACM)  # open serial port; port name may change if you disconnect

# input: command
# output: None


def command_sender(d, a):
    success = True
    while True:
        try:
            if not success:
                ser = serial.Serial(ACM)
            ser.write(f'{d}, {a}\n'.encode('ascii'))
            break
        except:
            success = False

# The functions below sends commands to the serial port
# input: commands
# output:


def stop():
    command_sender(0, 0)



def send_dir(pos):
    # pos.distance is a float from 0 to 1.
    d = {int(pos.distance*100)}
    a = {int(pos.angle)}
    command_sender(d, a)

dot = BlueDot()
dot.when_pressed = send_dir
dot.when_moved = send_dir
dot.when_released = stop

while True:
    time.sleep(0.3)
