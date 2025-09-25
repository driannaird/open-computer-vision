import os
import cv2

img = cv2.imread(os.path.join('.', 'data', 'dog.jpg'))

print("Image shape:", img.shape)

cropped_img = img[320:640, 420:840]

cv2.imshow('image', img)
cv2.imshow('cropped image', cropped_img)
cv2.waitKey(0)