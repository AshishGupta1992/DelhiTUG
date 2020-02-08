import cv2
import numpy as np

image = cv2.imread("pancard6.jpg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

blurr1 = cv2.GaussianBlur(gray, (5, 5), 0)
blurr2 = cv2.medianBlur(gray, 3)

thresh1 = cv2.threshold(blurr1, 0, 255,
                                cv2.THRESH_OTSU)[1]
thresh2 = cv2.threshold(blurr1,127,255,cv2.THRESH_BINARY)[1]
thresh3 = cv2.threshold(blurr1,127,255,cv2.THRESH_BINARY_INV)[1]
thresh4 = cv2.threshold(blurr1,127,255,cv2.THRESH_TRUNC)[1]
thresh5 = cv2.threshold(blurr1,127,255,cv2.THRESH_TOZERO)[1]
thresh6 = cv2.threshold(blurr1,127,255,cv2.THRESH_TOZERO_INV)[1]

cv2.imshow("Image", image)
cv2.imshow("Gray", gray)
cv2.imshow("Gaussian", blurr1)
cv2.imshow("Median", blurr2)
cv2.imshow("Thresh Otsu", thresh1)
cv2.imshow("Thresh Binary", thresh2)
cv2.imshow("Thresh Binary Inv", thresh3)
cv2.imshow("Thresh Trunc", thresh4)
cv2.imshow("Thresh ToZero", thresh5)
cv2.imshow("Thresh Tozero_Inv", thresh6)



cv2.waitKey(0)
cv2.destroyAllWindows()
