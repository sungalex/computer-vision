import cv2
import numpy as np

img1 = np.zeros((300,300), np.uint8)
img2 = np.zeros((300,300), np.uint8)
mask = np.zeros((300,300), np.uint8)

# img1에 흰색 원 그리기
cv2.circle(img1, (150,150), 100, 255, -1)

# img2에 왼쪽 반 흰색 사각형
cv2.rectangle(img2, (0,0), (150,300), 255, -1)

# mask에 위쪽 반 흰색
cv2.rectangle(mask, (0,0), (300,150), 255, -1)

# img1과 img2의 논리 곱
img1_and_img2 = cv2.bitwise_and(img1, img2)
cv2.bitwise_and(img1, img2, dst=img1_and_img2)

# mask 옵션을 사용하면, mask 이미지에서 0이 아닌 픽셀만 and 연산 수행(여기서는 mask 이미지는 위쪽 반만 흰색으로 마스크 적용 영역이 됨)
# img1_and_img2_with_mask = cv2.bitwise_and(img1, img2, mask=mask) # 검정색 바탕 이미지에 마스크 결과를 출력
img1_and_img2_with_mask = np.full((300,300), 127, np.uint8)
cv2.bitwise_and(img1, img2, dst=img1_and_img2_with_mask, mask=mask)

cv2.imshow("img1", img1)
cv2.imshow("img2", img2)
cv2.imshow("mask", mask)
cv2.imshow("img1_and_img2", img1_and_img2)
cv2.imshow("img1_and_img2_with_mask", img1_and_img2_with_mask)
cv2.waitKey()