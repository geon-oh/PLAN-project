import cv2 as cv

img_color = cv.imread('gray10.jpg')
img_gray = cv.cvtColor(img_color, cv.COLOR_BGR2GRAY)
ret, img_binary = cv.threshold(img_gray, 127, 255, 0)
contours, hierarchy = cv.findContours(img_binary, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)\

for cnt in contours:
    for p in cnt:
        cv.circle(img_color, (p[0][0], p[0][1]), 2, (255,0,0), -1)

cv.imshow("result", img_color)
cv.waitKey(0)