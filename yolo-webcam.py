import cv2
from ultralytics import YOLO

cap = cv2.VideoCapture(0)
# link to YOLO documentation: https://docs.ultralytics.com/reference/cfg/__init__/#ultralytics.cfg.check_cfg
# Load the YOLO11 model montagem tomada
model = YOLO("C:\\Users\\unfin\\Downloads\\yolo11n.pt")

while True:
    # Capture frame-by-frame as fast as it can
    ret, frame = cap.read()

    # Run YOLO11 inference on the frame
    results = model(frame)

    # Visualize the results on the frame
    annotated_frame = results[0].plot()
    max_area = 0
    box_num = 0
    for i in results[0].boxes:
        box = i.xyxy.numpy()[0]
        area = abs(box[0] - box[2]) * abs(box[1] - box[3])
        if max_area < area:
            max_area = area
            max_box_num = box_num
        box_num = box_num + 1
    # Display the resulting frame
    cv2.imshow("Camera", annotated_frame)
    print(max_area)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) == ord("q"):
        break

# Release resources and close windows
cv2.destroyAllWindows()
