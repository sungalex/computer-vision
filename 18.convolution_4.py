# filtering function 직접 구현하기 => color image 부분 수정 필요, sharpen filter 검토/확인 필요
import cv2 as cv
import numpy as np

# filter_gray(): gray scale image, zero padding(convolution 후 원본 이미지 크기 유지)
def filter_gray(img, kernel, border_type):
    kw, kh = kernel.shape[0:2]
    kw2, kh2 = kw//2, kh//2
    padding_img_shape = (img.shape[0] + kw-1, img.shape[1] + kh-1)
    padding_img = np.zeros(padding_img_shape, np.uint8)
    np.copyto(padding_img[kw2:-kw2, kh2:-kh2], img)
    if border_type == 1:   # 0(black)으로 패딩한 경우 테두리가 검은색이 되는 문제 해결(테두리 값 복사)
        padding_img[:kw2, kh2:-kh2] = img[0,:]
        padding_img[-kw2:, kh2:-kh2] = img[-1,:]
        padding_img[kw2:-kw2, :kh2] = img[:,0].reshape(img.shape[0], -1)
        padding_img[kw2:-kw2, -kh2:] = img[:,-1].reshape(img.shape[0], -1)
        padding_img[:kw2, :kh2] = img[0,0]
        padding_img[-kw2:, :kh2] = img[-1,0]
        padding_img[:kw2, -kh2:] = img[0,-1]
        padding_img[-kw2:, -kh2:] = img[-1,-1]

    # print(padding_img.shape)
    # cv.imshow('padding_img', padding_img)
    filtered_img = np.zeros_like(img, img.dtype)

    # filtered_img = cv.filter2D(padding_img, cv.CV_32F, conv_kernel)
    # cv.filter2D()와 동일한 기능 구현
    for i in range(filtered_img.shape[0]):
        for j in range(filtered_img.shape[1]):
            filtered_img[i,j] = np.multiply(padding_img[i:i+kw,j:j+kh], kernel).sum()
    return np.abs(filtered_img).astype(np.uint8)

def filter(img, kernel, border_type):
    if len(img.shape) == 2:
        return filter_gray(img, kernel, border_type)
    elif len(img.shape) == 3:    # 컬러 이미지 부분 수정 필요(cv.filter2D 소스 참조)
        hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
        h, s, v = cv.split(hsv)
        filtered_v = filter_gray(v, kernel, border_type)   # color를 변화 시키지 않기 위해 value 만 filter 처리
        filtered_hsv = cv.merge((h,s,filtered_v))
        filtered_bgr = cv.cvtColor(filtered_hsv, cv.COLOR_HSV2BGR)
        # b, g, r = cv.split(img)
        # filtered_b = filter_gray(b, kernel, border_type)
        # filtered_g = filter_gray(g, kernel, border_type)
        # filtered_r = filter_gray(r, kernel, border_type)
        # filtered_bgr = cv.merge((filtered_b, filtered_g, filtered_r))
        return filtered_bgr
    else:
        return None

img = cv.imread('image/filter_blur.jpg', cv.IMREAD_GRAYSCALE)
# img = cv.imread('image/filter_blur.jpg', cv.IMREAD_COLOR)
# print(img.shape)

kernel_size = 5   # 홀수 값 지정

# bluring filter (주변 값의 평균값으로 대체)
# kernel_b = np.full((3,3), 1./9)  # if kernel_size is 3
kernel_b = np.full((kernel_size,kernel_size), 1./(kernel_size*kernel_size))
filtered_b = filter(img, kernel_b, 1)

# sharpening filter
# 더 선명한 이미지로 변경하기 위해서는 주변 값에는 filter를 minus 값을 할당하고, 중심값에는 filter를 plus 값을 할당
# 중심값은 필터의 전체 합이 1이상 되게 설정하면 Sharpening 한 이미지가 됨
# 필터 연산을 수행하면, 주변 값이 더 크면 중심의 값이 작아지고, 주변 값이 더 작으면 중심의 값이 더 커짐
kernel_s = np.array([[0,-1,0],
                     [-1,5,-1],
                     [0,-1,0]])
# kernel_s = np.full((kernel_size,kernel_size), -1)
# kernel_s[kernel_size//2,kernel_size//2] = kernel_size*kernel_size
filtered_s = filter(img, kernel_s, 1)

cv.imshow('original', img)
cv.imshow('filtered_blur', filtered_b)
cv.imshow('filtered_sharpen', filtered_s)
cv.waitKey()