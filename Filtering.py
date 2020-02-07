import cv2
import numpy as np

image = cv2.imread("pancard6.jpg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

blurr1 = cv2.GaussianBlur(gray, (5, 5), 0)
blurr2 = cv2.medianBlur(gray, 3)

cv2.imshow("Image", image)
cv2.imshow("Gray", gray)
cv2.imshow("Blurr", blurr1)
cv2.imshow("Blurr", blurr2)


cv2.waitKey(0)
cv2.destroyAllWindows()
