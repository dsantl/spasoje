import numpy as np
import cv2


cap_right = cv2.VideoCapture(1)
cap_left = cv2.VideoCapture(2)

counter = 1

while True:
    ret, img_r = cap_right.read()
    ret, img_l = cap_left.read()
    cv2.imshow("right", img_r)
    cv2.imshow("left", img_l)
    key = cv2.waitKey(10)
    if key == 97:
        print "save..."
        cv2.imwrite("./test/imgR"+str(counter)+".jpg", img_r)
        cv2.imwrite("./test/imgL"+str(counter)+".jpg", img_l)
    if key == 27:
        break
    counter += 1

cv2.destroyAllWindows()
cv2.VideoCapture(0).release()
