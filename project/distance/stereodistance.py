import numpy as np
import cv2

def avg(lst):
    suma = sum(lst)
    return suma / float(len(lst))


def get_distance_height_pair(img_l, img_r):

    height = img_l.shape[0]
    width = img_l.shape[1]
    B = 100.0

    ind = np.indices((height, width))[1]
    ones = np.ones((width, 1))

    ind_l = np.multiply(img_l, ind)
    ind_r = np.multiply(img_r, ind)


    x_l = np.dot(ind_l, ones) / float(width)
    x_r = np.dot(ind_r, ones) / float(width)

    yl = np.arange(0, height, 1)
    yl = yl[::-1]

    dx = x_l - x_r
    
    zl = -B / dx

    return (zl, yl)
