import cv2 as cv
import Step1 as S1
import Step2 as S2
import numpy as np

image = cv.imread("C:\\Users\\maker\\Documents\\GitHub\\ball_picker_robot\\pictures\\IMG_6443.png")
image = cv.resize(image, None, fx=0.1, fy=0.1)
cv.namedWindow('full image')
cv.imshow('full image', image)
# image = image[:2142].shape
# print(image)
# cv.namedWindow('part image')
# height, length, c = image.shape
# height = height//2
# image_2 = image[height:]
# length = length//10
# for bob in range(10):
#     image_3 = image_2[:,length*bob:length*(bob+1)]
#     cv.imshow('part image', image_3)
#     cv.waitKey(0)
Bob = S1.color_based_ball_detector(image)
cv.namedWindow('Black and White image')
cv.imshow('Black and White image', Bob)

cv.waitKey(0)
