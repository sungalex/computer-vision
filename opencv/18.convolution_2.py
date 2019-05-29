# convolution : 합성곱 (두 metrics의 각 원소를 곱한 후 전체 합을 구함) -> 윤곽선 찾기
# roberts edge detection
import cv2 as cv
import numpy as np

img = cv.imread('image/edge_test.jpg', cv.IMREAD_GRAYSCALE)

# 중심 픽셀과 대각선 상단위 픽셀간의 차이를 추출
# 중심 픽셀과 대각선 하단 아래 픽셀간의 차이를 추출해도 유사한 결과 도출됨
# 4개의 대각선 필터를 모두 사용하면 좀던 선명한 경계값을 도출함(목적에 따라 사용)
kernel_lu = np.array([[-1,0,0],
                      [0,1,0],
                      [0,0,0]])
kernel_ru = np.array([[0,0,-1],
                      [0,1,0],
                      [0,0,0]])
# kernel_ld = np.array([[0,0,0],
#                       [0,1,0],
#                       [-1,0,0]])
# kernel_rd = np.array([[0,0,0],
#                       [0,1,0],
#                       [0,0,-1]])

# filter2D는 img와 kernel을 convolution 하는 메서드 (필터가 클수록 더 흐려짐)
filtered_lu = cv.filter2D(img, cv.CV_32F, kernel_lu)    # 소숫점 계산값을 받아오기 위해 float32로 지정
filtered_ru = cv.filter2D(img, cv.CV_32F, kernel_ru)
# filtered_ld = cv.filter2D(img, cv.CV_32F, kernel_ld)
# filtered_rd = cv.filter2D(img, cv.CV_32F, kernel_rd)

# 픽셀간의 크기를 계산하는 함수 : cv.magnitude(A,B)
img_filtered_u = cv.magnitude(filtered_lu, filtered_ru)   # 양의 정수 값을 반환
# img_filtered_d = cv.magnitude(filtered_ld, filtered_rd)
# img_filtered = cv.magnitude(img_filtered_u, img_filtered_d)

cv.imshow('original', img)
cv.imshow('filtered_lu', np.abs(filtered_lu).astype(np.uint8))   # float32를 uint8으로 변경
cv.imshow('filtered_ru', np.abs(filtered_ru).astype(np.uint8))
# cv.imshow('filtered_ld', np.abs(filtered_ld).astype(np.uint8))
# cv.imshow('filtered_rd', np.abs(filtered_rd).astype(np.uint8))
cv.imshow('filtered_u', img_filtered_u.astype(np.uint8))    # uint8로 변환
# cv.imshow('filtered_d', img_filtered_d.astype(np.uint8))
# cv.imshow('filtered', img_filtered.astype(np.uint8))
cv.waitKey()