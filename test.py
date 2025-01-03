import numpy as np
import cv2 as cv
import Directionprovider

newimage = 'newimage'
cv.namedWindow(newimage)
image = cv.imread("C:\\Users\\maker\\Documents\\GitHub\\ball_picker_robot\\pictures\\IMG_6443.png")
output = Directionprovider.color_based_ball_detector(image)
output = cv.resize(output, None, fx=0.1, fy=0.1)
cv.imshow(newimage, output)

key = cv.waitKey(0)
