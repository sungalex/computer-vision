import cv2
import numpy as np

mat0 = np.uint8([[130,140],[150,160]])
mat1 = np.uint8([[100,100],[100,100]])
mat2 = np.uint8([[145,145],[145,145]])

print('mat0')
print(mat0)
print('mat1')
print(mat1)
print('mat2')
print(mat2)

print('mat0 + mat1')
print(mat0 + mat1)

print('cv2.add(mat0, mat1)')
print(cv2.add(mat0, mat1))

print('mat0 - mat2')
print(mat0 - mat2)

print('cv2.subtract(mat0, mat2)')
print(cv2.subtract(mat0, mat2))

print('cv2.addWeighted(mat0, 0.7, mat1, 0.3, 0)')
print(cv2.addWeighted(mat0, 0.7, mat1, 0.3, 0))
