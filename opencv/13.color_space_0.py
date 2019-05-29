# 색공간(color space)란 이미지를 구성하는 하나의 픽셀(pixel) 정보를 다차원 수치공간으로 표현하는 방식이다.
# 대표적인 색공간으로는 Gray scale, RGB, HSV, YCrCb 등이 있다.

# 사람이 느끼는 color는 빛의 파장들에 대해 해당 시각세포가 인지하는 강도(시각세포가 활성화 되는 비율)이다.

# 모니터의 color는 G, B, R 값의 크기로 구성되어 있고, 
# 사람의 시각세포가 G, B, R에 반응하는 강도에 의해 모니터의 빛을 인식한다.

# 실제 사람이 느끼는 빛은 G, B, R만으로 표현할 수 없고, 
# RGB로 표현된 color는 실제 사람이 인지하는 color와는 다를 수도 있다.

import cv2
import numpy as np

bgr = cv2.imread('image/cat.jpg')   # 기본적으로 BRG color space로 표현됨

gray = cv2.cvtColor(bgr, cv2.COLOR_BGR2GRAY)   # GRAY color space
YCrCb = cv2.cvtColor(bgr, cv2.COLOR_BGR2YCrCb)    # YCrCbi color space
print(gray.shape, gray.dtype)
print(YCrCb.shape, YCrCb.dtype)

Y, Cr, Cb = cv2.split(YCrCb)   # 밝기, red, blue
print("np.array_equal(gray, Y):", np.array_equal(gray, Y))   # 결과: True => Y는 이미지의 밝기를 표현
print(Y.shape, Cr.shape, Cb.shape)

cv2.imshow('bgr', bgr)
cv2.imshow('gray', gray)
cv2.imshow('Y', Y)
cv2.imshow('Cr', Cr)
cv2.imshow('Cb', Cb)
cv2.waitKey()
