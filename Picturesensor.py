import cv2
image = cv2.imread("C:\\Users\\maker\\Documents\\GitHub\\ball_picker_robot\\pictures\\IMG_6443.png")
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

cv2.namedWindow(Window)
cv2.namedWindow(Mask)
height, width = image.shape[:2]
image = cv2.resize(image, (int(0.1*width), int(0.1*height)), interpolation=cv2.INTER_AREA)
low_H = 55
low_S = 165
low_V = 0
high_H = 109
high_S = 255
high_V = 170

cv2.createTrackbar(low_H_name, Mask, low_H, 188, on_low_H_thresh_trackbar)
cv2.createTrackbar(high_H_name, Mask, high_H, 188, on_high_H_thresh_trackbar)
cv2.createTrackbar(low_S_name, Mask, low_S, 255, on_low_S_thresh_trackbar)
cv2.createTrackbar(high_S_name, Mask, high_S, 255, on_high_S_thresh_trackbar)
cv2.createTrackbar(low_V_name, Mask, low_V, 255, on_low_V_thresh_trackbar)
cv2.createTrackbar(high_V_name, Mask, high_V, 255, on_high_V_thresh_trackbar)

cv2.imshow(Window, image)
while True:
    frame_threshold = cv2.inRange(image, (low_H, low_S, low_V), (high_H, high_S, high_V))
    cv2.imshow(Mask, frame_threshold)
    key = cv2.waitKey(30)
    if key == ord('q') or key == 27:
        break
# cv2.waitKey(0)
cv2.destroyAllWindows()
