import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
import os

img1 = cv.imread('5/images/img1.jpg')
img2 = cv.imread('5/images/img1.jpg')

img3 = cv.add(img1, img2)

img4 = cv.addWeighted(img1, 0.5, img2, 0.5, 0)

titles = ['src', 'map', 'add', 'addweight']
imgs = [img1, img2, img3, img4]

for i in range(4):
  plt.subplot(2,2,i+1)
  plt.imshow(imgs[i])
  plt.title(titles[i])
  plt.xticks([])
  plt.yticks([])
plt.show()