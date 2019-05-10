# diagonally gradient image

import cv2
import numpy as np

s = 500

img = np.zeros((s,s), dtype=np.uint8)

for i in range(s):
	for j in range(s):
		img[i,j] = (i+j)*255//(s+s)

cv2.imshow('img', img)
cv2.waitKey()