# Assignment_3_CV

This repository contains the solutions for the assignment comprising various computer vision tasks. Below are the details of each problem.

Problem 1: Object Matching in Video Footage

Description:
Captured a 10-second video footage of a blue water bottle by panning the camera slightly from left to right or right to left.
Picked an image frame from the video and selected a region of interest corresponding to the object from the UI.
Cropped the region and compared it with 10 randomly picked images from other frames appended from the video using SSD or normalized correlation.
Files:
Object_Video.mp4: The video of the object.
Dataset: 10-second video frames dataset.


Problem 2: Motion Tracking Equation and Lucas-Kanade Algorithm

Description:
Derived the motion tracking equation from fundamental principles.
Computed motion function estimates using 2 consecutive frames from the dataset.
Derived the procedure for performing Lucas-Kanade algorithm for affine motion tracking.



Problem 3: Disparity-Based Depth Estimation

Description:
Fixed a marker on a wall or flat vertical surface and captured an image from distance D.
Translated the camera horizontally by T units and captured another image.
Computed D using disparity-based depth estimation in stereo-vision theory.


Problem 4: Optical Flow Visualization

Description:
Plotted optical flow vectors on each frame of the video.
Treated every previous frame, every 11th frame, and every 31st frame as a reference frame.


Problem 5: Feature-Based Matching Object Detection

Description:
Ran feature-based matching object detection on the images from Problem 1.


Problem 6: Bag of Features Object Recognition

Description:
Implemented Bag of Features object recognition for household objects.
Picked 5 object types and evaluate performance. Images provided.


Problem 7: Uncalibrated Stereo Rectification

Description:
Captured image pairs and rotate camera 2 towards camera 1 after translation.
Used MATLAB's tutorial for uncalibrated stereo rectification.

Problem 8: Real-Time Object Tracker

Description:
Implemented a real-time object tracker with and without markers.
Used QR codes or April tags (aruco markers) for marker-based tracking.
