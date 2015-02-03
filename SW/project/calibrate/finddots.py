import numpy as np
import cv2
import cv2.cv as cv
import sys
from pylab import plot,show


def calibrate(img):

    #img = cv2.imread("cali.png")
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img = cv2.resize(img, (640, 480))

    rows,cols = img.shape

    #M = cv2.getRotationMatrix2D((cols/2,rows/2), 15,1)
    #img = cv2.warpAffine(img,M,(cols,rows))

    #cv2.imshow("test", img)
    #cv2.waitKey(0)

    cimg = cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)
    circles = cv2.HoughCircles(img,cv.CV_HOUGH_GRADIENT, 1, 20 , param1=200, param2=30)

    if circles is None:
        return cimg

    if len(circles[0,:]) != 5:
        return cimg

    circles = np.uint16(np.around(circles))
    
    x = []
    y = []
    radius = []

    for i in circles[0,:]:
        y.append(i[0])
        x.append(i[1])
        radius.append(i[2])
        cv2.circle(cimg,(i[0],i[1]),i[2],(0,255,0),2)
        cv2.circle(cimg,(i[0],i[1]),2,(0,0,255),3)

    #print x
    #print y

    x = np.array(x)
    A = np.array([x, np.ones(5)])
    w = np.linalg.lstsq(A.T,y)[0]
    avg_radius = np.average(radius)
    
    #print w[0]
    degree = np.degrees(np.arctan(w[0]))
    print degree
    M = cv2.getRotationMatrix2D((cols/2,rows/2), -degree, 1)
    img = cv2.warpAffine(img,M,(cols,rows))

    return img
    

def main():
    cam = cv2.VideoCapture(1)
        
    while True:
        r, img = cam.read()
        cv2.imshow("org", img)
        img = calibrate(img)
        cv2.imshow("calibrate", img)
        key = cv2.waitKey(100)
        if key == 27:
            break

if __name__ == "__main__":
    main()