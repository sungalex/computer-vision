import cv2 as cv
import numpy as np

# 트랙바의 값이 변할때마다 새로운 값이 val 로 넘어오며 호출된다.
def onChange(val):
    # 트랙바의 값을 얻을 수 있는 다른 방법
    pos = cv.getTrackbarPos('brightness', 'img')
    print(val, pos) # val 와 pos 의 값이 같음을 알 수 있다.
    img.fill(val)
    cv.imshow('img', img)


init_val = 128
img = np.full((480,640), init_val, np.uint8)
cv.namedWindow('img')
# brightness 라는 이름의 트랙바를 img 라는 이름의 창에 생성,
# init_val 초기값, 255 최대값
# onChange 함수를 콜백함수로 등록
cv.createTrackbar('brightness', 'img', init_val, 255, onChange)

cv.imshow('img', img)
cv.waitKey()