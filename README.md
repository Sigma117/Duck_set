# Duck_set
How to create a dataset to train a neural network to detect the roadway lines using Python

In this repository, I will explain how to create a dataset by extracting images from videos using Python. The dataset obtained with this procedure was used to train the CNN presented in [github Link](https://github.com/Sigma117/Robust-Lane-Detection), which had some specific requirements. Thus, if you need to create a dataset for another CNN, you will probably have some different requirements; however, some steps of my procedure may anyway be useful. 
The whole image extraction process was developed in Python via the following steps: 

1) **Resize video to 256x128 format.** This first step is necessary to extract images with a size of 256x128 pixels, as required by the neural network I  used. For this purpose, the video_size function is created. Then, through a for loop, all the videos are resized using the function just described and are duplicated in 256x128 format, not overwritten to the original videos. The Python script for this step is called chaging_Video_Resolution.py;

2) **Resized videos are trimmed to four second video length.** This step is done to have the same duration for all the videos, in order to simplify the following steps. Again, the new four-second videos are not overwritten to the previous ones, but have been duplicated. The Python script for this step is called Split_Video.py;

3) **Extract frames from the videos.** Twenty frames are obtained from each four-second video and are saved in a specially-created folder, which has the same name as the video from which the frames derive. The Python script for this step is called frame selection_v2.py;

4) **Create labels.** The 13th and 20th frames of each video were copied to a specific folder and then processed with a photo editing program in order to create the labels (unfortunately the labeling process needs to be done by hand XD). The Python script for this step is called take_13,20.py;

5) **Conversion of the labels in grayscale.** This step is necessary since the labels, which have been extracted directly from the starting videos, are colored, while the neural network that I used, required labels in grayscale. The Python script for this step is called MetaData_img.py;

6) **Creation of txt files for training.** Finally, the train_index and val_index txt files were created for training. The Python script for this step is called MetaData_img.py.

The next two images show how the folders should appear after the preocess is completed. The third image shows how the txt file train_index looks like. 
 
<img width="500" alt="Schermata 2022-05-11 alle 23 01 46" src="https://user-images.githubusercontent.com/71655239/167947806-928a1c74-8f61-41d8-8c68-b1c14422f001.png">  <img width="500" alt="Schermata 2022-05-11 alle 23 01 53" src="https://user-images.githubusercontent.com/71655239/167947815-3f646585-23f5-4ba5-a937-4952b1939374.png">
<img width="1400" alt="Schermata 2022-05-11 alle 23 04 16" src="https://user-images.githubusercontent.com/71655239/167947826-84d77f65-086b-40c9-931a-33f16ed22972.png">
