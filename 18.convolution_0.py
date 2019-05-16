# convolution : 합성곱 (두 metrics의 각 원소를 곱한 후 전체 합을 구함) -> bluring
import cv2 as cv
import numpy as np

img = cv.imread('image/filter_blur.jpg')

# 선명한 이미지를 부드럽게 변경하기(bluring 효과) : 주변 값의 평균값으로 대체
# 평균값을 계산하려면, 원하는 filter 크기의 kernel을 만들어서 1/filter크기(가로x세로)을 채운 후 convolution
# kernel = np.full((3,3), 1./9)   # 9는 필터 크기
kernel = np.full((9,9), 1./(9*9))

# filter2D는 img와 kernel을 convolution 하는 메서드 (필터 크기가 클수록 더 흐려짐)
img_filtered = cv.filter2D(img, -1, kernel)   # -1은 img의 자료형을 사용한다는 의미

# -1은 원본 이미지와 같은 데이터 타입으로 출력 이미지 생성함
print(img.shape, img.dtype)
print(img_filtered.shape, img_filtered.dtype)

cv.imshow('original', img)
cv.imshow('filtered', img_filtered)
cv.waitKey()