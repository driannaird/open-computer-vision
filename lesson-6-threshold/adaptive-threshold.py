import os
import cv2

img = cv2.imread(os.path.join('.', 'data', 'handwritten.jpg'))

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

thres = cv2.adaptiveThreshold(img_gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 21, 30)
ret, simple_thres = cv2.threshold(img_gray, 127, 255, cv2.THRESH_BINARY)

cv2.imshow('original image', img)
cv2.imshow('threshold image', thres)
cv2.imshow('simple threshold image', simple_thres)
cv2.waitKey(0)
cv2.destroyAllWindows()