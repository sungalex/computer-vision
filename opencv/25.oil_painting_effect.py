import cv2 as cv
import numpy as np

def oil_painting_effect(src, radius, levels):
	dst = np.zeros(src.shape, src.dtype)
	gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)

	for i in range(src.shape[0]):
		print(i)
		for j in range(src.shape[1]):
			hist = np.zeros(levels) # 이웃하는 픽셀들의 히스토그램을 저장할 변수
			bgr_sum = np.zeros((levels,3)) # 이웃하는 픽셀들의 컬러값의 합을 저장할 변수
			# 이웃하는 모든 픽셀들을 방분하며 히스토그램과 각 구간의 컬러의 합을 계산
			for u in range( max(i-radius,0), min(i+radius+1, src.shape[0]) ):
				for v in range( max(j-radius,0), min(j+radius+1, src.shape[1]) ):
					# 해당 히스토그램 상자의 인덱스 계산
					level = gray[u,v] * levels // 256
					hist[level] += 1 # 히스토그램 누적
					bgr_sum[level] += src[u,v]# 컬러의 합 누적
			max_idx = np.argmax(hist) # 히스토 그램의 값이 가장 큰 인덱스
			# 가장 많은 픽셀들이 속한 히스토드램 구간에 있는 픽셀들의 평균 컬러 값
			dst[i,j] = bgr_sum[max_idx] // hist[max_idx]

	return dst

img = cv.imread('red-and-green-leavs-of-autumn-jpg.jpg')

radius, levels = 4, 8
effect = oil_painting_effect(img, radius, levels)

cv.imshow('img', img)
cv.imshow('effect', effect)
cv.waitKey()