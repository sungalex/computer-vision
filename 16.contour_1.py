# 영상에서 특정 물체의 영역을 지정해서, 해당 이미지를 tracking 하도록 만들기(contour 추가)
import cv2
import numpy as np

capture = cv2.VideoCapture('capture.avi')
fps = capture.get(cv2.CAP_PROP_FPS)
dt = int(1000./fps)
print(fps, dt)

for i in range(30): capture.read()    # 처음 2장의 이미지는 버림
_, img0 = capture.read()

img = img0.copy()
pts = []

def on_mouse(enent, x, y, flags, param):
    global img
    if enent == cv2.EVENT_LBUTTONDOWN:
        if len(pts) > 0:
           cv2.line(img, (pts[-1][0], pts[-1][1]), (x,y), (0,0,255))
        pts.append([x,y])

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

lower_range = np.array([max(hmean-10,0),max(smean-20,0),max(vmean-30,0)])
upper_range = np.array([min(hmean+10,180),min(smean+20,255),min(vmean+30,255)])
print('lower_range:',lower_range)
print('upper_range:', upper_range)

cv2.destroyWindow("mask")
cv2.namedWindow('obj', cv2.WINDOW_NORMAL)

while True:
    ret, frame = capture.read()
    if not ret:
        cv2.waitKey()
        break
    
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, lower_range, upper_range)   # lower_range ~ upper_range 색상 범위만 마스크로 반환됨

    obj = cv2.bitwise_and(frame, frame, mask=mask)
    cv2.imshow('obj', obj)

    contours, _ = cv2.findContours(mask, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)

    # cv2.drawContours(img, contours, -1, (0,0,255), 3)
    for idx, contour in enumerate(contours):
        if cv2.contourArea(contour) > 100:   # noise를 둘러싼 contour를 제외하기 위해 contour 크기가 작은 것은 제외
            cv2.drawContours(frame, contours, idx, (0,0,255), 3)

    cv2.imshow('img', frame)
    if cv2.waitKey(dt) == 27: break

capture.release()