import cv2 as cv
import Directionprovider as Dp

image = cv.imread("C:\\Users\\maker\\Documents\\GitHub\\ball_picker_robot\\pictures\\IMG_6443.png")
image = cv.imread("C:\\Users\\unfin\\OneDrive\\Documents\\GitHub\\ball_picker_robot\\pictures\\IMG_6443.png")


def direction_decider(image):
    """in: output of step 1 - out: number between -1 and 1"""
    a,b,c =image.shape
    a=a/2
    b=b/2


