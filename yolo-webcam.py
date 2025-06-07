import cv2
from ultralytics import YOLO

cap = cv2.VideoCapture(0)

# Load the YOLO11 model montagem tomada
model = YOLO("C:\\Users\\unfin\\Downloads\\yolo11n.pt")

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Run YOLO11 inference on the frame
    results = model(frame)

    # Visualize the results on the frame
    annotated_frame = results[0].plot()
    max_area = 0

    for i in results[0].boxes:
        box_num = results[0].boxes[i-1].xyxy.numpy()[0]
        area = abs(box_num[0] - box_num[2]) * abs(box_num[1] - box_num[3])
        if max_area < area:
            max_area = area
    # print(results[0].tojson())
    # Display the resulting frame
    cv2.imshow("Camera", annotated_frame)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) == ord("q"):
        break

# Release resources and close windows
cv2.destroyAllWindows()