import cv2 as cv
import Step1 as S1
import numpy as np

# image = cv.imread("C:\\Users\\maker\\Documents\\GitHub\\ball_picker_robot\\pictures\\IMG_6443.png")
# image = cv.imread("C:\\Users\\unfin\\OneDrive\\Documents\\GitHub\\ball_picker_robot\\pictures\\IMG_6443.png")


def direction_decider(image):
    """in: output of step 1 - out: number between -1 and 1"""
    # image = cv.resize(image, None, fx=0.1, fy=0.1)
    w_bins = 10
    h_bins = 2
    output_1 = (w_bins-1)/2
    top_slice = 0
    threshold = 100
    # cv.namedWindow('full image')
    # cv.imshow('full image', image)
    # image = image[:2142].shape
    # print(image)
    # cv.namedWindow('part image')
    height, length = image.shape
    height = height // h_bins
    image_2 = image[height:]
    length = length // w_bins
    output = 0
    for slice in range(w_bins):
        image_3 = image_2[:, length * slice:length * (slice + 1)]
        white_pixel = np.sum(image_3 == 255)
        if top_slice < white_pixel:
            if white_pixel >= threshold
                top_slice = white_pixel
                output_1 = slice

        # cv.imshow('part image', image_3)
        # cv.waitKey(0)

    output_2 = output_1/((w_bins-1)/2)-1
    return output_2
