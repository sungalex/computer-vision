# histogram equalization : 이미지의 contrast를 향상시킬 수 있다
import cv2
from matplotlib import pyplot as plt

img0 = cv2.imread('image/cat.jpg', cv2.IMREAD_GRAYSCALE)
img1 = cv2.equalizeHist(img0)

cv2.imshow('img0', img0)
cv2.imshow('img1', img1)
cv2.waitKey()

plt.figure(figsize=(14,5))

# 원본 히스토그램
plt.subplot(1,2,1)
plt.hist(img0.ravel(), 32, [0,256])
plt.xlim([0,256])

# 평평해진 히스토그램
plt.subplot(1,2,2)
plt.hist(img1.ravel(), 32, [0,256])
plt.xlim([0,256])

plt.show()