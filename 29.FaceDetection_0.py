import cv2 as cv

#cap = cv.VideoCapture(0)
#while True:
#    ret, frame = cap.read()
#    cv.imshow('frame', frame)
#    if cv.waitKey(1) != -1: break
#cv.imwrite('myface.jpg', frame)
#cap.release()

# 얼굴과 눈을 검출하는 classifiers
xml_folder = 'C:/Users/USER/venv/computer-vision/Lib/site-packages/cv2/data/'
face_cascade = cv.CascadeClassifier(xml_folder+'haarcascade_frontalface_default.xml')
eye_cascade = cv.CascadeClassifier(xml_folder+'haarcascade_eye.xml')

img = cv.imread('myface.jpg')

# receive boxes for detected faces
# scaleFactor: increase the detection window size by 1.1 at each scale
# the real detected face should be detected by at least minNeighbors boxes
faces = face_cascade.detectMultiScale(img, scaleFactor=1.1, minNeighbors=5)
print('faces')
print(faces)

for (x, y, w, h) in faces:
    cv.rectangle(img, (x,y), (x+w,y+h), (255,0,0),2)
    roi = img[y:y+h, x:x+w] # get face sub region
    # detect eyes in the detected face region
    eyes = eye_cascade.detectMultiScale(roi, scaleFactor=1.1, minNeighbors=5)
    print('eyes')
    print(eyes)
    for (ex,ey,ew,eh) in eyes:
        cv.rectangle(roi, (ex,ey), (ex+ew, ey+eh), (0,255,0), 2)

cv.imshow('img', img)
cv.waitKey()