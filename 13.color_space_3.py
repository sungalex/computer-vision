# HSV cylinder와 유사한 2차원 이미지 만들기
# Hue:가로(색조), Saturation:세로(채도), Value:커서 상/하(밝기)
import cv2
import numpy as np

# smax = 256
# hmax = 180   # 색조의 범위는 0~179까지

# himg = np.zeros((smax, hmax), np.uint8)
# simg = np.zeros((smax, hmax), np.uint8)
# vimg = np.zeros((smax, hmax), np.uint8)

# for h in range(hmax):
#     himg[:, h] = h

# for s in range(smax):
#     simg[s, :] = s

# value = 128
# dv = 10

# while True:
#     vimg.fill(value)
#     HSV = cv2.merge((himg, simg, vimg))
#     BGR = cv2.cvtColor(HSV, cv2.COLOR_HSV2BGR)

#     cv2.imshow('himg', himg)
#     cv2.imshow('simg', simg)
#     cv2.imshow('vimg', vimg)
#     cv2.imshow('BGR', BGR)

#     key = cv2.waitKeyEx()
#     if key == 27: break
#     elif key == 107: value += dv
#     elif key == 106: value -= dv

value = 128
delta = 10

HSV = np.array([[h, s, value] \
    for s in np.arange(256) \
        for h in np.arange(180)], np.uint8).reshape(256,180,3)

while True:
    BGR = cv2.cvtColor(HSV, cv2.COLOR_HSV2BGR)
    cv2.imshow('HSV_hue', HSV[...,0])
    cv2.imshow('HSV_saturaion', HSV[...,1]) 
    cv2.imshow('HSV_value', HSV[...,2])
    cv2.imshow('BGR', BGR)
    key = cv2.waitKeyEx()   # 화살표 키도 인식(mac에서 화살표 인식 안됨)
    if key == 27: break
    elif key == 107: HSV[..., 2] += delta    # k
    elif key == 106: HSV[..., 2] -= delta    # j