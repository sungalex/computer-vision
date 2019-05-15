# 2차원 histogram
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('image/cat.jpg', cv2.IMREAD_COLOR)

plt.figure(figsize=(10,10))

# 0번과 1번 채널(blue, green)을 이용한 2차원 히스토그램
plt.subplot(1,3,1)
hist = cv2.calcHist([img], [0,1], None, [4, 4], [0,256,0,256])
plt.title(('0 & 1'))
plt.imshow(hist)

# 1번과 2번 채널(green, red)을 이용한 2차원 히스토그램
plt.subplot(1,3,2)
hist = cv2.calcHist([img], [1,2], None, [64, 64], [0,256,0,256])
plt.title(('1 & 2'))
plt.imshow(hist)

# 2번과 0번 채널(red, blue)을 이용한 2차원 히스토그램
plt.subplot(1,3,3)
hist = cv2.calcHist([img], [2,0], None, [64, 64], [0,256,0,256])
plt.title(('2 & 0'))
plt.imshow(hist)
plt.show()