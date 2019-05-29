import cv2 as cv

# Create classifiers for face and eye
xml_folder = 'C:/Users/USER/venv/computer-vision/Lib/site-packages/cv2/data/'
face_cascade = cv.CascadeClassifier(xml_folder+'haarcascade_frontalface_default.xml')
eye_cascade = cv.CascadeClassifier(xml_folder+'haarcascade_eye.xml')

cap = cv.VideoCapture(0)

while True:
	ret, frame = cap.read()

	faces = face_cascade.detectMultiScale(frame, scaleFactor=1.1, minNeighbors=5)
	print('faces')
	print(faces)

	for (x, y, w, h) in faces:
		cv.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
		roi = frame[y:y + h, x:x + w]  # get face sub region
		# detect eyes in the detected face region
		eyes = eye_cascade.detectMultiScale(roi, scaleFactor=1.1, minNeighbors=80)
		print('eyes')
		print(eyes)
		for (ex, ey, ew, eh) in eyes:
			cv.rectangle(roi, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)

	cv.imshow('frame', frame)
	if cv.waitKey(1) != -1: break