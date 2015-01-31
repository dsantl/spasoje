import numpy as np
import cv2
import sys
from matplotlib import pyplot as plt

cap_right = cv2.VideoCapture(2)

while True:
    ret, img = cap_right.read()
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # img = cv2.imread(file_name, cv2.CV_LOAD_IMAGE_GRAYSCALE)
    cv2.imshow("org", img)
    img = cv2.blur(img, (1, 5))
    ret, thresh1 = cv2.threshold(img, 220, 255, cv2.THRESH_BINARY)
    # cv2.imshow("blur_line", thresh1)
    kernel = np.ones((3, 5), np.uint8)
    erosion = cv2.morphologyEx(thresh1, cv2.MORPH_OPEN, kernel)
    cv2.imshow("test", erosion)
    # plt.hist(img.ravel(), 256, [0, 256])
    # plt.show()
    histr = cv2.calcHist([img], [0], None, [256], [0, 256])
    post = np.sum(histr) * 0.9
    suma = 0
    j = 0
    for i in histr:
        suma += i
        if suma > post:
            print j
            break
        j += 1
    key = cv2.waitKey(10)
    if key == 97:
        break
