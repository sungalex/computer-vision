import cv2
# import numpy as np

# mat0 = np.array([[120, 130], [140, 150]])
# mat1 = np.array([[100, 100], [100, 100]])
# mat2 = np.array([[145, 145], [145, 145]])

# print("mat0")
# print(mat0)
# print("mat1")
# print(mat1)
# print("mat2")
# print(mat2)

img0 = cv2.imread("add1.jpg")
img1 = cv2.imread("add2.jpg")

num_images = 100

# 두개의 이미지를 가중치를 달리하며 합성하기
for i in range(9999):
    w0 = (i%num_images) / (num_images-1)
    w1 = 1 - w0
    img = cv2.addWeighted(img0, w0, img1, w1, 0)
    cv2.imshow("img", img)
    if cv2.waitKey(30) == 27:
        break
