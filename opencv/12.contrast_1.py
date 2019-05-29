# 이미지의 대비(contrast) : 변화가 심한 정도
import cv2
import numpy as np

img0 = cv2.imread("image/cat.jpg")

# np.mean(img0, (0,1))   # B, G, R 각각의 밝기 평균을 구함
# mean의 모든 픽셀을 img0의 B, G, R 각각의 평균 값으로 셋팅
mean = np.zeros(img0.shape, np.uint8)
mean[:, :] = np.mean(img0, (0,1))
scale = 1.5    # scale: alpha
img1 = cv2.addWeighted(img0, scale, mean, 1-scale, 0)  # 대비는 증가하지만 밝기는 변화가 없음
# g(x) = alpha * (f(x)-mean) + mean = alpha * f(x) + (1-alpha) * mean => beta: 1-alpha
# g(x)는 f(x)를 mean 만큼 아래로 이동 한 후, alpha 만큼 곱하고, 다시 mean 만큼 더해줌 => 다차원 곡선의 이동과 증폭처럼 생각하면 됨

cv2.imshow('img0', img0)
cv2.imshow('img1', img1)
# cv2.imshow('mean', mean)
cv2.waitKey()
