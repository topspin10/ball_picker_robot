'''
debugger command line: 

cd /home/wonwong/Projects/ball_picker_robot ; /usr/bin/env /home/wonwong/Projects/ball_picker_robot/env/bin/python /home/wonwong/.vscode/extensions/ms-python.debugpy-2025.8.0-linux-arm64/bundled/libs/debugpy/adapter/../../debugpy/launcher 48501 -- /home/wonwong/Projects/ball_picker_robot/yolo-picam.py

regular command line: 

/home/wonwong/Projects/ball_picker_robot/env/bin/python /home/wonwong/Projects/ball_picker_robot/yolo-picam.py

'''

import cv2
import numpy
from ultralytics import YOLO
from picamera2 import Picamera2
from datetime import datetime

picam2 = Picamera2()
config = picam2.create_still_configuration(main={"size": (4608, 2592)})
picam2.configure(config)
cap = cv2.VideoCapture(0)
# link to YOLO documentation: https://docs.ultralytics.com/reference/cfg/__init__/#ultralytics.cfg.check_cfg
# Load the YOLO11 model montagem tomada
model = YOLO("/home/wonwong/Downloads/yolo11n.pt") # REMEMBER: change file path depending on device
picam2.start()

while True:
    # Capture frame-by-frame as fast as it can
    filename = "pictures/" + datetime.now().strftime("%Y%m%d_%H%M%S") + ".jpg"
    picam2.capture_file(filename)

    # Run YOLO11 inference on the frame
    # TODO: uncomment lines 29 and 30. replace the stuff in model with the path to filename 
    results = model([f"/home/wonwong/Projects/ball_picker_robot/pictures/IMG_6442.png"])

    # Visualize the results on the frame
    annotated_frame = results[0].plot()
    max_area = 0
    box_num = 0
    max_box_num = 0
    good_box_num = 0
    # IMPORTANT NOTES: to find the label of the boxes look inside 0 of results for boxes then for CLS not ID. confidence is CONF: cls for sports ball is 32
    # TODO: add if statement to check if the boxes' CLS is 32 and the CONF is over 50 percent
    for i in results[0].boxes:
        if i.cls == 32:
            if i.conf > 0.5:
                box = i.xyxy.numpy()[0]
                area = abs(box[0] - box[2]) * abs(box[1] - box[3])
                if max_area < area:
                    max_area = area
                    max_box_num = box_num
                good_box_num = good_box_num + 1
        box_num = box_num + 1
    # Display the resulting frame
    cv2.imshow("Camera", annotated_frame)
    print(max_area, max_box_num, box_num)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) == ord("q"):
        break

# Release resources and close windows
cv2.destroyAllWindows()
