import cv2 as cv
import numpy as np

feature_params = dict( maxCorners = 10,
                       qualityLevel = 0.3,
                       minDistance = 100,
                       blockSize = 7 )

lk_params = dict( winSize  = (15,15),
                  maxLevel = 5,
                  criteria = (cv.TERM_CRITERIA_EPS | cv.TERM_CRITERIA_COUNT, 10, 0.03))

# Select colors from hue in HSV color space, saturation=255, value=255
colors_hsv = np.zeros((1, feature_params['maxCorners'], 3), np.uint8)
for i in range(colors_hsv.shape[1]):
	colors_hsv[0,i] = 180  * i // feature_params['maxCorners'], 255, 255
colors_bgr = cv.cvtColor(colors_hsv, cv.COLOR_HSV2BGR)

device = 0
cap = cv.VideoCapture(device)

while True:
	_, img = cap.read()
	cv.imshow('img', img)
	if cv.waitKey(1) == 32: break

_, img0 = cap.read()
img0_gray = cv.cvtColor(img0, cv.COLOR_BGR2GRAY)
# 초기 트랙킹할 특징점들 선정
pts0 = cv.goodFeaturesToTrack(img0_gray, **feature_params)

# Create a canvas image for drawing track lines
track_img = np.zeros_like(img0)

while True:
	_, img1 = cap.read()

	img1_gray = cv.cvtColor(img1, cv.COLOR_BGR2GRAY)

	pts1, status, error = cv.calcOpticalFlowPyrLK(img0_gray, img1_gray, pts0, None, **lk_params)

	# 찾는데 성공한 점들만 모음
	pts0_success = pts0[status == 1]
	pts1_success = pts1[status == 1]

	for i, (p0, p1) in enumerate(zip(pts0_success, pts1_success)):
		# track_img 에 트랙킹 선을 그린다.
		cv.line(track_img, tuple(p0), tuple(p1), colors_bgr[0,i].tolist(), 2)
		# 현재 컬러 프레임에 원을 그린다.
		cv.circle(img1, tuple(p1), 7, colors_bgr[0,i].tolist(), -1)

	# 트랙킹 선과 현재 이미지를 합한다.
	img = cv.add(img1, track_img)

	# 현재 프레임의 pts_success1 에서 다음 프레임을 위해 pts0 로 업데이트
	pts0 = pts1_success.reshape(-1,1,2)

	# 현재 프레임의 흑백 이미지를 다음 프레임을 위해서 img0_gray 로 업데이트
	np.copyto(img0_gray, img1_gray)

	cv.imshow('img', img)
	cv.imshow('track', track_img)
	if cv.waitKey(1) == 27: break
