import cv2
import numpy as np

def color_based_ball_detector(image):
    '''input = image
    output = black and white version of the image'''
    low_H = 55
    low_S = 165
    low_V = 0
    high_H = 109
    high_S = 255
    high_V = 170
    erosion_shape = cv2.MORPH_RECT
    erosion_size = 1
    kernel = cv2.getStructuringElement(erosion_shape, (2 * erosion_size + 1, 2 * erosion_size + 1),(erosion_size, erosion_size))
    output_1 = cv2.inRange(image, (low_H, low_S, low_V), (high_H, high_S, high_V))
    output_2 = cv2.erode(output_1, kernel)
    output_3 = cv2.dilate(output_2, kernel, iterations=10)
    _, length = image.shape
    if length >= 400 then:
        
    return output_3

def circle_based_ball_detector(image):
    '''input = image
    output = black and white version of the image'''
    input = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    output_1 = cv2.HoughCircles(input, cv2.HOUGH_GRADIENT, 2, 200, minRadius=50, maxRadius=500)
    # measured thing. closest ball diameter is 500
    if output_1 is not None:
        output_1 = np.uint16(np.around(output_1))
        for i in output_1[0, :]:
            center = (i[0], i[1])
            radius = i[2]
            cv2.circle(image, center, radius, (255, 255, 255), -1)

    return image
