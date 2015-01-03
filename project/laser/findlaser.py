import numpy as np
import cv2
import sys

def get_mask(img_color):
    (_, _, img) = cv2.split(img_color)
    #img = cv2.cvtColor(img_color, cv2.COLOR_BGR2GRAY)
    img = cv2.blur(img, (1, 5))
    ret, img = cv2.threshold(img, 120, 255, cv2.THRESH_BINARY)
    kernel = np.ones((3, 3), np.uint8)
    img = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)

    return img

def main():
    img = cv2.imread(sys.argv[1])
    mask = get_mask(img)
    cv2.imshow("Test mask", mask)
    while True:
        key = cv2.waitKey(10)
        if key == 27:
            break
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()