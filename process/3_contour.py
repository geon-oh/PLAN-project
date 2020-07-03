import cv2 as cv


img_color = cv.imread('FINAL.jpg')
img_gray = cv.cvtColor(img_color, cv.COLOR_BGR2GRAY)
ret, img_binary = cv.threshold(img_gray, 127, 255, 0)
contours, hierarchy = cv.findContours(img_binary, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)


for cnt in contours:
    cv.drawContours(img_color, [cnt], 0, (255, 255, 0), 0)

cv.imshow("result", img_color)

cv.waitKey(0)



for cnt in contours:

    area = cv.contourArea(cnt)

    print(area)


cv.imshow("result", img_color)

cv.waitKey(0)