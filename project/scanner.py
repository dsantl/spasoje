import capture.stereocapture as cap
import laser.findlaser as laser
import distance.stereodistance as distance
import cv2
import matplotlib.pyplot as plt

z_list = []
x_list = []

def image_process(img_l, img_r):
    
    global z_list
    global x_list

    cv2.imshow("right", img_r)
    cv2.imshow("left", img_l)
    
    img_binary_r = laser.get_mask(img_r)
    img_binary_l = laser.get_mask(img_l)
    
    #cv2.imshow("right", img_binary_r)
    #cv2.imshow("left", img_binary_l)
    plt.clf()
    plt.axis([0, 1, 0, 500])
    plt.plot(z_list, x_list)
    plt.draw()
    
    
    key = cv2.waitKey(10)
    if key == ord('a'):
        z_list, x_list = distance.get_distance_height_pair(img_binary_l, img_binary_r)
    elif key == 27:
        return False
    return True

capture = cap.Capture(1, 2)
capture.set_callback_function(image_process)

plt.ion()
plt.show()

capture.capture_loop()
cv2.destroyAllWindows()