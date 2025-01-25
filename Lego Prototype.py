import cv2 as cv
import Step1 as S1
import Step2 as S2

cam = cv.VideoCapture(0)
while True:
    _, pic = cam.read()
    # TODO: improve functions, resize images to 400 length
    # TODO: set threshold, set default
    black_white = S1.color_based_ball_detector(pic)
    direction = S2.direction_decider(black_white)
    print(direction)
