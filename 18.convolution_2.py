# convolution : 합성곱 (두 metrics의 각 원소를 곱한 후 전체 합을 구함) -> 윤곽선 찾기
# roberts edge detection
import cv2 as cv
import numpy as np

img = cv.imread('image/edge_test.jpg', cv.IMREAD_GRAYSCALE)

# 중심 픽셀과 대각선 상단위 픽셀간의 차이를 추출
kernel_l = np.array([[-1,0,0],
                  [0,1,0],
                  [0,0,0]])
kernel_r = np.array([[0,0,-1],
                  [0,1,0],
                  [0,0,0]])

# filter2D는 img와 kernel을 convolution 하는 메서드 (필터가 클수록 더 흐려짐)
# filtered_l = cv.filter2D(img, -1, kernel_l)
# filtered_r = cv.filter2D(img, -1, kernel_r)
filtered_l = cv.filter2D(img, cv.CV_32F, kernel_l)    # 소숫점 계산값을 받아오기 위해 float32로 지정
filtered_r = cv.filter2D(img, cv.CV_32F, kernel_r)

# 픽셀간의 크기를 계산하는 함수 : cv.magnitude(A,B)
img_filtered = cv.magnitude(filtered_l, filtered_r)   # 양의 정수 값을 반환

cv.imshow('original', img)
# cv.imshow('filtered_l', img_filtered_l)
# cv.imshow('filtered_r', img_filtered_r)
cv.imshow('filtered_l', np.abs(filtered_l).astype(np.uint8))   # float32를 uint8으로 변경
cv.imshow('filtered_r', np.abs(filtered_r).astype(np.uint8))
cv.imshow('filtered', img_filtered.astype(np.uint8))    # uint8로 변환
cv.waitKey()