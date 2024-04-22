import cv2 as cv
import numpy as np

# Load the predefined dictionary of ArUco markers
aruco_dict = cv.aruco.getPredefinedDictionary(cv.aruco.DICT_6X6_250)
#aruco_dict = cv.aruco.Dictionary_get(cv.aruco.DICT_6X6_250)

# Create a detector with default parameters
aruco_params = cv.aruco.DetectorParameters()

# Open a video capture device (e.g., webcam)
cap = cv.VideoCapture(0)

while True:
    # Read a frame from the video capture
    ret, frame = cap.read()
    if not ret:
        break

    # Detect ArUco markers in the frame
    corners, ids, _ = cv.aruco.detectMarkers(frame, aruco_dict, parameters=aruco_params)

    # Draw detected markers on the frame
    if ids is not None:
        cv.aruco.drawDetectedMarkers(frame, corners, ids)

    # Display the frame
    cv.imshow('Frame', frame)

    # Break the loop if 'q' is pressed
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture device and close OpenCV windows
cap.release()
cv.destroyAllWindows()