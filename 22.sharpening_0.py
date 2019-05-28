import cv2 as cv
import numpy as np

img = cv.imread('filter_blur.jpg')

weight = 5
img_blurred = cv.GaussianBlur(img, (5,5), 0)
img_sharpened = cv.addWeighted(img, weight+1, img_blurred, -weight, 0)

cv.imshow('img', img)
cv.imshow('img_blurred', img_blurred)
cv.imshow('img_sharpened', img_sharpened)
cv.waitKey()