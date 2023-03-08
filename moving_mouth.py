import cv2

# Load the image
img = cv2.imread('image.jpg')

# Define the location of the mouth
mouth_cascade = cv2.CascadeClassifier('haarcascade_mouth.xml')
mouth_rects = mouth_cascade.detectMultiScale(img, 1.3, 5)

# Loop through each mouth rectangle and apply changes to the image
for (x, y, w, h) in mouth_rects:
    # Draw a rectangle around the mouth
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)

    # Add a black rectangle below the mouth
    cv2.rectangle(img, (x, y + h), (x + w, y + h + int(h / 2)), (0, 0, 0), -1)

# Display the modified image
cv2.imshow('Talking Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
