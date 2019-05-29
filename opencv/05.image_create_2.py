# create an image with green rectangle inside

import cv2
import numpy as np

h = 480
w = 640

img = np.zeros((h,w,3), dtype=np.uint8)

img[h*1//3:h*2//3,w*1//3:w*2//3] = (0,255,0)

cv2.imshow('img',img)
cv2.waitKey()