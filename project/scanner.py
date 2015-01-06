import capture.stereocapture as cap
import laser.findlaser as laser
import distance.stereodistance as distance
import cv2
import matplotlib.pyplot as plt
import sys

z_list = []
y_list = []

def image_process(img_l, img_r):
    
    global z_list
    global y_list

    cv2.imshow("right_o", img_r)
    cv2.imshow("left_o", img_l)
    
    img_binary_r = laser.get_mask(img_r)
    img_binary_l = laser.get_mask(img_l)
    
    #cv2.imshow("right", img_binary_r)
    #cv2.imshow("left", img_binary_l)

    plt.clf()
    #plt.axis([0, 1, 0, 500])
    plt.plot(z_list, y_list)
    plt.draw()
    
    key = cv2.waitKey(10)
    #if key == ord('a'):
    z_list, y_list = distance.get_distance_height_pair(img_binary_l, img_binary_r)
    
    if key == 27:
        return False
    return True

capture = cap.Capture(1, 2)
capture.set_callback_function(image_process)

plt.ion()
plt.show()

capture.capture_loop()
cv2.destroyAllWindows()
