import cv2
import numpy as np
import random

# Extract frames from the video and append them to frames list
cap = cv2.VideoCapture('/Users/sonipriyapaul/Downloads/Object_Video.mp4')
frames = []
# while True:
#     ret, frame = cap.read()
#     if not ret:
#         break
#     frames.append(frame)

while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    # Display the frame
    cv2.imshow('Video', frame)

    # Appending frames here
    frames.append(frame)

    # User will select ROI (press 's' to stop the video and select)
    key = cv2.waitKey(1) & 0xFF
    if key == ord('s'):
        # Select ROI using mouse drag and then click enter to lock that region in for roi selection process
        roi = cv2.selectROI('Select ROI', frame, fromCenter=False)
        cap.release()
        cv2.destroyAllWindows()
        break

# Choose an image frame
selected_frame = random.choice(frames)

# Identify a region of interest (ROI)
# For testing purposes: manually selected the ROI coordinates
#roi_x, roi_y, roi_w, roi_h = 100, 100, 50, 50

# Extract ROI from the first frame
x, y, w, h = roi
roi_frame = frame[y:y+h, x:x+w]
#print(roi) # To see the difference in coordinates selected for every different frame

# Crop the ROI
roi = selected_frame[y:y+h, x:x+w]

# Selecting only 10 random frames now
random_frames = random.sample(frames, 10)

# Step 7: Calculate similarity metrics
similarity_scores = []
for frame in random_frames:
    # Extract the region corresponding to the ROI
    roi_region = frame[y:y+h, x:x+w]
    
    # Calculate similarity metric (sum of squared differences formula)
    ssd = np.sum((roi.astype("float") - roi_region.astype("float")) ** 2)
    similarity_scores.append(ssd)

# Print the similarity scores
print(similarity_scores)

# Analysis of the results
#Defining a threshold value
threshold = 100000000  # Adjust as needed (setting a high threshold for stricter matching criteria)

# Count the number of matches
num_matches = sum(score > threshold for score in similarity_scores)

# Determine if there's a match based on the number of matches
if num_matches >= 5:  # Adjust threshold for number of matches
    print("Object found in the scene.")
else:
    print("Object not found in the scene.")