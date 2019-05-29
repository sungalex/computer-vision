# 동영상에 fps 정보 추가하기
import cv2
import numpy as np
import time

# cv2.getTickCount() : 경과한 tick 수 => 경과 시간 = tick1 - tick0
# cv2.getTickFrequency() => fps = 경과 시간 / cv2.getTickFrequency()
capture = cv2.VideoCapture(0)
print(capture.get(cv2.CAP_PROP_FPS))
count = 0   # 캡처한 이미지 수
fps = 0
# t0 = cv2.getTickCount()
t0 = time.time()
cv2.namedWindow('frame', cv2.WINDOW_NORMAL)

while True:
    ret, frame = capture.read()    # ret: frae capture 결과(bool), frame: capture한 이미지
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