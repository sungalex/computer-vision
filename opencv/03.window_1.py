# increase the image size incrementally keeping the aspect ratio and the center position

import cv2

img = cv2.imread('cat.jpg', cv2.IMREAD_UNCHANGED)
img_rows, img_cols = img.shape[0:2]
aspect_ratio = img_cols / img_rows

cv2.namedWindow('img', cv2.WINDOW_NORMAL)
height = 100

for i in range(10):
	width = aspect_ratio * height
	cv2.moveWindow('img', int(1920/2-width/2), int(1080/2-height/2))
	cv2.resizeWindow('img', int(width), int(height))
	cv2.imshow('img', img)
	cv2.waitKey(500)
	height *= 1.2
