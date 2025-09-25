import os
import cv2

img = cv2.imread(os.path.join('.', 'data', 'bird.jpg'))

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret, thres = cv2.threshold(img_gray, 80, 255, cv2.THRESH_BINARY)

cv2.imshow('original image', img)
cv2.imshow('threshold image', thres)
cv2.waitKey(0)
cv2.destroyAllWindows()