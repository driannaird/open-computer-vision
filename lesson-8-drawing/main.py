import os
import cv2

img = cv2.imread(os.path.join(".", "data", "whiteboard.webp"))

# line
img_line = cv2.line(img, (100, 150), (300, 350), (0, 255, 0), 3)

# rectangle
img_rect = cv2.rectangle(img_line, (200, 200), (400, 400), (255, 0, 0), 2)

# circle
img_circle = cv2.circle(img_rect, (400, 100), 50, (0, 0, 255), cv2.FILLED)

# text
img_text = cv2.putText(img_circle, "OpenCV", (50, 200), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 1, (0, 0, 0), 2)

# cv2.imshow("Image", img)
cv2.imshow("Text", img_text)
cv2.waitKey(5000)
cv2.destroyAllWindows()