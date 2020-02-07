import cv2
import numpy as np

image = cv2.imread("pancard6.jpg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

kernel = np.ones((3, 3), np.uint8)
dilate = cv2.dilate(gray, kernel, iterations=2)
erosion = cv2.erode(gray, kernel, iterations=2)


cv2.imshow("Image", image)
cv2.imshow("Gray", gray)
cv2.imshow("Dilation", dilate)
cv2.imshow("Erosion", erosion)

cv2.waitKey(0)
cv2.destroyAllWindows()
