# 고양이 이미지의 H, S, V 값을 변경해서 각각의 이미지를 저장하기
# Hue:가로(색조), Saturation:세로(채도), Value:커서 상/하(밝기)
import cv2
import numpy as np

img = cv2.imread('image/cat.jpg')
HSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
h, s, v = cv2.split(HSV)

dh = cv2.addWeighted(h, 1, h, 0, 180//2)    # 색조는 범위가 180까지 (90을 더하면 반대 색)
HSV_dh = cv2.merge((dh, s, v))
img_hue_plus = cv2.cvtColor(HSV_dh, cv2.COLOR_HSV2BGR)
cv2.imwrite('image/cat_hue_plus.png', img_hue_plus)

ds = cv2.addWeighted(s, 2, s, 0, 0)
HSV_ds1 = cv2.merge((h, ds, v))
img_saturation_plus = cv2.cvtColor(HSV_ds1, cv2.COLOR_HSV2BGR)
cv2.imwrite('image/cat_saturation_plus.png', img_saturation_plus)

ds = cv2.addWeighted(s, 0.5, s, 0, 0) 
HSV_ds2 = cv2.merge((h, s, v))
img_saturation_minus = cv2.cvtColor(HSV_ds2, cv2.COLOR_HSV2BGR)
cv2.imwrite('image/cat_saturation_minus.png', img_saturation_minus)

while True:
    cv2.imshow("img", img)
    cv2.imshow('img_saturation_plus', img_saturation_plus)
    cv2.imshow('img_value_minus', img_saturation_minus)
    cv2.imshow('img_hue_plus', img_hue_plus)
    key = cv2.waitKeyEx()   # 화살표 키도 인식(mac에서 화살표 인식 안됨)
    if key == 27: break