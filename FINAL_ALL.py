
import sys
import getopt

args = sys.argv[1:]
opts, args = getopt.getopt(args, 'r:g:b:p:o:h')



path = "./images/sample1.jpg"
output = './output.gif'




#0 =======================================================================================================

import cv2
import numpy as np




#1 black & white==========================================================================================


img_color = cv2.imread('results/plan.jpg', cv2.IMREAD_COLOR)

img_gray = cv2.cvtColor(img_color, cv2.COLOR_BGR2GRAY)

cv2.imwrite('results/savedimage.jpg', img_gray)



#2 =======================================================================================================

img_color = cv2.imread('results/savedimage.jpg', cv2.IMREAD_COLOR)

img_gray = cv2.cvtColor(img_color, cv2.COLOR_BGR2GRAY)

ret,img_binary = cv2.threshold(img_gray, 10, 255, cv2.THRESH_BINARY_INV)

cv2.imwrite('results/gray10.jpg', img_binary)




#3 =======================================================================================================

img = cv2.imread('results/gray10.jpg',0)

kernel = np.ones((4,4), np.uint8)
result = cv2.erode(img, kernel, iterations = 1)

cv2.imwrite('results/gray20.jpg', result)




#4 =======================================================================================================

img = cv2.imread('results/gray20.jpg',0)

kernel = np.ones((25, 25), np.uint8)
result = cv2.dilate(img, kernel, iterations = 1)

cv2.imwrite('results/gray30.jpg', result)




#5 =======================================================================================================

img = cv2.imread('results/gray30.jpg',0)

kernel = np.ones((20,20), np.uint8)
result = cv2.erode(img, kernel, iterations = 1)

cv2.imwrite('results/gray40.jpg', result)




#6 =======================================================================================================

img_color = cv2.imread('results/gray40.jpg', cv2.IMREAD_COLOR)
img_gray = cv2.cvtColor(img_color, cv2.COLOR_BGR2GRAY)

ret,img_binary = cv2.threshold(img_gray, 10, 255, cv2.THRESH_BINARY_INV)

cv2.imshow('Binary', img_binary)
cv2.waitKey(0)

cv2.imwrite('results/FINAL.jpg', img_binary)

cv2.destroyAllWindows()

