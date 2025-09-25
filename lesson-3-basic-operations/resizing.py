import os 
import cv2

# Read the image
image_path = os.path.join(".", "data", "dog.jpg")
image = cv2.imread(image_path)

image_resized = cv2.resize(image, (640, 480))

print("Image shape:", image.shape)
print("Resized image shape:", image_resized.shape)

cv2.imshow("image", image)
cv2.imshow("resized image", image_resized)
cv2.waitKey(0)