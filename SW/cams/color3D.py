import numpy as np
import cv2
import sys
import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import time

def avg(lst):
    suma = 0.0
    for i in lst:
        suma += i
    return suma / len(lst)


img1 = cv2.imread(sys.argv[1], cv2.CV_LOAD_IMAGE_GRAYSCALE)
img2 = cv2.imread(sys.argv[2], cv2.CV_LOAD_IMAGE_GRAYSCALE)

ret, thresh1 = cv2.threshold(img1, 0, 255, cv2.THRESH_BINARY)
ret, thresh2 = cv2.threshold(img2, 0, 255, cv2.THRESH_BINARY)

kernel = np.ones((3, 3), np.uint8)
closing1 = cv2.erode(thresh1, kernel)
closing2 = cv2.erode(thresh2, kernel)

height = closing1.shape[0]
width = closing1.shape[1]

d1 = [[] for i in xrange(height)]
d2 = [[] for i in xrange(height)]

for i in xrange(height):
    for j in xrange(width):
        if closing1[i, j] == 0:
            d1[i].append(j)
        if closing2[i, j] == 0:
            d2[i].append(j)

xl = []
yl = []
zl = []

B = 100
for i in xrange(height):
    if d1[i] and d2[i]:
        x1 = avg(d1[i])
        x2 = avg(d2[i])
        dx = x1 - x2
        z = -B/dx
        print x1, x2
        yl.append(i)
        xl.append(x1)
        zl.append(z)
        #print z, x2-x1, -l*B/(x2-x1)


plt.plot(zl, yl)
plt.show()
