# BGR을 HSV로 변환하여 저장하기
import cv2
import numpy as np

bgr = cv2.imread('image/cat.jpg')   # 기본적으로 BRG color space로 표현됨

HSV = cv2.cvtColor(bgr, cv2.COLOR_BGR2HSV)    # YCrCbi color space
print(bgr.shape, bgr.dtype)
print(HSV.shape, HSV.dtype)

hue, saturation, value = cv2.split(HSV)

cv2.imwrite("image/cat_hue.png", hue)
cv2.imwrite("image/cat_saturation.png", saturation)
cv2.imwrite("image/cat_value.png", value)

cv2.imshow('bgr', bgr)
cv2.imshow('HSV', HSV)
cv2.imshow('hue', hue)
cv2.imshow('saturation', saturation)
cv2.imshow('value', value)
cv2.waitKey()