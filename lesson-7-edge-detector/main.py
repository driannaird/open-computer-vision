import os
import cv2
import numpy as np

img = cv2.imread(os.path.join('.', 'data', 'basketball.jpg'))

edges = cv2.Canny(img, 100, 200)

img_dilated = cv2.dilate(edges, np.ones((3, 3), dtype=np.uint8))

img_eroded = cv2.erode(img_dilated, np.ones((3, 3), dtype=np.uint8))

cv2.imshow('original image', img)
cv2.imshow('edges', edges)
cv2.imshow('dilated edges', img_dilated)
cv2.imshow('eroded edges', img_eroded)
cv2.waitKey(0)
cv2.destroyAllWindows()