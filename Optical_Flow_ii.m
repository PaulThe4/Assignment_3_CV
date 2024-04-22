% Load the video file
videoFile = 'Object_Video.mp4';
videoReader = VideoReader(videoFile);

% Create an optical flow object
opticFlow = opticalFlowFarneback();

% Read the first frame
referenceFrame = readFrame(videoReader);

% Process the video frame by frame
frameCount = 1;
while hasFrame(videoReader)
    % Read the current frame
    currFrame = readFrame(videoReader);
    
    % Compute optical flow using the reference frame as reference
    if mod(frameCount, 11) == 0
        flow = estimateFlow(opticFlow, rgb2gray(currFrame), rgb2gray(referenceFrame));
    else
        flow = estimateFlow(opticFlow, rgb2gray(currFrame));
    end
    
    % Plot optical flow vectors on the current frame
    imshow(currFrame);
    hold on;
    plot(flow, 'DecimationFactor', [10 10], 'ScaleFactor', 2);
    title('Optical Flow');
    hold off;
    
    % Pause to display the frame
    pause(0.1);
    
    % Update the reference frame if necessary
    if mod(frameCount, 11) == 0
        referenceFrame = currFrame;
    end
    
    % Increment frame count
    frameCount = frameCount + 1;
end