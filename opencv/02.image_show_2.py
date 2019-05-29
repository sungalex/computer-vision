# show image until 'esc' gets pressed

import cv2

img = cv2.imread('image/cat.jpg', cv2.IMREAD_UNCHANGED)

while True:
	cv2.imshow('img', img)
	key = cv2.waitKey(30)
	if key == 27: break
