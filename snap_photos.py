from picamera2 import Picamera2
import time
import cv2 as cv
from datetime import datetime
# TODO need to resize images before you save them and save them using a distinct name
# TODO put this code into startup sequence

def main():
    picam2 = Picamera2()

    config = picam2.create_still_configuration(main={"size": (800, 800)})
    picam2.configure(config)

    picam2.start()
    
    try:
        while True:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"{timestamp}.jpg"

            picam2.capture_file(filename)
            print(f"Captured {filename}")

            time.sleep(5)
    except KeyboardInterrupt:
        print("Stopping capture loop.")
    finally:
        picam2.close()

if __name__ == "__main__":
    main()
