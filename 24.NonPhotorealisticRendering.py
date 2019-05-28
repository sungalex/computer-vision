import cv2 as cv
import numpy as np

def on_ep_change(_):
	sigma_s = cv.getTrackbarPos('sigma_s', 'edge_preserved')
	sigma_r = cv.getTrackbarPos('sigma_r', 'edge_preserved') * 0.01
	print('edge_preserved: sigma_s, sigma_r =', sigma_s, sigma_r)
	dst = cv.edgePreservingFilter(img, sigma_s=sigma_s, sigma_r=sigma_r)
	cv.imshow('edge_preserved', dst)

def on_de_change(_):
	sigma_s = cv.getTrackbarPos('sigma_s', 'detail_enhanced')
	sigma_r = cv.getTrackbarPos('sigma_r', 'detail_enhanced') * 0.01
	print('detail_enhanced: sigma_s, sigma_r =', sigma_s, sigma_r)
	dst = cv.detailEnhance(img, sigma_s=sigma_s, sigma_r=sigma_r)
	cv.imshow('detail_enhanced', dst)

def on_ps_change(_):
	sigma_s = cv.getTrackbarPos('sigma_s', 'pencil_sketch')
	sigma_r = cv.getTrackbarPos('sigma_r', 'pencil_sketch') * 0.01
	print('pencil_sketch: sigma_s, sigma_r =', sigma_s, sigma_r)
	dst_gray, dst_color = cv.pencilSketch(img, sigma_s=sigma_s, sigma_r=sigma_r)
	cv.imshow('pencil_sketch', dst_color)
	cv.imshow('pencil_sketch_gray', dst_gray)

def on_st_change(_):
	sigma_s = cv.getTrackbarPos('sigma_s', 'stylization')
	sigma_r = cv.getTrackbarPos('sigma_r', 'stylization') * 0.01
	print('stylization: sigma_s, sigma_r =', sigma_s, sigma_r)
	dst = cv.stylization(img, sigma_s=sigma_s, sigma_r=sigma_r)
	cv.imshow('stylization', dst)


cv.namedWindow('edge_preserved')
cv.createTrackbar('sigma_s', 'edge_preserved', 60, 60, on_ep_change)
cv.createTrackbar('sigma_r', 'edge_preserved', 40, 100, on_ep_change)

cv.namedWindow('detail_enhanced')
cv.createTrackbar('sigma_s', 'detail_enhanced', 10, 60, on_de_change)
cv.createTrackbar('sigma_r', 'detail_enhanced', 15, 100, on_de_change)

cv.namedWindow('pencil_sketch')
cv.createTrackbar('sigma_s', 'pencil_sketch', 60, 60, on_ps_change)
cv.createTrackbar('sigma_r', 'pencil_sketch', 20, 100, on_ps_change)

cv.namedWindow('stylization')
cv.createTrackbar('sigma_s', 'stylization', 60, 60, on_st_change)
cv.createTrackbar('sigma_r', 'stylization', 45, 100, on_st_change)

img = cv.imread('red-and-green-leavs-of-autumn-jpg.jpg')

cv.imshow('img', img)
on_ep_change(0)
on_de_change(0)
on_ps_change(0)
on_st_change(0)
cv.waitKey()