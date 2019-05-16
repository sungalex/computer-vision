import cv2 as cv
import numpy as np

img = np.array([[2,1,3],
                [7,5,4]], np.uint8)

mask = np.array([[0,1,1],
                [0,1,1]], np.uint8)

minVal, maxVal, minLoc, maxLoc = cv.minMaxLoc(img, mask=mask)   # mask가 1인 영역 중에서 min, max

print('img\n', img)
print('mask\n', mask)
print("minVal, minLoc", minVal, minLoc)    # minLoc: (col, row)
print("maxVal, maxLoc", maxVal, maxLoc)
