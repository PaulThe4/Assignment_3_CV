% Load the video file
videoFile = 'Object_Video.mp4';
videoReader = VideoReader(videoFile);

% Read the first frame
prevFrame = readFrame(videoReader);

% Convert the first frame to grayscale
prevFrameGray = rgb2gray(prevFrame);

% Process the video frame by frame
while hasFrame(videoReader)
    % Read the current frame
    currFrame = readFrame(videoReader);
    
    % Convert the current frame to grayscale
    currFrameGray = rgb2gray(currFrame);
    
    % Compute optical flow using the Farneback method
    flow = estimateFlow(opticalFlowFarneback, currFrameGray);
    
    % Plot optical flow vectors on the current frame
    imshow(currFrame);
    hold on;
    plot(flow, 'DecimationFactor', [10 10], 'ScaleFactor', 2);
    title('Optical Flow');
    hold off;
    
    % Pause to display the frame
    pause(0.1);
end