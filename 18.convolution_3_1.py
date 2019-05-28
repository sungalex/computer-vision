# blur color image

import cv2 as cv
import numpy as np


def filter_gray(img, kernel, border_type):

	kh, kw = kernel.shape[0:2]
	kh2, kw2 = kh//2, kw//2

	tmp_shape = list(img.shape)
	tmp_shape[0] += (kh2*2)
	tmp_shape[1] += (kw2*2)

	tmp = np.zeros(tmp_shape, img.dtype)
	np.copyto(tmp[kh2:kh2+img.shape[0], kw2:kw2+img.shape[1]], img)

	if border_type == 1:
		tmpH, tmpW = tmp.shape
		tmp[0        : kh2 ] = tmp[kh2]
		tmp[tmpH-kh2 : tmpH] = tmp[tmpH-kh2-1]
		tmp[:, 0        : kw2 ] = tmp[:, kw2        : kw2+1   ]
		tmp[:, tmpW-kw2 : tmpW] = tmp[:, tmpW-kw2-1 : tmpW-kw2]

	#cv.imshow('tmp', tmp)
	#cv.waitKey()

	dst = np.zeros(img.shape, img.dtype)

	for i in range(dst.shape[0]):
		for j in range(dst.shape[1]):
			dst[i,j] = (tmp[i:i+kh, j:j+kw] * kernel).sum()

	return dst


def filter(img, kernel, border_type=0):
	channels = cv.split(img)
	channels_filtered = []
	for channel in channels:
		channels_filtered.append(filter_gray(channel, kernel, border_type))
	img_filtered = cv.merge(channels_filtered)
	return img_filtered


img = cv.imread('filter_blur.jpg', cv.IMREAD_COLOR)
ksize = 9
kernel = np.full((ksize,ksize), 1./(ksize*ksize))
img_filtered = filter(img, kernel, 1)

cv.imshow('original', img)
cv.imshow('filtered', img_filtered)
cv.waitKey()