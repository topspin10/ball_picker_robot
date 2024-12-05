import cv2
# image = cv2.imread("C:\\Users\\maker\\Documents\\GitHub\\ball_picker_robot\\pictures\\IMG_6442.png")
image = cv2.imread("C:\\Users\\maker\\Pictures\\IMG_6442.png")
print(type(image))
Window = 'window'
Mask = 'mask'
cv2.namedWindow(Window)
cv2.namedWindow(Mask)
height, width = image.shape[:2]
image = cv2.resize(image, (int(0.1*width), int(0.1*height)), interpolation=cv2.INTER_AREA)
low_H = 30
low_S = 70
low_V = 0
high_H = 40
high_S = 255
high_V = 255
frame_threshold = cv2.inRange(image, (low_H, low_S, low_V), (high_H, high_S, high_V))

cv2.imshow(Window, image)
cv2.imshow(Mask, frame_threshold)
cv2.waitKey(0)
cv2.destroyAllWindows()
