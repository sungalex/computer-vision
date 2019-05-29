# Image sharpening with a trackbar

import cv2 as cv
import numpy as np


def onChangeKernelSize(val):
	global half_ksize, weight
	half_ksize = val
	print('half ksize, weight =', half_ksize, weight)
	smoothed = cv.GaussianBlur(img, (half_ksize*2+1, half_ksize*2+1), 0)
	sharpened = cv.addWeighted(img, weight+1, smoothed, -weight, 0)
	cv.imshow('sharpened', sharpened)


def onChangeWeight(val):
	global half_ksize, weight
	weight = val/10
	print('half_ksize, weight =', half_ksize, weight)
	smoothed = cv.GaussianBlur(img, (half_ksize*2+1, half_ksize*2+1), 0)
	sharpened = cv.addWeighted(img, weight+1, smoothed, -weight, 0)
	cv.imshow('sharpened', sharpened)


img = cv.imread('filter_blur.jpg', cv.IMREAD_COLOR)

half_ksize = 2
weight = 2.5
cv.namedWindow('sharpened')
cv.createTrackbar('ksize/2', 'sharpened', half_ksize, 5, onChangeKernelSize)
cv.createTrackbar('weight*10', 'sharpened', int(weight*10), 70, onChangeWeight)

smoothed = cv.GaussianBlur(img, (half_ksize*2+1, half_ksize*2+1), 0)
sharpened = cv.addWeighted(img, weight + 1, smoothed, -weight, 0)

cv.imshow('img', img)
cv.imshow('sharpened', sharpened)
cv.waitKey()