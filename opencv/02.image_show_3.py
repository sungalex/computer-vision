# bgr->rgb using slicing [start:stop:step]

import cv2
from matplotlib import pyplot as plt

img = cv2.imread('image/cat.jpg', cv2.IMREAD_COLOR)
# print(img.shape)
# print(img[:, :, -1].shape)
# print(img[:, :10, ::-1].shape)
# print("img[:] = ", img[:].shape)
# print("img[::] = ", img[::1].shape)
# print(img[::2, :20, ::-1].shape)
# print(img[:, :, ::-1].shape)

# start, stop, skip
# skip == -1이면 뒤에서부터 BGR to RGB
# skip == 2이면 jump 2
plt.imshow(img[:, :, ::-1], interpolation='bicubic')

# x,y label 설정
plt.xticks([]), plt.yticks([]) # == axis("off")
# plt.axis("off")
plt.show()

plt.imshow(img[:, :, ::-1], interpolation='bicubic')

# cv2.imshow("img", img)
# cv2.waitKey()

# plt.imshow(img[:, :, ::-1], interpolation='none')
# plt.show()
# plt.imshow(img[:, :, ::-1], interpolation='kaiser')
# plt.show()

# print()
# L = [_ for _ in range(20)]
# print(L)
# print(L[::-1])
# LL = [0, 10, 20, 9 ,8, 7, 6]
# print(LL[::-1])