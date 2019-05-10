# Add two images

import cv2

img0 = cv2.imread('add1.jpg', cv2.IMREAD_COLOR)
img1 = cv2.imread('add2.jpg', cv2.IMREAD_COLOR)

cv2.imshow('img0', img0)
cv2.imshow('img1', img1)
cv2.imshow('numpy_add', img0 + img1)
cv2.imshow('opencv_add', cv2.add(img0, img1))
cv2.waitKey()