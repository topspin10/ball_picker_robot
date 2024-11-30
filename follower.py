from __future__ import print_function
import cv2 as cv

low_H = 30
low_S = 70
low_V = 0
high_H = 40
high_S = 255
high_V = 255
window_capture_name = 'Video Capture'
window_detection_name = 'Object Detection'

cap = cv.VideoCapture(0)
cv.namedWindow(window_capture_name)
cv.namedWindow(window_detection_name)

while True:
    ret, frame = cap.read()
    if frame is None:
        break
    frame_HSV = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    frame_threshold = cv.inRange(frame_HSV, (low_H, low_S, low_V), (high_H, high_S, high_V))

    cv.imshow(window_capture_name, frame)
    cv.imshow(window_detection_name, frame_threshold)

    key = cv.waitKey(30)
    if key == ord('q') or key == 27:
        break

# Import required packages:
import cv2

# Load the image and convert it to grayscale:
image = cv2.imread("test_image.png")
# sets a variable to a file containing an image
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#

# Apply cv2.threshold() to get a binary image
ret, thresh = cv2.threshold(gray_image, 50, 255, cv2.THRESH_BINARY)

# Find contours:
im, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

# Draw contours:
cv2.drawContours(image, contours, 0, (0, 255, 0), 2)

# Calculate image moments of the detected contour
M = cv2.moments(contours[0])

# Print center (debugging):
print("center X : '{}'".format(round(M['m10'] / M['m00'])))
print("center Y : '{}'".format(round(M['m01'] / M['m00'])))

# Draw a circle based centered at centroid coordinates
cv2.circle(image, (round(M['m10'] / M['m00']), round(M['m01'] / M['m00'])), 5, (0, 255, 0), -1)

# Show image:
cv2.imshow("outline contour & centroid", image)

# Wait until a key is pressed:
cv2.waitKey(0)

# Destroy all created windows:
cv2.destroyAllWindows()
