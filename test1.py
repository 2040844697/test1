import numpy as np
import cv2
import matplotlib.pyplot as plt

imgo = cv2.imread("YellowStick.jpg",1)
# img = cv2.GaussianBlur(imgo,(5,5),0)
img = imgo
cv2.imshow("oringel", img)

height, width, channel = img.shape

for i in range(height):
    for j in range(width):
        b, g, r = img[i, j]
        if ((abs(r-174)<35 and abs(g-165)<35 and abs(b-44)<35)
                or (abs(r-85)<20 and abs(g-78)<20 and abs(b-32)<35)
                or(abs(r-119)<20 and abs(g-110)<20 and abs(b-31)<35)):
            b = 0
            g = 0
            r = 0
        else:
            b = 255
            g = 255
            r = 255

        img[i, j] = [r, g, b]



kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3,3))
img = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
img = cv2.morphologyEx(img,cv2.MORPH_CLOSE,kernel)
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (7,7))
img = cv2.morphologyEx(img,cv2.MORPH_CLOSE,kernel)



imgG = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

ret, thresh = cv2.threshold(imgG, 175, 255, 0)

image, contours, hier = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)


for item in contours:

    x, y, w, h = cv2.boundingRect(item)






xy = ((x+w)/2,(y+h)/2)

print(xy)
imgo1 = cv2.imread("YellowStick.jpg",1)
cv2.rectangle(imgo1,(x, y), (x + w, y + h), (0, 255, 0), 1)
plt.imshow(imgo1)
plt.show()
cv2.imshow("Result", imgo1)
cv2.imshow("2", thresh)



cv2.waitKey(0)
cv2.destroyAllWindows()
