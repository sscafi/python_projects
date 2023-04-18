import cv2

# Load the video capture device
cap = cv2.VideoCapture(0)

while True:
    # Read a frame from the video capture device
    ret, frame = cap.read()

    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect edges in the grayscale image
    edges = cv2.Canny(gray, 100, 200)

    # Display the original frame and the edge detection result
    cv2.imshow('Original', frame)
    cv2.imshow('Edges', edges)

    # Check for key press to exit the loop
    if cv2.waitKey(1) == ord('q'):
        break

# Release the video capture device and close all windows
cap.release()
cv2.destroyAllWindows()
