import numpy as np
import cv2 as cv
import Step1 as St1
import Step2 as St2

# newimage = 'newimage'
# cv.namedWindow(newimage)
image = cv.imread("C:\\Users\\maker\\Documents\\GitHub\\ball_picker_robot\\pictures\\IMG_6443.png")
output_1 = St1.color_based_ball_detector(image)
# output_1 = cv.resize(output_1, None, fx=0.1, fy=0.1)
# # cv.imshow(newimage, output_1)
# # image = cv.resize(image, None, fx=0.1, fy=0.1)
# # output_2 = Dp.circle_based_ball_detector(image)
#
# cv.imshow(newimage, output_1)
#
# key = cv.waitKey(0)
bob = St2.direction_decider(output_1)
print(bob)
