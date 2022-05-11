import numpy as np
import cv2
import glob
import os

def video_resize(input_path, output_path):
    cap = cv2.VideoCapture(input_path)

    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter(output_path, fourcc, 30.0, (256, 128))

    while True:
        ret, frame = cap.read()
        if ret == True:
            b = cv2.resize(frame, (256, 128), fx=0, fy=0, interpolation=cv2.INTER_CUBIC)
            out.write(b)

        else:
            break

    cap.release()
    out.release()
    cv2.destroyAllWindows()




all_video = [i for i in glob.glob("*.mp4")]
j = 1
for i in all_video:
    output = str(j) + ".mp4"
    video_resize(i, output)  
    j = j+1

print("done")
