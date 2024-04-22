% Step 1: Dataset Preparation

% Define the folder path where temporary images will be stored
tempFolderPath = fullfile(tempdir, 'CutleryPhotos');
mkdir(tempFolderPath);

% Load and assign images to variables
spoonImage = imread('/Users/sonipriyapaul/Downloads/Assignment_3_CV/CutleryPhotos/Spoon.jpg');
forkImage = imread('/Users/sonipriyapaul/Downloads/Assignment_3_CV/CutleryPhotos/Fork.jpg');
knifeImage = imread('/Users/sonipriyapaul/Downloads/Assignment_3_CV/CutleryPhotos/Knife.jpg');
whiskImage = imread('/Users/sonipriyapaul/Downloads/Assignment_3_CV/CutleryPhotos/Whisk.jpg');
ladleImage = imread('/Users/sonipriyapaul/Downloads/Assignment_3_CV/CutleryPhotos/Ladle.jpg');

% Save images to temporary files
imwrite(spoonImage, fullfile(tempFolderPath, 'Spoon.jpg'));
imwrite(forkImage, fullfile(tempFolderPath, 'Fork.jpg'));
imwrite(knifeImage, fullfile(tempFolderPath, 'Knife.jpg'));
imwrite(whiskImage, fullfile(tempFolderPath, 'Whisk.jpg'));
imwrite(ladleImage, fullfile(tempFolderPath, 'Ladle.jpg'));

% Create imageDatastore objects for each object category
spoonImageDatastore = imageDatastore(fullfile(tempFolderPath, 'Spoon.jpg'));
forkImageDatastore = imageDatastore(fullfile(tempFolderPath, 'Fork.jpg'));
knifeImageDatastore = imageDatastore(fullfile(tempFolderPath, 'Knife.jpg'));
whiskImageDatastore = imageDatastore(fullfile(tempFolderPath, 'Whisk.jpg'));
ladleImageDatastore = imageDatastore(fullfile(tempFolderPath, 'Ladle.jpg'));

% Combine all imageDatastore objects into one imageDatastore
allFiles = [spoonImageDatastore.Files; forkImageDatastore.Files; knifeImageDatastore.Files; whiskImageDatastore.Files; ladleImageDatastore.Files];
combinedDatastore = imageDatastore(allFiles);

% Step 2: Feature Extraction

% Define the Bag of Features parameters
bag = bagOfFeatures(combinedDatastore, 'VocabularySize', 500);

% Extract features from each image using the Bag of Features
featuresSpoon = encode(bag, spoonImage);
featuresFork = encode(bag, forkImage);
featuresKnife = encode(bag, knifeImage);
featuresWhisk = encode(bag, whiskImage);
featuresLadle = encode(bag, ladleImage);

% Step 3: Training

% Create labels for the features
labels = [repmat({'spoon'}, size(featuresSpoon, 1), 1);
          repmat({'fork'}, size(featuresFork, 1), 1);
          repmat({'knife'}, size(featuresKnife, 1), 1);
          repmat({'whisk'}, size(featuresWhisk, 1), 1);
          repmat({'ladle'}, size(featuresLadle, 1), 1)];

% Combine features and labels
allFeatures = [featuresSpoon; featuresFork; featuresKnife; featuresWhisk; featuresLadle];

% Train a classifier (e.g., Support Vector Machine) using the extracted features and labels
classifier = fitcecoc(allFeatures, labels);

% Step 4: Testing and Performance Evaluation

% Evaluate the classifier on the training set
predictedLabels = predict(classifier, allFeatures);

% Calculate accuracy
accuracy = sum(strcmp(predictedLabels, labels)) / numel(labels);
disp(['Accuracy: ', num2str(accuracy)]);
