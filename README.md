# Duck_set-
How to create a dataset to train a neural network to detect the roadway lines using Python

In this repository, I will explain how to create a dataset by extracting images from videos using Python. The dataset obtained with this procedure was used to train the CNN presented in [github Link](https://github.com/Sigma117/Robust-Lane-Detection), which had some specific requirements. Thus, if you need to create a dataset for another CNN, you will probably have some different requirements; however, some steps of my procedure may anyway be useful. 
The whole image extraction process was developed in Python via the following steps: 

1) **Resize video to 256x128 format.** This first step is necessary to extract images with a size of 256x128 pixels, as required by the neural network I  used. For this purpose, the video_size function is created. Then, through a for loop, all the videos are resized using the function just described and are duplicated in 256x128 format, not overwritten to the original videos;

2) **Resized videos are trimmed to four second video length.** This step is done to have the same duration for all the videos, in order to simplify the following steps. Again, the new four-second videos are not overwritten to the previous ones, but have been duplicated;

3) **Extract frames from the videos.** Twenty frames are obtained from each four-second video and are saved in a specially-created folder, which has the same name as the video from which the frames derive;

4) **Create labels.** The 13th and 20th frames of each video were copied to a specific folder and then processed with a photo editing program in order to create the labels (unfortunately the labeling process needs to be done by hand XD);

5) **Conversion of the labels in grayscale.** This step is necessary since the labels, which have been extracted directly from the starting videos, are colored, while the neural network that I used, required labels in grayscale;

6) **Creation of txt files for training.** Finally, the train_index and val_index txt files were created for training.
