# read image as gray and show array info

import cv2

img = cv2.imread('image/cat.jpg', cv2.IMREAD_GRAYSCALE)

print('type(img) =', type(img))
print('img.shape, img.dtype =', img.shape, img.dtype)