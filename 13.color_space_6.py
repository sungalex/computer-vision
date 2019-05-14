# 영상에서 특정 물체의 영역을 지정해서, 해당 이미지를 tracking 하도록 만들기
import cv2
import numpy as np

capture = cv2.VideoCapture('capture.avi')
fps = capture.get(cv2.CAP_PROP_FPS)
dt = int(1000./fps)
print(fps, dt)

for i in range(2): capture.read()    # 처음 2장의 이미지는 버림
_, img0 = capture.read()

img = img0.copy()
x0, y0 = -1, -1
pts = []

def on_mouse(enent, x, y, flags, param):
    global x0, y0, img
    if enent == cv2.EVENT_LBUTTONDOWN:
        pts.append([x,y])
        if (x0,y0) != (-1,-1):
            cv2.line(img, (x0,y0), (x,y), (0,0,255))
        x0, y0 = x, y

cv2.namedWindow('img', cv2.WINDOW_NORMAL)
cv2.setMouseCallback('img', on_mouse)

while True:
    cv2.imshow('img', img)
    if cv2.waitKey(dt) == 27: break

cv2.fillPoly(img, [np.array(pts).reshape(-1,1,2)], (255,255,255))

cv2.namedWindow('mask', cv2.WINDOW_NORMAL)
mask = np.zeros(img.shape[0:2], np.uint8)
cv2.fillPoly(mask, [np.array(pts).reshape(-1,1,2)], 255)

cv2.imshow('img', img)
cv2.imshow('mask', mask)
cv2.waitKey()

hsv = cv2.cvtColor(img0, cv2.COLOR_BGR2HSV)
hmean, smean, vmean, _ = cv2.mean(hsv, mask)    # mask 영역만 평균값 구하기

lower_range = np.array([max(hmean-20,0),max(smean-40,0),max(vmean-60,0)])
upper_range = np.array([min(hmean+20,180),min(smean+40,255),min(vmean+60,255)])
print('lower_range:',lower_range)
print('upper_range:', upper_range)

cv2.namedWindow('obj', cv2.WINDOW_NORMAL)

while True:
    ret, frame = capture.read()
    if not ret: break
    
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, lower_range, upper_range)   # lower_range ~ upper_range 색상 범위만 마스크로 반환됨

    obj = cv2.bitwise_and(frame, frame, mask=mask)
    cv2.imshow('obj', obj)
    if cv2.waitKey(dt) == 27: break

capture.release()