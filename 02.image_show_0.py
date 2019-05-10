import cv2

img = cv2.imread('image/cat.jpg', cv2.IMREAD_UNCHANGED)
cv2.imshow('img', img)
#cv2.waitKey()

img1 = cv2.imread('image/cat.jpg')
cv2.imshow('img1', img)
cv2.waitKey()
