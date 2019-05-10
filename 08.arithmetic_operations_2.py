# blend two images with various weights

import cv2

img0 = cv2.imread('add1.jpg', cv2.IMREAD_COLOR)
img1 = cv2.imread('add2.jpg', cv2.IMREAD_COLOR)

cv2.imshow('img0', img0)
cv2.imshow('img1', img1)
cv2.waitKey()
cv2.destroyAllWindows()

num_images = 5

for i in range(num_images):
	w0 = i/(num_images-1)
	w1 = 1 - w0
	img = cv2.addWeighted(img0, w0, img1, w1, 0)
	cv2.imshow('img', img)
	cv2.waitKey()