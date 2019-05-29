# contour : 테투리(윤곽선)
import cv2
import numpy as np

img = np.zeros((480,640,3), np.uint8)

# 두께를 -1로 하면 공간 전체를 채움
cv2.circle(img, (200,150), 80, (255,255,0), -1)
cv2.circle(img, (500,150), 50, (255,0,0), -1)
cv2.rectangle(img, (300,300), (500,400), (0,255,255), -1)

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_, img_thresh = cv2.threshold(img_gray, 150, 255, cv2.THRESH_BINARY)   # threshold(150) 보다 큰 값은 255로, 작은 값은 0으로 변환

contours, _ = cv2.findContours(img_thresh, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)   # RETR: retrieval, APPROX: Aproximation(근사)
# print(type(contours[0]))
# print('contours')
# for c in contours:
#     print(c.shape, c.dtype, cv2.contourArea(c))   # c.shape : (점의 갯수, 1, (x,y))

# 심플한 contour (점이 최소로 만들어짐)
# contours, _ = cv2.findContours(img_thresh, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)   # RETR: retrieval, APPROX: Aproximation(근사)

# print(contours[0][2][0][0], contours[0][2][0][1])    # 첫번째 contour의 3번째(index 2)의 x, y 좌표

color = [(0,255,0), (0,0,255)]
# for idx, contour in enumerate(contours):
#     for point in contour:
#         x, y = point[0][0], point[0][1]
#         cv2.circle(img, (x,y), 3, color[idx], -1)

# cv2.drawContours(img, contours, -1, (0,0,255), 3)

for idx, contour in enumerate(contours):
    cv2.drawContours(img, contours, idx, color[idx], 3)

cv2.imshow("img", img)
cv2.imshow("img_gray", img_gray)
cv2.imshow("img_thresh", img_thresh)

cv2.waitKey()