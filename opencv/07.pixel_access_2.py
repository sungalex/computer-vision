# set all red channels to 0

import cv2

img = cv2.imread('cat.jpg', cv2.IMREAD_UNCHANGED)

img[:,:,2] = 0

cv2.imshow('img',img)
cv2.waitKey()