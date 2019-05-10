# 저장된 동영상 play
import cv2

capture = cv2.VideoCapture("capture.avi")    # 파일명을 쓰면, 파일에서 읽어옴
fps = capture.get(cv2.CAP_PROP_FPS)
print("fps:", fps)

dt = int(1000./fps)    # delay time

while True:
    ret, frame = capture.read()    # ret: frae capture 결과(bool), frame: capture한 이미지
    if ret:
        cv2.imshow('frame', frame)
    else:
        break
    if cv2.waitKey(dt) == 27:
        break
    
capture.release()