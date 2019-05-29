# blur gray image with border type

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

	# 원본 이미지의 가장자리를 상, 하, 좌, 우 남는 영역에 복사해 넣음
	if border_type == 1:
		tmpH, tmpW = tmp.shape
		tmp[0        : kh2 ] = tmp[kh2] # top
		tmp[tmpH-kh2 : tmpH] = tmp[tmpH-kh2-1] # bottom
		tmp[:, 0        : kw2 ] = tmp[:, kw2        : kw2+1   ] # left
		tmp[:, tmpW-kw2 : tmpW] = tmp[:, tmpW-kw2-1 : tmpW-kw2] # right

	cv.imshow('tmp', tmp)
	cv.waitKey()

	dst = np.zeros(img.shape, img.dtype)

	for i in range(dst.shape[0]):
		for j in range(dst.shape[1]):
			dst[i,j] = (tmp[i:i+kh, j:j+kw] * kernel).sum()

	return dst


img = cv.imread('filter_blur.jpg', cv.IMREAD_GRAYSCALE)
ksize = 9
kernel = np.full((ksize,ksize), 1./(ksize*ksize))
img_filtered = filter_gray(img, kernel, 1)

cv.imshow('original', img)
cv.imshow('filtered', img_filtered)
cv.waitKey()