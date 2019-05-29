# remove noise from image

import cv2 as cv
import numpy as np

img = cv.imread('face_with_noise.png')
img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
_, mask = cv.threshold(img_gray, 100, 255, cv.THRESH_BINARY)
mask_dilated = cv.dilate(mask, None, iterations=6)
background_mean = cv.mean(img, cv.bitwise_not(mask_dilated))
print(background_mean)
background = np.full(img.shape, background_mean[0:3], dtype=np.uint8)
mask_eroded = cv.erode(mask, None, iterations=3)
mask_eroded_dilated = cv.dilate(mask_eroded, None, iterations=6)
mask_eroded_dilated_not = cv.bitwise_not(mask_eroded_dilated)
face = cv.bitwise_and(img, img, mask=mask_eroded_dilated)
not_face = cv.bitwise_and(background, background, mask=mask_eroded_dilated_not)
img_without_noise = cv.add(face, not_face)

face_without_noise = cv.imread('face_without_noise.png')
print('Success =', np.array_equal(img_without_noise, face_without_noise))

face_mask = cv.bitwise_and(mask, mask_eroded_dilated)

cv.imshow('img', img)
cv.imshow('img_gray', img_gray)
cv.imshow('mask', mask)
cv.imshow('mask_eroded', mask_eroded)
cv.imshow('mask_eroded_dilated', mask_eroded_dilated)
cv.imshow('mask_eroded_dilated_not', mask_eroded_dilated_not)
cv.imshow('face', face)
cv.imshow('not_face', not_face)
cv.imshow('img_wighout_noise', img_without_noise)
cv.imshow('face_mask', face_mask)
cv.waitKey()
