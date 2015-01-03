import cv2

class Capture:

    def __init__(self, left_cam_index, right_cam_index):
        self.left_index = left_cam_index
        self.right_index = right_cam_index
        self.right = cv2.VideoCapture(left_cam_index) 
        self.left = cv2.VideoCapture(right_cam_index)
        self.callback_function = None

    def set_callback_function(self, callback):
        self.callback_function = callback

    def capture_loop(self):
        if self.callback_function == None:
            return False
        
        while True:
            try:
                img_l, img_r = self.get_images()
                if self.callback_function(img_l, img_r) == False:
                    return True
            except IOError as e:
                print e
                return False

    def get_images(self):
        left_ret, left_img = self.left.read()
        right_ret, right_img = self.right.read()
        
        if left_ret == False:
            raise IOError("Left camera capture error (check camera)!")
        
        if right_ret == False:
            raise IOError("Right camera capture error (check camera)!")
        
        return (left_img, right_img)

    def __del__(self):
        cv2.VideoCapture(self.left_index).release()
        cv2.VideoCapture(self.right_index).release()