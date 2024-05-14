import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
import os

print(os.curdir)

# 2 Ie Bee]
img = cv.imread('5/sudoku.png', cv.IMREAD_GRAYSCALE)
assert img is not None, "file could not be read, check with os.path.exists()"

# Olzls} +aHst7]
img = cv.medianBlur(img,5)

ret, th1= cv.threshold(img, 127,255, cv.THRESH_BINARY)
th2 = cv.adaptiveThreshold(img,255,cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY_INV,11,2)
th3 = cv.adaptiveThreshold(img,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY_INV,11,2)

# 284 AS 718s)
titles = ['Original Image', 'BINARY', 'BINARY_INV', 'TRUNC', 'TOZERO', 'TOZERO_INV']

# SAO A] Tl Ses]

images = [img, th1,th2,th3]

for i in range(4):
    plt. subplot (2,3, i+1),plt.imshow( images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.show()