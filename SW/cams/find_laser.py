import numpy as np
import cv2
import sys
from matplotlib import pyplot as plt

for file_name in sys.argv[1:]:
    img = cv2.imread(file_name, cv2.CV_LOAD_IMAGE_GRAYSCALE)
    cv2.imshow("org", img)
    img = cv2.blur(img, (1, 5))
    ret, thresh1 = cv2.threshold(img, 120, 255, cv2.THRESH_BINARY)
    # cv2.imshow("blur_line", thresh1)
    kernel = np.ones((3, 3), np.uint8)
    erosion = cv2.morphologyEx(thresh1, cv2.MORPH_OPEN, kernel)
    # erosion = cv2.erode(img, kernel)
    cv2.imshow("test", erosion)
    # plt.hist(img.ravel(), 256, [0, 256])
    # plt.show()
    while True:
        key = cv2.waitKey(10)
        if key == 97:
            break
