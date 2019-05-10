# detect mouse clicks and wheel scroll up and down

import cv2


def on_mouse(event, x, y, flags, param):
	if event == cv2.EVENT_LBUTTONDOWN:
		print('Left mouse button down at', x, y)
	elif event == cv2.EVENT_LBUTTONUP:
		print('Left mouse button up at', x, y)
	elif event == cv2.EVENT_RBUTTONDOWN:
		print('right mouse button down at', x, y)
	elif event == cv2.EVENT_RBUTTONUP:
		print('right mouse button up at', x, y)
	elif event == cv2.EVENT_LBUTTONDBLCLK:
		print('Left mouse button double clicked at', x, y)
	elif event == cv2.EVENT_RBUTTONDBLCLK:
		print('right mouse button double clicked at', x, y)
	elif event == cv2.EVENT_MOUSEWHEEL:
		if flags > 0:
			print('mouse wheel scrolled up at', x, y)
		else:
			print('mouse wheel scrolled down at', x, y)


img = cv2.imread('image/cat.jpg', cv2.IMREAD_UNCHANGED)

cv2.namedWindow('img')
cv2.setMouseCallback('img', on_mouse)

while True:
	cv2.imshow('img', img)
	key = cv2.waitKey(30)
	if key == 27: break