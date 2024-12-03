import cv2
# image = cv2.imread("C:\\Users\\maker\\Documents\\GitHub\\ball_picker_robot\\pictures\\IMG_6442.png")
image = cv2.imread("C:\\Users\\maker\\Pictures\\IMG_6442.png")
print(type(image))
Window = 'window'
cv2.namedWindow(Window)
height, width = image.shape[:2]
width = width/2
height = height/2
resized_image = cv2.resize(image, (width/2, height/2), interpolation = cv2.INTER_CUBIC)
cv2.imshow(Window, image)
cv2.waitKey(0)
cv2.destroyAllWindows()
