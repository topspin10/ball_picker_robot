import numpy as np
import cv2 as cv
import Directionprovider as dp

newimage = 'newimage'
cv.namedWindow(newimage)
image = cv.imread("C:\\Users\\maker\\Documents\\GitHub\\ball_picker_robot\\pictures\\IMG_6443.png")
# output_1 = dp.color_based_ball_detector(image)
# output_1 = cv.resize(output_1, None, fx=0.1, fy=0.1)
# cv.imshow(newimage, output_1)
image = cv.resize(image, None, fx=0.1, fy=0.1)
output_2 = dp.circle_based_ball_detector(image)

cv.imshow(newimage, output_3)

# key = cv.waitKey(0)
