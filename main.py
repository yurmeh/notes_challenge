import cv2
import numpy as np

# Load the image
image = cv2.imread('C:\\Users\\TLP-001\\Desktop\\academy\\notes challenge\\pic.jpg', cv2.IMREAD_COLOR)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply preprocessing (e.g., blurring and thresholding)
blurred = cv2.GaussianBlur(gray, (5, 5), 0)
_, thresholded = cv2.threshold(blurred, 0, 0, cv2.THRESH_BINARY)

# Find contours
contours, _ = cv2.findContours(thresholded, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Loop over the contours
for contour in contours:
    # Calculate the area of the contour
    area = cv2.contourArea(contour)

    # Set a threshold for the minimum area to consider
    min_area_threshold = 0

    if area > min_area_threshold:
        print("hello")
        # Check if the contour has at least 5 points
        if len(contour) >= 5:
            print("asda")
            # Fit an ellipse to the contour
            ellipse = cv2.fitEllipse(contour)

            # Draw the ellipse on the original image
            cv2.ellipse(image, ellipse, (0, 255, 0), 2)

# Display the result
cv2.imshow('Filled Circles Detection', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
