# show for at most 3 secs and display key value

import cv2

img = cv2.imread('image/cat.jpg', cv2.IMREAD_UNCHANGED)

cv2.imshow('img', img)
# delay 3s
key = cv2.waitKey(3000)
print('key =', key)
