from picamera import PiCamera
import time

while True:
    camera = PiCamera()
    time.sleep(2)
    camera.capture("/home/pi/Pictures/img.jpg")
    print("Done.")
    time.sleep(5)
