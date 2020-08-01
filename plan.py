###0_Executing Program =================================================================================================

import sys
import getopt

args = sys.argv[1:]
try:
    opts, args = getopt.getopt(sys.argv, "i:o:h:")
except:
    print("error")
    opts = []

path = './image/plan.jpg'
output = './results/fINAL.jpg'

for opt, arg in opts:
    if opt == "-i":
        path = arg
    elif opt == "-o":
        output = arg
    elif opt == "-h":
        print("-i : Input image file path. Default path is \"%s\"" % path)
        print("-o : output image file path. Default path is \"%s\"" % output)
        sys.exit(1)

###1_Importing Modules and Packages ====================================================================================

import cv2
import numpy as np

###2_reading image File ================================================================================================

img = cv2.imread(path, cv2.IMREAD_COLOR)

###3_convert to gray scale image =======================================================================================

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

###4_binarization ======================================================================================================

ret, img_binary = cv2.threshold(img_gray, 10, 255, cv2.THRESH_BINARY_INV)

###5_eroding and dilating ==============================================================================================


kernel = np.ones((4, 4), np.uint8)

erosion = cv2.erode(img_binary, kernel, iterations=1)
dilation = cv2.dilate(erosion, kernel, iterations=8)
erosion2 = cv2.erode(dilation, kernel, iterations=6)

###6_contrast image ====================================================================================================

ret, img_binary2 = cv2.threshold(erosion2, 10, 255, cv2.THRESH_BINARY_INV)

###7_show  image =======================================================================================================

cv2.imshow('FINAL', img_binary2)
cv2.waitKey(0)
cv2.destroyAllWindows()

###8_saved image =======================================================================================================

cv2.imwrite(output, img_binary2)

print("program finished")
