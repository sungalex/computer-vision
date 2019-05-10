import cv2
import numpy as np

img = np.zeros((480,640,3), dtype=np.uint8)
cv2.imshow('img',img)
cv2.waitKey()