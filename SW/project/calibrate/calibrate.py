import numpy as np
import cv2
import cv2.cv as cv

circle_number = 5
img_resize = (640, 480)
param1 = 200
param2 = 30

def translate_y_img(img_l, y_l, y_r):

    rows,cols = img_l.shape
    
    delta_y = np.average(y_r - y_l)
    M = np.float32([[1,0,0],[0,1,delta_y]])
   
    return cv2.warpAffine(img_l, M, (cols,rows))
    

def fit_scale_rotation(img_l, img_r, d1, r1, d2, r2):
    
    rows,cols = img_l.shape
    
    resize = r1/r2

    M1 = cv2.getRotationMatrix2D((cols/2,rows/2), d1, 1)
    M2 = cv2.getRotationMatrix2D((cols/2,rows/2), d2, resize)
    
    img_l = cv2.warpAffine(img_l, M1, (cols,rows))
    img_r = cv2.warpAffine(img_r, M2, (cols,rows)) 

    return (img_l, img_r)


def get_degree_radius(img):

    img = cv2.resize(img, img_resize)
    rows,cols = img_resize
    circles = cv2.HoughCircles(img,cv.CV_HOUGH_GRADIENT, 1, 20 , param1=param1, param2=param2)

    if circles is None:
        return None

    if len(circles[0,:]) != circle_number:
        return None

    circles = np.uint16(np.around(circles))
    x = []
    y = []
    radius = []
    for i in circles[0,:]:
        y.append(i[0])
        x.append(i[1])
        radius.append(i[2])

    x = np.array(x)
    A = np.array([x, np.ones(circle_number)])
    w = np.linalg.lstsq(A.T,y)[0]
    avg_radius = np.average(radius)
    
    degree = np.degrees(np.arctan(w[0]))
    
    
    return (-degree, avg_radius, x)

def main():
    #right = cv2.VideoCapture(1) 
    #left = cv2.VideoCapture(2)

    #cal_r = None
    #cal_l = None

    #while(True):
    img_l = cv2.imread("cali_left.png") #left.read()
    img_r = cv2.imread("cali_right.png") #right.read()
    cv2.imshow("org_l", img_l)
    cv2.imshow("org_r", img_r)

    img_l = cv2.cvtColor(img_l, cv2.COLOR_BGR2GRAY)
    img_r = cv2.cvtColor(img_r, cv2.COLOR_BGR2GRAY)

    p1 = get_degree_radius(img_l)
    p2 = get_degree_radius(img_r)

    if (p1 is not None) and (p2 is not None):
        (d1, r1, y1) = p1
        (d2, r2, y2) = p2
        print d1, r1
        print d2, r2
        img_l, img_r = fit_scale_rotation(img_l, img_r, d1, r1, d2, r2) 
        #cal_l = translate_y_img(cal_l, y1, y2)

    cv2.imshow("l", img_l)
    cv2.imshow("r", img_r)

    key = cv2.waitKey(0)

    #if key == 27:
    #    break


if __name__ =="__main__":
    main()