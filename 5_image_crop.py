import cv2

src = cv2.imread("gray10.jpg", cv2.IMREAD_COLOR)

dst = src.copy()
dst = src[40:605, 175:780]

cv2.imshow("src", src)
cv2.imshow("dst", dst)
cv2.waitKey(0)
cv2.destroyAllWindows()

ret,img_binary = cv2.threshold(dst, 10, 255, cv2.THRESH_BINARY_INV)

cv2.imwrite("gray20.jpg", img_binary)