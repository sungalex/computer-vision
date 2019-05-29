# convolution : 합성곱 (두 metrics의 각 원소를 곱한 후 전체 합을 구함) -> sharpening
import cv2 as cv
import numpy as np

img = cv.imread('image/filter_blur.jpg')

# 더 선명한 이미지로 변경하기 위해서는 주변 값에는 filter를 minus 값을 할당하고, 중심값에는 filter를 plus 값을 할당
# 필터 연산을 수행하면, 주변 값이 더 크면 중심의 값이 작아지고, 주변 값이 더 작으면 중심의 값이 더 커짐

# 3x3 filter
# kernel = np.array([[0,-1,0],
#                   [-1,5,-1],
#                   [0,-1,0]])    # 합이 1(정규화 불필요)
# 주변 8개 kernel 셀을 모두 적용하면 상하좌우 만 적용한 경우보다 변화가 조금 더 커짐
# kernel = np.full((3,3), -1)   # 중앙값을 제외한 주변 값의 합은 -8
# kernel[1,1] = 9   # 필터의 전체 합이 1이 되게 설정하면 조금 더 Sharpening 한 이미지가 됨

# 5x5 filter
kernel = np.array([[-1,-1,-1,-1,-1],
                   [-1,2,2,2,-1],
                   [-1,2,8,2,-1],
                   [-1,2,2,2,-1],
                   [-1,-1,-1,-1,-1]])/8.0   # 8로 나눠서 정규화(합이 1이 되게 함)

# filter2D는 img와 kernel을 convolution 하는 메서드 (필터가 클수록 더 흐려짐)
img_filtered = cv.filter2D(img, -1, kernel)

# -1은 원본 이미지와 같은 데이터 타입으로 출력 이미지 생성함
print(img.shape, img.dtype)
print(img_filtered.shape, img_filtered.dtype)

cv.imshow('original', img)
cv.imshow('filtered', img_filtered)
cv.waitKey()