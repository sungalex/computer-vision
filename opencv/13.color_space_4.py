# YCrCb를 이용하여 HSV cylinder와 유사한 2차원 이미지 만들기
import cv2
import numpy as np

# rmax = 256
# bmax = 256

# Y = np.zeros((rmax, bmax), np.uint8)
# Cr = np.zeros((rmax, bmax), np.uint8)
# Cb = np.zeros((rmax, bmax), np.uint8)

# for r in range(rmax):
#     Cr[:, r] = r

# for b in range(bmax):
#     Cb[b, :] = b

# value = 128
# dv = 10

# while True:
#     Y.fill(value)
#     YCrCb = cv2.merge((Y, Cr, Cb))
#     BGR = cv2.cvtColor(YCrCb, cv2.COLOR_YCrCb2BGR)

#     cv2.imshow('himg', Y)
#     cv2.imshow('simg', Cr)
#     cv2.imshow('vimg', Cb)
#     cv2.imshow('BGR', BGR)

#     key = cv2.waitKeyEx()
#     if key == 27: break
#     elif key == 107: value += dv
#     elif key == 106: value -= dv

value = 128
delta = 10

YCrCb = np.array([[value, Cr, Cb] \
    for Cb in np.arange(256) \
        for Cr in np.arange(256)], np.uint8).reshape(256,256,3)

while True:
    BGR = cv2.cvtColor(YCrCb, cv2.COLOR_YCrCb2BGR)
    cv2.imshow('Y', YCrCb[...,0])
    cv2.imshow('Cr', YCrCb[...,1]) 
    cv2.imshow('Cb', YCrCb[...,2])
    cv2.imshow('BGR', BGR)
    key = cv2.waitKeyEx()   # 화살표 키도 인식(mac에서 화살표 인식 안됨)
    if key == 27: break
    elif key == 107: YCrCb[..., 0] += delta    # k
    elif key == 106: YCrCb[..., 0] -= delta    # j