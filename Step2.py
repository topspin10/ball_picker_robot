import cv2 as cv
import Step1 as S1

# image = cv.imread("C:\\Users\\maker\\Documents\\GitHub\\ball_picker_robot\\pictures\\IMG_6443.png")
# image = cv.imread("C:\\Users\\unfin\\OneDrive\\Documents\\GitHub\\ball_picker_robot\\pictures\\IMG_6443.png")


def direction_decider(image):
    """in: output of step 1 - out: number between -1 and 1"""
    image = cv.resize(image, None, fx=0.1, fy=0.1)
    cv.namedWindow('full image')
    cv.imshow('full image', image)
    # image = image[:2142].shape
    # print(image)
    cv.namedWindow('part image')
    height, length, c = image.shape
    height = height // 2
    image_2 = image[height:]
    length = length // 10
    for bob in range(10):
        image_3 = image_2[:, length * bob:length * (bob + 1)]
        cv.imshow('part image', image_3)
        cv.waitKey(0)
