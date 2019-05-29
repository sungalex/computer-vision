import cv2
import numpy as np

img = np.zeros((480,640,3), np.uint8)

cv2.line(img, (20,20), (620,460), (0, 255, 0), 3,)
cv2.rectangle(img, (100,100), (400,400), (0, 0, 255), 3)
cv2.rectangle(img, (500,100), (600,200), (255,0,0), -1)   # 두께를 -1로 하면 공간 전체를 채움
cv2.circle(img, (320,240), 100, (255,255,0), 3)
cv2.ellipse(img, (320,240), (300,200), 10, 0, 180, (0,255,255), 3)

pts = np.array([[50,150], [200,80], [350,120], [300,200]], np.int32)
cv2.polylines(img, [pts.reshape((-1,1,2))], True, (255,0,255), 3)   # 차원의 수와 차원의 크기를 맞춰줘야 함

pts = np.array([[350,350],[500,280],[630,320],[520,320]], np.int32)
cv2.fillPoly(img, [pts.reshape((-1,1,2))], (0,0,255))

cv2.putText(img, "Hello", (10, 450), cv2.FONT_HERSHEY_SIMPLEX, 4, (255,255,255), 3)

cv2.imshow("img", img)
cv2.waitKey()