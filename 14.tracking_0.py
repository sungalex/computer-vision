# 영상에서 특정 물체의 영역을 지정해서, 해당 이미지를 tracking 하도록 만들기
import cv2
import numpy as np

capture = cv2.VideoCapture(0)
width = int(capture.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(capture.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = capture.get(cv2.CAP_PROP_FPS)
print("width:", width)
print("height:", height)
print("fps:", fps)

pts = list()
img = np.zeros((height, width, 3), np.uint8)

def on_mouse(event, x, y, flags, param):
    global pts, img

    if event == cv2.EVENT_LBUTTONDOWN:
        if len(pts) != 0:
            cv2.line(img, (pts[-1][0], pts[-1][1]), (x,y), (0,0,255))
            cv2.imshow("capture", img)
        pts.append([x,y])

pause = False
cv2.namedWindow('capture', cv2.WINDOW_NORMAL)
cv2.setMouseCallback('capture', on_mouse)

while True:
    ret, frame = capture.read()
    key = cv2.waitKey(30)
    if key == 27: break
    elif key == 32:    # space bar
        pause = True
        cv2.imshow("capture", frame)
        pts = list()
        img = frame
    elif key == 13:    # enter
        pause = False
        if len(pts) > 2:
            pts = np.array(pts).reshape(-1,1,2)
            cv2.fillPoly(img, [pts], (255,255,255))
            cv2.imshow('capture', img)

            cv2.namedWindow('selected', cv2.WINDOW_NORMAL)
            black_img = np.zeros((height, width, 3), np.uint8)
            cv2.fillPoly(black_img, [pts], (255,255,255))
            cv2.imshow('selected', black_img)
            pts = list()
        cv2.waitKey()    # wait any key
    elif not pause:
        cv2.imshow("capture", frame)
