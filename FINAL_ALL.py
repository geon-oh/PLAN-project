
import sys
import getopt


def help():
    print
    "print help usage"
    return

def main():
    try:
        opts, args = getopt.getopt(sys.argv[1:], "abchi:o:", ["input=", "output=", "help"])
    except getopt.GetoptError as err:
        print
        str(err)
        help()
        sys.exit(1)

    for opt, arg in opts:
        if (opt == "-a"):
            print
            "a option enabled"
        elif (opt == "-b"):
            print
            "b option enabled"
        elif (opt == "-c"):
            print
            "c option enabled"
        elif (opt == "-i") or (opt == "--input"):
            print
            "input file = " + arg
        elif (opt == "-o") or (opt == "--output"):
            print
            "ouput file = " + arg
        elif (opt == "-h") or (opt == "--help"):
            help()

    return


if __name__ == '__main__':
    main()


#0 =======================================================================================================

import cv2
import numpy as np


#1 =======================================================================================================

img_color = cv2.imread('plan.jpg', cv2.IMREAD_COLOR)

img_gray = cv2.cvtColor(img_color, cv2.COLOR_BGR2GRAY)

cv2.imwrite('savedimage.jpg', img_gray)




#2 =======================================================================================================

img_color = cv2.imread('savedimage.jpg', cv2.IMREAD_COLOR)

img_gray = cv2.cvtColor(img_color, cv2.COLOR_BGR2GRAY)

ret,img_binary = cv2.threshold(img_gray, 10, 255, cv2.THRESH_BINARY_INV)

cv2.imwrite('gray10.jpg', img_binary)




#3 =======================================================================================================

img_color = cv2.imread('gray10.jpg')
img_gray = cv2.cvtColor(img_color, cv2.COLOR_BGR2GRAY)
ret, img_binary = cv2.threshold(img_gray, 127, 255, 0)
contours, hierarchy = cv2.findContours(img_binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)\

for cnt in contours:
    for p in cnt:
        cv2.circle(img_color, (p[0][0], p[0][1]), 2, (255,0,0), -1)




#4 =======================================================================================================

img = cv2.imread('gray10.jpg',0)

kernel = np.ones((4,4), np.uint8)
result = cv2.erode(img, kernel, iterations = 1)

cv2.imwrite('gray30.jpg', result)




#5 =======================================================================================================

img = cv2.imread('gray30.jpg',0)

kernel = np.ones((25, 25), np.uint8)
result = cv2.dilate(img, kernel, iterations = 1)

cv2.imwrite('gray40.jpg', result)




#6 =======================================================================================================

img = cv2.imread('gray40.jpg',0)

kernel = np.ones((20,20), np.uint8)
result = cv2.erode(img, kernel, iterations = 1)

cv2.imwrite('gray50.jpg', result)




#7 =======================================================================================================

img_color = cv2.imread('gray50.jpg', cv2.IMREAD_COLOR)
img_gray = cv2.cvtColor(img_color, cv2.COLOR_BGR2GRAY)

ret,img_binary = cv2.threshold(img_gray, 10, 255, cv2.THRESH_BINARY_INV)

cv2.imshow('Binary', img_binary)
cv2.waitKey(0)

cv2.imwrite('FINAL.jpg', img_binary)

cv2.destroyAllWindows()

