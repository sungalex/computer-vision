# 동영상에 fps 정보 추가하기
import cv2
import numpy as np
import time

# cv2.getTickCount() : 경과한 tick 수 => 경과 시간 = tick1 - tick0
# cv2.getTickFrequency() => fps = 경과 시간 / cv2.getTickFrequency()
capture = cv2.VideoCapture(0)

# 화면 사이즈가 크면, FPS가 낮게 나타남(프레임 처리에 time delay 발생???) : 640 * 480 으로 변경
capture.set(3, 640)
capture.set(4, 480)

fps = int(capture.get(5))
size = (int(capture.get(3)), int(capture.get(4)))
print(fps)

count = 0   # 캡처한 이미지 수
fps = 0
# t0 = cv2.getTickCount()
t0 = time.time()
cv2.namedWindow('frame', cv2.WINDOW_NORMAL)

while True:
    ret, frame = capture.read()    # ret: frae capture 결과(bool), frame: capture한 이미지
    frame = cv2.flip(frame, 1)
    cv2.putText(frame, str(fps), (10,60), cv2.FONT_HERSHEY_SIMPLEX, 2, (0,255,0), 3)
    cv2.imshow('frame', frame)
    
    count += 1
    if count == 10:
        # t = cv2.getTickCount()
        # delta_time = (t - t0) / cv2.getTickFrequency()
        t = time.time()
        delta_time = t - t0
        #print(delta_time)
        fps = int(10./delta_time)
        count = 0
        t0 = t
    
    if cv2.waitKey(1) == 27: break
    
capture.release()