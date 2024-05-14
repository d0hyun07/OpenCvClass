import cv2
import numpy as np
from matplotlib import pyplot as plt

img1 = cv2.imread("./images/img11.jpg", cv2.IMREAD_GRAYSCALE)

h,w, = img1.shape
c_b = h //2 ;c_w = w//2
