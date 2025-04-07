import time

import cv2 as cv

Bob = 'Bob'
cv.namedWindow(Bob)
image = cv.imread("C:\\Users\\maker\\Documents\\GitHub\\ball_picker_robot\\data\\Images\\IMG_6442.png")
height, width = image.shape[:2]
image = cv.resize(image, (int(0.1*width), int(0.1*height)), interpolation=cv.INTER_AREA)
print(image)
cv.imshow(Bob, image)
cv.waitKey(0)
cv .destroyAllWindows()
