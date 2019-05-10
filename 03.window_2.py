# control the window position with arrow keys using cv2.waitKeyEx

import cv2

arrowL = 2424832
arrowR = 2555904
arrowU = 2490368
arrowD = 2621440
delta = 10
xpos = 500
ypos = 500

img = cv2.imread('cat.jpg', cv2.IMREAD_UNCHANGED)

cv2.namedWindow('img')

while True:
	cv2.moveWindow('img', xpos, ypos)
	cv2.imshow('img', img)
	key = cv2.waitKeyEx(30)

	if key == 27: break
	elif key == arrowL: xpos -= delta
	elif key == arrowR: xpos += delta
	elif key == arrowU: ypos -= delta
	elif key == arrowD: ypos += delta
