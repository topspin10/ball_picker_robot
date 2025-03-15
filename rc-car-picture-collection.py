from picamera import PiCamera
import time
# TODO need to resize images before you save them and save them using a distinct name
# TODO put this code into startup sequence

while True:
    camera = PiCamera()
    time.sleep(2)
    camera.capture("/home/pi/Pictures/img.jpg")
    print("Done.")
    time.sleep(5)
