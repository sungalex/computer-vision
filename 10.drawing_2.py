import cv2
import numpy as np

# 1: 직선, 2:사각형, 3:원, 4:자유곡선

x0, y0 = 0, 0
draw = False
img = np.zeros((480,640,3), np.uint8)
cp_img = np.copy(img)
mode = 1 

def on_mouse(event, x, y, flags, param):
    global x0, y0, img, cp_img, draw, mode

    if event == cv2.EVENT_LBUTTONDOWN:
        draw = True
        x0, y0 = x, y
        pts = [x, y]
    elif draw and event == cv2.EVENT_MOUSEMOVE:
        if mode < 4:   # 자유곡선을 만들 때는 기존 이미지를 유지
            np.copyto(img, cp_img)    # 새로운 변수를 만들지 않고 기존 reference에 값을 복사함
        
        if mode == 1:
            cv2.line(img, (x0,y0), (x,y), (255, 0, 0), 2)
        elif mode == 2:
            cv2.rectangle(img, (x0,y0), (x,y), (0, 255, 0), 2)
        elif mode == 3:
            r = np.sqrt((x-x0)*(x-x0) + (y-y0)*(y-y0))
            cv2.circle(img, (x0,y0), int(r), (0, 0, 255), 2)
        elif mode == 4:
            cv2.line(img, (x0,y0), (x,y), (255, 0, 255), 2)
            x0, y0 = x, y

    elif event == cv2.EVENT_LBUTTONUP:
        draw = False
        np.copyto(cp_img, img)

cv2.namedWindow('img')
cv2.setMouseCallback('img', on_mouse)

while True:
    cv2.imshow('img', img)
    key = cv2.waitKey(30)
    if key > 48 and key < 53: mode = key - 48
    if key == 27: break