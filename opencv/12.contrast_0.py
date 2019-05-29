# 이미지의 대비(contrast) : 변화가 심한 정도
import cv2
import numpy as np

img0 = cv2.imread("image/cat.jpg")
img1 = cv2.addWeighted(img0, 1.5, img0, 0, 0)  # weight를 키우면 대비(contrast)도 커지고, 밝기(brightness)도 증가함
# img1 = cv2.addWeighted(img0, 1, img0, 0, 60)   # 이미지에 값을 더하면, 밝기는 증가하지만 대비는 변화가 없음

cv2.imshow('img0', img0)
cv2.imshow('img1', img1)
cv2.waitKey()
