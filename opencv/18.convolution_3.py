# convolution 직접 구현 : 같의 위치의 원소끼리 곱한 후 모두 합하기(scala 값)
import numpy as np

mat0 = np.array([[0,1,0],[1,2,1],[0,1,0]])
mat1 = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(mat0)
print(mat1)

# 직접 계산
sum = 0
for i in range(3):
    for j in range(3):
        sum += mat0[i,j] * mat1[i,j]
print('convolution:', sum)

# numpy matrix operation => multiply & sum
mat_conv = mat0 * mat1   # 같은 위치의 원소 끼리 곱해서 동일한 shape의 matrix 생성
mat_mul = np.multiply(mat0, mat1)
print('mat_conv:\n', mat_conv)
print('mat_multiply:\n', mat_mul)
print('numpy convolution:', mat_mul.sum())

# cf: numpy dot & matmul(행렬 곱셈) => convolution이 아님
# print(np.dot(mat0, mat1))
# print(np.matmul(mat0, mat1))