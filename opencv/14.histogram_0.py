import cv2
from matplotlib import pyplot as plt

img = cv2.imread('image/cat.jpg', cv2.IMREAD_GRAYSCALE)

print('img:', img.shape, img.dtype)
print('img.ravel():', img.ravel().shape, img.ravel().dtype)

plt.hist(img.ravel(), 256, [0,256])
plt.xlim([0,256])
plt.show()

hist = cv2.calcHist([img], [0], None, [256], [0,256])
print('hist:', hist.shape, hist.dtype)

plt.plot(hist)
plt.xlim([0,256])
plt.show()
