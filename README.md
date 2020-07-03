## 1. PROJECT
>* **Name : PLAN PROJECT**     
>* **Producer : OH-Geon** 

## 2. OBJECTIVE
> ***"To extract drawings through images"***    
> I thought it would be possible to reduce and automate human labor through the automation of drawings.

## 3. DEPENDENCY
>* **Window10**      
>* **Python 3.8**    
>* **OpenCV**    

## 4. USAGE          
* **0. Importing Libraries**
```
import cv2
import numpy as np
```
* **1. Grayscale**
```
img_color = cv2.imread('plan.jpg', cv2.IMREAD_COLOR)

img_gray = cv2.cvtColor(img_color, cv2.COLOR_BGR2GRAY)

cv2.imwrite('savedimage.jpg', img_gray)
```
* **2. Contrast**
```
img_color = cv2.imread('savedimage.jpg', cv2.IMREAD_COLOR)

img_gray = cv2.cvtColor(img_color, cv2.COLOR_BGR2GRAY)

ret,img_binary = cv2.threshold(img_gray, 10, 255, cv2.THRESH_BINARY_INV)

cv2.imwrite('gray10.jpg', img_binary)
```
* **3. Contours**
```
img_color = cv2.imread('gray10.jpg')
img_gray = cv2.cvtColor(img_color, cv2.COLOR_BGR2GRAY)
ret, img_binary = cv2.threshold(img_gray, 127, 255, 0)
contours, hierarchy = cv2.findContours(img_binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)\

for cnt in contours:
    for p in cnt:
        cv2.circle(img_color, (p[0][0], p[0][1]), 2, (255,0,0), -1)
```
* **4. Erosion**
```
img = cv2.imread('gray10.jpg',0)

kernel = np.ones((4,4), np.uint8)
result = cv2.erode(img, kernel, iterations = 1)

cv2.imwrite('gray30.jpg', result)
```
* **5. Dialation**
```
img = cv2.imread('gray30.jpg',0)

kernel = np.ones((25, 25), np.uint8)
result = cv2.dilate(img, kernel, iterations = 1)

cv2.imwrite('gray40.jpg', result)
```
* **6. Erosion**
```
img = cv2.imread('gray40.jpg',0)

kernel = np.ones((20,20), np.uint8)
result = cv2.erode(img, kernel, iterations = 1)

cv2.imwrite('gray50.jpg', result)
```
* **7. Black & White**
```
img_color = cv2.imread('gray50.jpg', cv2.IMREAD_COLOR)
img_gray = cv2.cvtColor(img_color, cv2.COLOR_BGR2GRAY)

ret,img_binary = cv2.threshold(img_gray, 10, 255, cv2.THRESH_BINARY_INV)

cv2.imshow('Binary', img_binary)
cv2.waitKey(0)

cv2.imwrite('FINAL.jpg', img_binary)

cv2.destroyAllWindows()
```     
           
## 5. RESULT
<img src = "https://github.com/geon-oh/PLAN-project/blob/master/results/plan.jpg" width = "450"> <img src = "https://github.com/geon-oh/PLAN-project/blob/master/results/FINAL.jpg" width = "450">

