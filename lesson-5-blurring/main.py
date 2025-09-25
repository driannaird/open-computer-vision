import os
import cv2

img = cv2.imread(os.path.join('.', 'data', 'bird.jpg'))

k_size = 7

img_blur = cv2.blur(img, (k_size, k_size))
img_gaussian = cv2.GaussianBlur(img, (k_size, k_size), 10)
img_median = cv2.medianBlur(img, k_size)

cv2.imshow('original image', img)
cv2.imshow('blurred image', img_blur)
cv2.imshow('gaussian image', img_gaussian)
cv2.imshow('median image', img_median)

cv2.waitKey(0)
cv2.destroyAllWindows()