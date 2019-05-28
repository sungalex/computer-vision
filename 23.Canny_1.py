# Canny edge detector with a trackbar

import cv2 as cv
import numpy as np


def onChangeThresh1(val):
	global thresh1, thresh2
	thresh1 = val
	print('thresh1, thresh2 =', thresh1, thresh2)
	edge = cv.Canny(img, thresh1, thresh2)
	cv.imshow('edge', edge)


def onChangeThresh2(val):
	global thresh1, thresh2
	thresh2 = val
	print('thresh1, thresh2 =', thresh1, thresh2)
	edge = cv.Canny(img, thresh1, thresh2)
	cv.imshow('edge', edge)


img = cv.imread('edge_test1.jpg', cv.IMREAD_COLOR)

thresh1 = 50
thresh2 = 120
cv.namedWindow('edge')
cv.createTrackbar('thresh1', 'edge', thresh1, 255, onChangeThresh1)
cv.createTrackbar('thresh2', 'edge', thresh2, 255, onChangeThresh2)

edge = cv.Canny(img, thresh1, thresh2)

cv.imshow('img', img)
cv.imshow('edge', edge)
cv.waitKey()