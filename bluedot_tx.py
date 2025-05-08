from bluedot import BlueDot
import time
import serial

ser = serial.Serial('/dev/ttyACM1')  # open serial port
cmd = None
def send_dir(pos):
    # pos.distance is a float from 0 to 1.
    cmd = f'{int(pos.distance*100)}, {int(pos.angle)}'
    ser.write(cmd.encode('ascii'))

dot = BlueDot()
dot.when_moved = send_dir

while True:
    time.sleep(0.3)
