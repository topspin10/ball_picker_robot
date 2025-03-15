from picamera import PiCamera
import time
import cv2 as cv
# TODO need to resize images before you save them and save them using a distinct name
# TODO put this code into startup sequence
bob = []

while True:
    camera = PiCamera()
    time.sleep(2)
    bill = camera.capture("/home/pi/Pictures/img.jpg")
    bobby = cv2.resize(image, (int(0.1*width), int(0.1*height)), interpolation=cv2.INTER_AREA)
    bob.append(bobby)
    print("Done.")
    time.sleep(5)
