import cv2

events = [i for i in dir(cv2) if 'EVENT' in i]
print(events)


def on_mouse(event, x, y, flags, param):
	print(event, x, y, flags, param)


img = cv2.imread('image/cat.jpg', cv2.IMREAD_UNCHANGED)

cv2.namedWindow('img')
cv2.setMouseCallback('img', on_mouse)

while True:
	cv2.imshow('img', img)
	key = cv2.waitKey(30)
	if key == 27: break