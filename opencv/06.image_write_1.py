# read color image as gray and save it as jpg

import cv2

img = cv2.imread('cat.jpg', cv2.IMREAD_GRAYSCALE)

cv2.imshow('img',img)
cv2.waitKey()

cv2.imwrite('img.jpg', img)
