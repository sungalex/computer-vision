import cv2

capture = cv2.VideoCapture(0)   # 괄호 안의 숫자는 장치 번호(첫번째 장치:0, 두번째:1, ...)

capture.set(3, 640)   # cv2.CAP_PROP_FRAME_WIDTH
capture.set(4, 480)   # cv2.CAP_PROP_FRAME_HEIGHT
size = (int(capture.get(3)), int(capture.get(4)))
# width = int(capture.get(cv2.CAP_PROP_FRAME_WIDTH))
# height = int(capture.get(cv2.CAP_PROP_FRAME_HEIGHT))
# fps = capture.get(cv2.CAP_PROP_FPS)
fps = int(capture.get(5))   # cv2.CAP_PROP_FPS
print("fps:", fps)
print("width, height:", size)

# fourcc는 코덱 이름, 
fourcc = cv2.VideoWriter_fourcc(*'XVID')    # XVID 코덱 사용 : (*'XVID')는 ('X', 'V', 'I', 'D')와 동일한 의미
# fourcc = cv2.VideoWriter_fourcc(*'DX50')    # DX50 코덱 사용
# fourcc = cv2.VideoWriter_fourcc(*'H260')    # H260 코덱 사용(코덱이 설치되지 않은 경우 에러가 발생함) => 설치 해야 함
writer = cv2.VideoWriter('capture.avi', fourcc, fps, size)

# fourcc = cv2.VideoWriter_fourcc(*'mp4v')      # lower case
# writer = cv2.VideoWriter('capture.mp4', fourcc, fps, (width, height))

cv2.namedWindow('frame', cv2.WINDOW_NORMAL)

while True:
    _, frame = capture.read()
    frame = cv2.flip(frame, 1)
    writer.write(frame)
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xff == 27: break   # waitKey(1)은 최소 1ms를 대기한다는 의미(1ms 이상)
    
capture.release()
writer.release()