# contour hierarchy (Tree) 
import cv2
import numpy as np

img = np.zeros((480,640,3), np.uint8)

# 두께를 -1로 하면 공간 전체를 채움
cv2.rectangle(img, (50,50), (200,430), (255,255,255), -1)
cv2.rectangle(img, (250,50), (400,430), (255,255,255), -1)
cv2.rectangle(img, (450,50), (600,430), (255,255,255), -1)

cv2.rectangle(img, (90,150), (160,220), (0,0,0), -1)
cv2.rectangle(img, (90,270), (160,340), (0,0,0), -1)
cv2.rectangle(img, (270,70), (380,410), (0,0,0), -1)

cv2.rectangle(img, (300,120), (350,170), (255,255,255), -1)
cv2.rectangle(img, (300,220), (350,270), (255,255,255), -1)
cv2.rectangle(img, (300,320), (350,370), (255,255,255), -1)

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# contours, hierachy = cv2.findContours(img_gray, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

# cv2.RETR_TREE : 영역 기준으로 Tree 생성(구조는 hierarchy로 반환)
contours, hierachy = cv2.findContours(img_gray, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

print('number of contours:', len(contours))
print('hierachy:', hierachy.shape)
for i in range(hierachy.shape[1]):
    print(i, hierachy[0][i])   # [next_contour, previous_contour, first_child_contour, parent_contour] -> 없는 경우 -1

color = [(255,0,0), (0,255,0), (0,0,255), (255,255,0), (0,255,255), (255,0,255), (127,0,0), (0,127,0), (0,0,127)]

for idx, contour in enumerate(contours):
    cv2.drawContours(img, contours, idx, color[idx], 3)
    pos = contour[0][0][0], contour[0][0][1] - 7
    cv2.putText(img, str(idx), pos, cv2.FONT_HERSHEY_SIMPLEX, 1, color[idx], 3)

cv2.imshow("img", img)

cv2.waitKey()