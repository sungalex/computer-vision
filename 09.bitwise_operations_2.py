import cv2
import numpy as np

img = cv2.imread('bit_test.jpg', cv2.IMREAD_COLOR)
logo = cv2.imread('logo.jpg', cv2.IMREAD_COLOR)

# 컬러를 흑백이미지로 변환
logo_gray = cv2.cvtColor(logo,cv2.COLOR_BGR2GRAY)

# 10 보다 큰 값을 가진 픽셀은 255로, 아니면 0으로 이진 이미지 생성
_, mask = cv2.threshold(logo_gray, 10, 255, cv2.THRESH_BINARY)

# logo size로 img 자르기
# roi = img[(img.shape[0]-logo.shape[0])//2:(img.shape[0]+logo.shape[0])//2, (img.shape[1]-logo.shape[1])//2:(img.shape[1]+logo.shape[1])//2, :]
img_rows, img_cols = img.shape[0:2]
logo_rows, logo_cols = logo.shape[0:2]
roi_x = (img_cols - logo_cols)//2
roi_y = (img_rows - logo_rows)//2
img_target = np.copy(img)    # 원본 img를 유지하기 위해 복사해서 사용(deep copy)
roi = img_target[roi_y:roi_y+logo_rows, roi_x:roi_x+logo_cols]
# roi와 img_target은 roi 영역을 공유하는 변수임(roi를 변경하면, img_target도 변경됨)

# logo와 target img 합치기
# 자기 자신과 bitwise_and를 하면 자기 자신이 됨. 마스크가 지정되지 않은 영역은 0으로 초기화됨
logo_fg = cv2.bitwise_and(logo, logo, mask = mask)    # logo 부분만 채워져 있는 logo
mask_inv = cv2.bitwise_not(mask)
img_bg = cv2.bitwise_and(roi, roi, mask = mask_inv)   # logo 부분이 비어있는 img 

img_add = cv2.add(img_bg, logo_fg)
np.copyto(roi, img_add)    # 원래의 roi의 reference는 변경하지 않고, roi의 값만 img_add의 값으로 대체함
# python은 기본적으로 변수가 value가 아닌, reference로 동작함 (np.copy의 경우 새로운 reference를 생성함)
# 아래 코드는 roi라는 이름으로 새로운 reference 변수가 생성되어, img_target의 값은 변경되지 않음
# roi = cv2.add(img_bg, logo_fg)

# 출력하기
cv2.imshow("img", img)
cv2.imshow("logo", logo)
cv2.imshow("logo_gray", logo_gray)
cv2.imshow("mask", mask)
cv2.imshow("roi", roi)
cv2.imshow("logo_fg", logo_fg)
cv2.imshow("img_bg", img_bg)
cv2.imshow("img_target", img_target)
cv2.waitKey()