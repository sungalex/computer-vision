import cv2
import numpy as np

x0, y0 = 0, 0
draw = False
img = np.zeros((480,640,3), np.uint8)
cp_img = np.copy(img)   # img와 cp_img는 다른 reference를 가지게 됨

def on_mouse(event, x, y, flags, param):
    global x0, y0, img, cp_img, draw

    if event == cv2.EVENT_LBUTTONDOWN:
        draw = True
        x0, y0 = x, y
    elif draw and event == cv2.EVENT_MOUSEMOVE:
        # img = np.copy(cp_img)
        np.copyto(img, cp_img)
        cv2.rectangle(img, (x0,y0), (x,y), (0, 255, 0), 2)
    elif event == cv2.EVENT_LBUTTONUP:
        draw = False
        np.copyto(cp_img, img)

cv2.namedWindow('img')
cv2.setMouseCallback('img', on_mouse)

while True:
    cv2.imshow('img', img)
    key = cv2.waitKey(30)
    if key == 27: break