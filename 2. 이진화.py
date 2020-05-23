import cv2


img_color = cv2.imread('plan.jpg', cv2.IMREAD_COLOR)

cv2.imshow('Color', img_color)
cv2.waitKey(0)

img_gray = cv2.cvtColor(img_color, cv2.COLOR_BGR2GRAY)

cv2.imshow('Gray', img_gray)
cv2.waitKey(0)

ret,img_binary = cv2.threshold(img_gray, 10, 255, cv2.THRESH_BINARY_INV)

cv2.imshow('Binary', img_binary)
cv2.waitKey(0)

cv2.imwrite('gray10.jpg', img_binary)

cv2.destroyAllWindows()