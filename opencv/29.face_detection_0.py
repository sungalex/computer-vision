import cv2 as cv
import numpy as np

# 얼굴 이미지 저장하기
# capture = cv.VideoCapture(0)
# capture.set(cv.CAP_PROP_FRAME_WIDTH, 640)
# capture.set(cv.CAP_PROP_FRAME_HEIGHT, 480)
# width = int(capture.get(cv.CAP_PROP_FRAME_WIDTH))
# height = int(capture.get(cv.CAP_PROP_FRAME_HEIGHT))
# print(width, height)

# while True:
#     _, frame = capture.read()
#     cv.imshow('frame', frame)
#     if cv.waitKey(1) != -1: break
# cv.imwrite('myface.jpg', frame)
# capture.release()

# 얼굴과 눈을 검출하는 classifiers
xml_folder = '/Users/alex/venvs/opencv/lib/python3.6/site-packages/cv2⁩/data/'
face_cascade = cv.CascadeClassifier(xml_folder+'haarcascade_frontalface_default.xml')
eye_cascade = cv.CascadeClassifier(xml_folder+'haarcascade_eye.xml')

cap = cv.VideoCapture(0)
img = cv.imread('myface.jpg')

while True:
    ret, frame = cap.read()
    faces = face_cascade.detectMultiScale(img, scaleFactor=1.1, minNeighbors=5)
    print('faces:', faces)

    # ...