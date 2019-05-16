import cv2 as cv
import numpy as np

def minMaxFilterGray(img, kernel_size, flag):
    # flag=0 이면 min filter, flag=1 이면 max filter
    kh = kw = kernel_size
    kh2, kw2 = kernel_size//2, kernel_size//2

    dst = np.zeros(img.shape, img.dtype)
    mask = np.zeros_like(dst)

    for row in range(dst.shape[0]):
        for col in range(dst.shape[1]):
            # roi = img[max(row-kh2,0):min(row+kh2+1,dst.shape[0]), max(col-kw2,0):min(col+kw2+1,dst.shape[1])]
            roi = img[max(row-kh2,0):row+kh2+1, max(col-kw2,0):col+kw2+1]
            minVal, maxVal, minLoc, maxLoc = cv.minMaxLoc(roi)
            if flag == 0:
                dst[row, col] = minVal
            elif flag == 1:
                dst[row, col] = maxVal
            else:
                pass
    return dst

def minMaxFilter(img, kernel_size, flag):
    if len(img.shape) == 2:
        dst = minMaxFilterGray(img, kernel_size, flag)
        return dst
    elif len(img.shape) == 3:
        hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
        h, s, v = cv.split(hsv)
        filtered_v = minMaxFilterGray(v, kernel_size, flag)   # color를 변화 시키지 않기 위해 value 만 filter 처리
        filtered_hsv = cv.merge((h,s,filtered_v))
        filtered_bgr = cv.cvtColor(filtered_hsv, cv.COLOR_HSV2BGR)
        return filtered_bgr
    else:
        return None

img = cv.imread('image/min_max.jpg', cv.IMREAD_COLOR)
minFiltered = minMaxFilter(img, 7, 0)
maxFiltered = minMaxFilter(img, 7, 1)

cv.imshow('img', img)
cv.imshow('minFiltered', minFiltered)
cv.imshow('maxFiltered', maxFiltered)
cv.waitKey()