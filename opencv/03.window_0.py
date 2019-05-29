import cv2
import time

img = cv2.imread('image/cat.jpg', cv2.IMREAD_UNCHANGED)

# # 사진크기를 설정할 수 있음.
# cv2.namedWindow('img')
# time.sleep(3)
# cv2.moveWindow('img', 0, 0)
# # 창 크기를 사진 크기에 맞춰 줌.
# cv2.imshow('img', img)
# # esc 누를때 까지 정지
# cv2.waitKey()
# cv2.moveWindow('img', 400, 400)
# cv2.waitKey()
# # 지금까지 열렸던 모든 창을 닫음.
# cv2.destroyAllWindows()

cv2.namedWindow('img-autosize', cv2.WINDOW_AUTOSIZE)
time.sleep(3)
cv2.namedWindow('img-normal', cv2.WINDOW_NORMAL)
cv2.imshow('img-autosize', img)
cv2.imshow('img-normal', img)
cv2.waitKey()
cv2.destroyAllWindows()

cv2.namedWindow('img-autosize', cv2.WINDOW_AUTOSIZE)
cv2.namedWindow('img-normal', cv2.WINDOW_NORMAL)
cv2.resizeWindow('img-autosize', 1000, 1000)
cv2.resizeWindow('img-normal', 500, 500)
cv2.imshow('img-autosize', img)
cv2.imshow('img-normal', img)
cv2.waitKey()