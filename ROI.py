import cv2

# Load the video
cap = cv2.VideoCapture('/Users/sonipriyapaul/Downloads/Object_Video.mp4')

# Play the video and select ROI
while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    # Display the frame
    cv2.imshow('Video', frame)
    
    # Wait for user to select ROI (press 's' to select)
    key = cv2.waitKey(1) & 0xFF
    if key == ord('s'):
        # Select ROI using mouse drag
        roi = cv2.selectROI('Select ROI', frame, fromCenter=False)
        cv2.destroyAllWindows()
        break

# Extract ROI from the first frame
x, y, w, h = roi
roi_frame = frame[y:y+h, x:x+w]

# Save the ROI as an image
cv2.imwrite('/Users/sonipriyapaul/Downloads/roi_image.png', roi_frame)

# Release the video capture object
cap.release()
cv2.destroyAllWindows()