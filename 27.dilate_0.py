import cv2 as cv
import numpy as np

mat = np.array([[0, 1, 2, 3],
				[4, 5, 6, 7],
				[8, 9, 8, 7],
				[6, 5, 4, 3]], np.uint8)

print('mat')
print(mat)
# this uses all the neighbors in the kernel
kernel = np.array([[1, 1, 1],
				   [1, 1, 1],
				   [1, 1, 1]], np.uint8)
print('kernel')
print(kernel)
# find the maximum value in the neighbors indicated by the non-zero elements in the kernel
dilated = cv.dilate(mat, kernel)
print('dilated')
print(dilated)

# kernel = None -> kernel = 3 by 3 filled with 1s
dilated = cv.dilate(mat, None)
print(dilated)

print('\nmat')
print(mat)
# this uses current pixel and only top, bottom, left, right neighbors
kernel = np.array([[0, 1, 0],
				   [1, 1, 1],
				   [0, 1, 0]], np.uint8)
print('kernel')
print(kernel)
dilated = cv.dilate(mat, kernel)
print('dilated')
print(dilated)

# dilate one more time
dilated_dilated = cv.dilate(dilated, kernel)
print('dilated_dilated')
print(dilated_dilated)

# the same result as above
dilated_iterations2 = cv.dilate(mat, kernel, iterations=2)
print('dilated_iterations2')
print(dilated_iterations2)