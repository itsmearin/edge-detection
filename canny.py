import cv2

# np is an alias pointing to numpy library
import numpy as np

# capture frames from a camera
image = cv2.imread('arin.jpg',0)
heigth


    # Display an original image
    cv2.imshow('Original', frame)

    # finds edges in the input image image and
    # marks them in the output map edges
    edges = cv2.Canny(frame, 100, 200)

    # Display edges in a frame
    cv2.imshow('Edges', edges)

    # Wait for Esc key to stop
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

# Close the window
cap.release()

# De-allocate any associated memory usage
cv2.destroyAllWindows() 