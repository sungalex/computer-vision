# color image histogram equalization : 이미지의 contrast를 향상시키기
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('image/cat.jpg', cv2.IMREAD_COLOR)
cv2.imshow('img', img)

# 컬러별로 분리한 후 각각 히스토그램 평평하게 변환(BGR)
b, g, r = cv2.split(img)
b1 = cv2.equalizeHist(b) 
g1 = cv2.equalizeHist(g)
r1 = cv2.equalizeHist(r)

# 변형된 각각 채널을 합침
img_bgr_eq = cv2.merge((b1, g1, r1))
cv2.imshow('img_bgr_eq', img_bgr_eq)   # 선명해지긴 했지만, 색조가 변함

# 컬러별로 분리한 후 히스토그램 평평하게 변환(HSV)
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
h, s, v = cv2.split(hsv)
v1 = cv2.equalizeHist(v)   # 밝기 만 변환(hue와 saturation은 그대로)

# 변형된 각각 채널을 합침
hsv1 = cv2.merge((h, s, v1))
img_hsv_eq = cv2.cvtColor(hsv1, cv2.COLOR_HSV2BGR)
cv2.imshow('img_hsv_eq', img_hsv_eq)    # 컬러가 유지되고, 선명해짐

# 컬러별로 분리한 후 히스토그램 평평하게 변환(YCrCb)
YCrCb = cv2.cvtColor(img, cv2.COLOR_BGR2YCrCb)
Y, Cr, Cb = cv2.split(YCrCb)
Y1 = cv2.equalizeHist(Y)   # 밝기 만 변환

# 변형된 각각 채널을 합침
YCrCb1 = cv2.merge((Y1, Cr, Cb))
img_YCrCb_eq = cv2.cvtColor(YCrCb1, cv2.COLOR_YCrCb2BGR)
cv2.imshow('img_YCrCb_eq', img_YCrCb_eq)    # 컬러가 유지되고, 선명해짐(HSV로 변환한 것과 유사하지만 완전히 같지는 않음)

cv2.waitKey()
