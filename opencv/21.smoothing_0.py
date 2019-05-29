import cv2 as cv
import numpy as np

img = cv.imread('filter_blur.jpg')

rx, ry = 12, 6 # half kernel size
sx, sy =  6, 3 # spread of Gaussian in x and y directions

kernel = np.zeros((ry*2+1, rx*2+1), np.float32)
for i in range(kernel.shape[0]):
    for j in range(kernel.shape[1]):
        x = j - rx # x distance from the kernel center
        y = i - ry # y distance from the kernel center
        kernel[i,j] = np.exp(-(x*x)/(2*sx*sx)-(y*y)/(2*sy*sy))

cv.imshow('kernel', cv.resize(kernel, (400,200)))

kernel /= kernel.sum() # make the kernel sum 0
img_smoothed = cv.filter2D(img, -1, kernel)

# (rx*2+1, ry*2+1) is kernel size in x and y directions
img_blurred = cv.GaussianBlur(img, (rx*2+1,ry*2+1), sigmaX=sx, sigmaY=sy)

# auto detect sigmax, sigmay from the kernel size
img_blurred_autosigma = cv.GaussianBlur(img, (rx*2+1,ry*2+1), 0)

cv.imshow('original', img)
cv.imshow('smoothed', img_smoothed)
cv.imshow('GaussianBlurred', img_blurred)
cv.imshow('GaussianBlurredAutoSigma', img_blurred_autosigma)

cv.waitKey()