# Canny edge detector

import cv2 as cv
import numpy as np

img = cv.imread('edge_test1.jpg', cv.IMREAD_COLOR)

# thresh2 is recommended to be 2~3 times of thresh1
thresh1, thresh2 = 50, 120

# the order of thresh1 and thresh2 is irrelevant
edge = cv.Canny(img, thresh1, thresh2)

cv.imshow('img', img)
cv.imshow('edge', edge)
cv.waitKey()