# show histogram for each channel
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('image/cat.jpg', cv2.IMREAD_COLOR)

color = ['b', 'g', 'r']

for i, c in enumerate(color):
    hist = cv2.calcHist([img], [i], None, [256], [0,256])
    plt.plot(hist, color=c)
    
plt.xlim([0, 256])
plt.show()