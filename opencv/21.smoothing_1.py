# gaussianBlur with a trackbar

import cv2 as cv
import numpy as np


def onChangeSigmaX(val):
	global sigma_x, sigma_y
	sigma_x = max(val, 0.01)
	print('sigma_x, sigma_y =', sigma_x, sigma_y)
	smoothed = cv.GaussianBlur(img, (0,0), sigmaX=sigma_x, sigmaY=sigma_y)
	cv.imshow('smoothed', smoothed)


def onChangeSigmaY(val):
	global sigma_x, sigma_y
	sigma_y = max(val, 0.01)
	print('sigma_x, sigma_y =', sigma_x, sigma_y)
	smoothed = cv.GaussianBlur(img, (0,0), sigmaX=sigma_x, sigmaY=sigma_y)
	cv.imshow('smoothed', smoothed)


img = cv.imread('filter_blur.jpg', cv.IMREAD_COLOR)

sigma_x, sigma_y = 3, 3
cv.namedWindow('smoothed')
cv.createTrackbar('sigmax', 'smoothed', sigma_x, 10, onChangeSigmaX)
cv.createTrackbar('sigmay', 'smoothed', sigma_y, 10, onChangeSigmaY)

smoothed = cv.GaussianBlur(img, (0,0), sigmaX=sigma_x, sigmaY=sigma_y)

cv.imshow('img', img)
cv.imshow('smoothed', smoothed)
cv.waitKey()