import cv2
image = cv2.imread("C:\\Users\\maker\\Documents\\GitHub\\ball_picker_robot\\pictures\\IMG_6443.png")
# C:\Users\unfin\OneDrive\Documents\GitHub\ball_picker_robot\pictures\IMG_6442.png"
#"C:\\Users\\maker\\Documents\\GitHub\\ball_picker_robot\\pictures\\IMG_6442.png"
#image = cv2.imread("C:\\Users\\maker\\Pictures\\IMG_6442.png")
print(type(image))
low_H_name = 'Low H'
low_S_name = 'Low S'
low_V_name = 'Low V'
high_H_name = 'High H'
high_S_name = 'High S'
high_V_name = 'High V'
Window = 'window'
Mask = 'mask'
Erode = 'erode'
findcontour = 'findcontour'

def on_low_H_thresh_trackbar(val):
    global low_H
    global high_H
    low_H = val
    low_H = min(high_H-1, low_H)
    cv2.setTrackbarPos(low_H_name, Mask, low_H)

def on_high_H_thresh_trackbar(val):
    global low_H
    global high_H
    high_H = val
    high_H = max(high_H, low_H+1)
    cv2.setTrackbarPos(high_H_name, Mask, high_H)

def on_low_S_thresh_trackbar(val):
    global low_S
    global high_S
    low_S = val
    low_S = min(high_S-1, low_S)
    cv2.setTrackbarPos(low_S_name, Mask, low_S)

def on_high_S_thresh_trackbar(val):
    global low_S
    global high_S
    high_S = val
    high_S = max(high_S, low_S+1)
    cv2.setTrackbarPos(high_S_name, Mask, high_S)

def on_low_V_thresh_trackbar(val):
    global low_V
    global high_V
    low_V = val
    low_V = min(high_V-1, low_V)
    cv2.setTrackbarPos(low_V_name, Mask, low_V)

def on_high_V_thresh_trackbar(val):
    global low_V
    global high_V
    high_V = val
    high_V = max(high_V, low_V+1)
    cv2.setTrackbarPos(high_V_name, Mask, high_V)


cv2.namedWindow(findcontour)
cv2.namedWindow(Window)
cv2.namedWindow(Mask)
cv2.namedWindow(Erode)
height, width = image.shape[:2]
image = cv2.resize(image, (int(0.1*width), int(0.1*height)), interpolation=cv2.INTER_AREA)
low_H = 55
low_S = 165
low_V = 0
high_H = 109
high_S = 255
high_V = 170
erosion_shape = cv2.MORPH_RECT
erosion_size = 1
kernel = cv2.getStructuringElement(erosion_shape, (2 * erosion_size + 1, 2 * erosion_size + 1),(erosion_size, erosion_size))
# title_trackbar_element_shape = 'Element:\n 0: Rect \n 1: Cross \n 2: Ellipse'
# frame_threshold = cv2.inRange(image, (low_H, low_S, low_V), (high_H, high_S, high_V))
# cv2.imshow(Mask, frame_threshold)
# src = "C:\\Users\\maker\\Documents\\GitHub\\ball_picker_robot\\pictures\\IMG_6443.png"
# erosion_size = 0
# max_elem = 2
# max_kernel_size = 21
# title_trackbar_element_shape = 'Element:\n 0: Rect \n 1: Cross \n 2: Ellipse'
# title_trackbar_kernel_size = 'Kernel size:\n 2n +1'
# element =

cv2.createTrackbar(low_H_name, Mask, low_H, 188, on_low_H_thresh_trackbar)
cv2.createTrackbar(high_H_name, Mask, high_H, 188, on_high_H_thresh_trackbar)
cv2.createTrackbar(low_S_name, Mask, low_S, 255, on_low_S_thresh_trackbar)
cv2.createTrackbar(high_S_name, Mask, high_S, 255, on_high_S_thresh_trackbar)
cv2.createTrackbar(low_V_name, Mask, low_V, 255, on_low_V_thresh_trackbar)
cv2.createTrackbar(high_V_name, Mask, high_V, 255, on_high_V_thresh_trackbar)
# cv2.createTrackbar(title_trackbar_element_shape, Erode, 0, max_elem, erosion)


while True:
    frame_threshold = cv2.inRange(image, (low_H, low_S, low_V), (high_H, high_S, high_V))
    cv2.imshow(Mask, frame_threshold)
    # def morph_shape(val):
    #     if val == 0:
    #         return cv2.MORPH_RECT
    #     elif val == 1:
    #         return cv2.MORPH_CROSS
    #     elif val == 2:
    #         return cv2 .MORPH_ELLIPSE
    # def erosion(val):
    #     erosion_size = cv2.getTrackbarPos(title_trackbar_kernel_size, Erode)
    #     erosion_shape = morph_shape(cv2.getTrackbarPos(title_trackbar_element_shape, Erode))
    #
    #     element = cv2.getStructuringElement(erosion_shape, (2 * erosion_size + 1, 2 * erosion_size + 1),
    #                                        (erosion_size, erosion_size))
    #
    #     erosion_dst = cv2.erode(src, element)
    #     cv2.imshow(Erode, erosion_dst)

    # erosion("C:\\Users\\maker\\Documents\\GitHub\\ball_picker_robot\\pictures\\IMG_6443.png")



    eroded = cv2.dilate(frame_threshold, kernel,iterations = 2)
    cv2.imshow(Erode, eroded)
    contours,_ = cv2.findContours(eroded, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    print(contours)
    cv2.drawContours(image, contours, -1, (0, 255, 0), -1)
    cv2.imshow(findcontour, image)

    # cv2.imshow(findcontour, contour)
    key = cv2.waitKey(0)
    if key == ord('q') or key == 27:
        break
# cv2.waitKey(0)
cv2.destroyAllWindows()
