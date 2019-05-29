# pip install opencv-contrib-python
import cv2 as cv
import numpy as np

tracker_types = ['BOOSTING', 'MIL', 'KCF', 'TLD', 'MEDIANFLOW', 'MOSSE', 'CSRT']
tracker_type = tracker_types[5]
tracker = None

if tracker_type == 'BOOSTING':
	tracker = cv.TrackerBoosting_create()
elif tracker_type == 'MIL':
	tracker = cv.TrackerMIL_create()
elif tracker_type == 'KCF':
	tracker = cv.TrackerKCF_create()
elif tracker_type == 'TLD':
	tracker = cv.TrackerTLD_create()
elif tracker_type == 'MEDIANFLOW':
	tracker = cv.TrackerMedianFlow_create()
elif tracker_type == 'MOSSE':
	tracker = cv.TrackerMOSSE_create()
elif tracker_type == "CSRT":
	tracker = cv.TrackerCSRT_create()


video = cv.VideoCapture(0)

while True:
	ok, frame = video.read()
	if not ok: break
	cv.imshow('Tracking', frame)
	if cv.waitKey(1) != -1: break

bbox = cv.selectROI('Tracking', frame, showCrosshair=False)
print(bbox)

# Initialize tracker with first frame and bounding box
ok = tracker.init(frame, bbox)
print('tracker.init :', ok)

count = 0
fps = 0
t0 = cv.getTickCount()

while True:

	ok, frame = video.read()
	if not ok: break
	if cv.waitKey(1) == 27: break

	# Update tracker
	ok, bbox = tracker.update(frame)

	# Draw bounding box
	if ok:
		# Tracking success
		p1 = (int(bbox[0]), int(bbox[1]))
		p2 = (int(bbox[0] + bbox[2]), int(bbox[1] + bbox[3]))
		cv.rectangle(frame, p1, p2, (0, 255, 0), 2)
	else:
		# Tracking failure
		cv.putText(frame, 'Tracking failure', (200, 240), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

	# Display tracker type on frame
	cv.putText(frame, tracker_type + " Tracker", (10, 60), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

	# Display FPS on frame
	cv.putText(frame, "FPS : " + str(int(fps)), (10, 30), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

	# Display result
	cv.imshow('Tracking', frame)

	# Exit if ESC pressed
	if cv.waitKey(1) == 27: break

	count += 1
	if( count == 10 ):
		t = cv.getTickCount()
		time = (t-t0) / cv.getTickFrequency()
		fps = int(np.round(10/time))
		count = 0
		t0 = t

