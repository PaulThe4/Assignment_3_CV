import cv2

# Initialize feature extractor (e.g., ORB)
orb = cv2.ORB_create()

# Initialize feature matcher (e.g., brute-force matcher)
bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

# Path to the video file
video_file = 'Object_Video.mp4'

# Capture video stream
cap = cv2.VideoCapture(video_file)

# Read and process frames
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Convert frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect keypoints and compute descriptors
    keypoints, descriptors = orb.detectAndCompute(gray, None)

    # Track keypoints in subsequent frames
    if 'prev_keypoints' in locals():
        # Match keypoints between current and previous frames
        matches = bf.match(descriptors, prev_descriptors)
        # Sort matches by distance
        matches = sorted(matches, key=lambda x: x.distance)
        # Draw matches
        matched_frame = cv2.drawMatches(frame, keypoints, prev_frame, prev_keypoints, matches[:10], None, flags=cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)
        # Display frame with matches
        cv2.imshow('Object Tracker', matched_frame)
    else:
        # Save keypoints and descriptors for next frame
        prev_keypoints = keypoints
        prev_descriptors = descriptors
        prev_frame = frame

    # Update previous keypoints and descriptors
    prev_keypoints = keypoints
    prev_descriptors = descriptors
    prev_frame = frame

    # Quit if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release video capture and close windows
cap.release()
cv2.destroyAllWindows()