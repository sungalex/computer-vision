import cv2 as cv
import numpy as np

mat = np.array([[0, 1, 2, 3],
				[4, 5, 6, 7],
				[8, 9, 8, 7],
				[6, 5, 4, 3]], np.uint8)
print('mat')
print(mat)

# 커널안의 모든 원소들을 이용
kernel = np.array([[1, 1, 1],
				   [1, 1, 1],
				   [1, 1, 1]], np.uint8)
print('kernel')
print(kernel)

# 커널의 0이 아닌 값이 가리키는 이웃 픽셀들의 최소값을 찾아 대체
eroded = cv.erode(mat, kernel)
print('eroded')
print(eroded)

# kernel = None 로 넣어주면 1로 채워진 3 by 3 커널이 자동으로 적용된다.
eroded = cv.erode(mat, None)
print(eroded)

print('\nmat')
print(mat)
# 나 자신과 상하좌우의 이웃값들 중에 최소값을 찾음
kernel = np.array([[0, 1, 0],
				   [1, 1, 1],
				   [0, 1, 0]], np.uint8)
print('kernel')
print(kernel)
eroded = cv.erode(mat, kernel)
print('eroded')
print(eroded)

# 침식한결과를 다시 침식
eroded_eroded = cv.erode(eroded, kernel)
print('eroded_eroded')
print(eroded_eroded)

# 위와 같은 결과
eroded_iterations2 = cv.erode(mat, kernel, iterations=2)
print('eroded_iterations2')
print(eroded_iterations2)