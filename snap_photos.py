#!/usr/bin/env python3

from picamera2 import Picamera2
import time
import cv2 as cv
from datetime import datetime
# TODO need to resize images before you save them and save them using a distinct name
# TODO put this code into startup sequence

def main():
    picam2 = Picamera2()

    config = picam2.create_still_configuration(main={"size": (4608, 2592)})
    picam2.configure(config)

    picam2.start()
    n = 0

    try:
        # take photos for 2 minutes, 5 seconds interval
        while n < 25:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"/home/wonwong/Projects/data/{timestamp}.jpg"

            picam2.capture_file(filename)
            print(f"Captured {filename}")

            time.sleep(5)
            n = n + 1
    except KeyboardInterrupt:
        print("Stopping capture loop.")
    finally:
        picam2.close()

if __name__ == "__main__":
    main()
