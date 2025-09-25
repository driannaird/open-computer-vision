import os 
import cv2

img = cv2.imread(os.path.join(".", "data", "bird.jpg"))

imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

cv2.imshow("original image", img)
cv2.imshow("RGB image", imgRGB)
cv2.imshow("Gray image", imgGray)
cv2.imshow("HSV image", imgHSV)
cv2.waitKey(0)
cv2.destroyAllWindows()