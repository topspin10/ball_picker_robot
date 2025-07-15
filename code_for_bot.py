from picamera2 import Picamera2
import sys
import serial
import time
from datetime import datetime
from ultralytics import YOLO
# "model" is the what i'm going to run on the pictures i take.
model = YOLO("/home/wonwong/Downloads/yolo11n.pt") # REMEMBER: change file path depending on device
# "results" is the list of images that have been run through YOLO
results = []
num = 12
#TODO specify what num is
'''
input: command ('t, num: direction', 'at, num: angle, num: number of times', or 'm, num: speed, num: direction')
output: nothing
'''


def command_sender(*args):
    global ser
    success = True
    cmd = ','.join(map(str, args))
    num_of_tries = 0
    while num_of_tries < 4:
        try:
            if not success:
                # Question for coach: the code works, but I don't know how is ACM defined within this function?
                ser = serial.Serial(ACM,timeout=1)
            ser.write(f'{cmd}\n'.encode('ascii'))
            start = time.time_ns()
            """wait for cmd DONE at most 15 seconds"""
            response = f"{cmd} DONE"
            while time.time_ns() - start < 15000000001:
                received_response = ser.readline()
                if received_response[0] == response:
                    global rotation 
                    rotation = received_response[1]
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
# Question for coach: what is "main"? Is it a keyword arg or a variable?
config = picam2.create_still_configuration(main={"size": (4608, 2592)})
picam2.configure(config)
picam2.start()
max_area = 0
max_pic_num = 0
for p in range(num):
    # t = turn ; m = move
    command_sender('at', 360/num, p)
    # rotation is in DEGREES
    filename = f"/home/wonwong/Projects/data/{rotation}.jpg"#do you need to save it
    pic = picam2.capture_file(filename)
    # Run YOLO11 inference on the frame
    results.append(model(pic))
    print(p)
print("done")
picam2.stop()
for n in range(num):
    for i in results[n][0].boxes:
        if i.cls == 32:#repalce 32 with an enumeration BALL=32
            if i.conf > .5:#also this should become a parameter
                box = i.xyxy.numpy()[0]#insert links to the documentation that explains the format of i.xyxy
                area = abs(box[0] - box[2]) * abs(box[1] - box[3])
                if max_area < area:
                    max_area = area
                    max_pic_num = n
    pic_num = pic_num + 1
print(max_area, max_pic_num)
command_sender('t', max_pic_num * 30)#should use the gyro (didn't we talk about getting the gyro info back from the hub), think about an absolute reference to avoid accumulating errors
