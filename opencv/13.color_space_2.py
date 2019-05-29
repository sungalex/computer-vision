# HSV를 읽어서 BGR로 변환하여 저장하기
import cv2
import numpy as np

hue = cv2.imread('image/cat_hue.png', cv2.IMREAD_UNCHANGED)    # cv2.COLOR_GRAYSCALE
saturation = cv2.imread('image/cat_saturation.png', cv2.IMREAD_UNCHANGED)
value = cv2.imread('image/cat_value.png', cv2.IMREAD_UNCHANGED)

HSV = cv2.merge((hue, saturation, value))
bgr = cv2.cvtColor(HSV, cv2.COLOR_HSV2BGR)

print(hue.shape, HSV.shape)

cv2.imwrite("image/cat_merge.png", bgr)

cv2.imshow('hue', hue)
cv2.imshow('saturation', saturation)
cv2.imshow('value', value)
cv2.imshow('HSV', HSV)    # cv2.imshow()는 3채널 이미지는 BGR로 인지하기 때문에 화면에는 변형된 color로 보임
cv2.imshow('bgr', bgr)
cv2.waitKey()