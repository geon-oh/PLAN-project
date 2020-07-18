#0_Executing Program ===================================================================================================

import sys
import getopt

args = sys.argv[1:]
try:
    opts, args=getopt.getopt(argv, "i:o:h:")
except:
    print("error")
    opts=[]


path = "./results/plan.jpg"
output = './results/FINAL.jpg'


for opt, arg in opts:
    if opt == "-i":
        path = arg
    elif opt == "-o":
        output = arg
    elif opt == "-h":
        print("-i : Input image file path. Default path is \"%s\"" % path)
        print("-o : output image file path. Default path is \"%s\"" % output)
        sys.exit(1)

#1_Importing Modules and Packages ======================================================================================

import cv2
import numpy as np

#2_reading image File ==================================================================================================

img = cv2.imread(path, cv2.IMREAD_COLOR)

#3_convert to gray scale image =========================================================================================

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#4_binarization ========================================================================================================

img_binary = cv2.threshold(img_gray, 10, 255, cv2.THRESH_BINARY_INV)

###5_eroding and dilating ==================================================================================================

kernel= np.ones((4, 4), np.uint8)

erode = cv2.erode(img_binary, kernel, iterations=1)

dilate = cv2.dilate(erode , kernel, iterations=8)

erode2 = cv2.erode(dilate, kernel, iterations=6)

#6_contrast image ======================================================================================================

img_binary2 = cv2.threshold(erode2, 10, 255, cv2.THRESH_BINARY_INV)

cv2.imshow('FINAL', img_binary2)
cv2.waitKey(0)

cv2.destroyAllWindows()

