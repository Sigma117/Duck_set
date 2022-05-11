import numpy as np
import cv2
import glob
import os

#script che permette di confertire i video in 256 x 128
# da un errore che non compredo

def video_resize(input_path, output_path):
    cap = cv2.VideoCapture(input_path)

    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter(output_path, fourcc, 30.0, (256, 128))  # se ci metti output.mp4v non sa errore ma non esce l'output

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


#video_resize("20160408151056_ayrton.video.mp4","1.mp4")

all_video = [i for i in glob.glob("*.mp4")]
j = 1
for i in all_video:
    output = str(j) + ".mp4"
    video_resize(i, output)  #[:-4] dalla fine -4 lettere
    j = j+1

print("done")



#print (all_video)
#print (len(all_video))