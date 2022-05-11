import os
import numpy as np
import glob



#crea una cartella prende 20 frame da 4 secondi di video e poi li mette nella cartella creata che ha lo stesso nome del video caricato senza estensione

all_video = [i for i in glob.glob("*.mp4")]

j = 1
for i in all_video:
    bashCommand_Frame = ("ffmpeg -i {} -vf thumbnail=6,setpts=N/TB -r 1 -vframes 20 {}_%02d.jpg".format(i, i[:-4]))
    bashCommand_mkdir = ("mkdir {}".format(i[:-4]))


    os.system(bashCommand_mkdir)
    os.system(bashCommand_Frame)
    all_frame = [x for x in glob.glob("*.jpg")]
    print(all_video)
    print(all_frame)
    j = j+1
    for k in all_frame:
        bashCommand_mv = ("mv {} {}".format(k, i[:-4]))
        os.system(bashCommand_mv)

print("done")


#os.system("mv 3_3_001.jpeg 3_3")

#https://stackoverflow.com/questions/35912335/how-to-extract-a-fixed-number-of-frames-with-ffmpeg
#https://stackoverflow.com/questions/32047137/need-to-use-a-variable-in-an-os-system-command-in-python
#https://stackoverflow.com/questions/4256107/running-bash-commands-in-python/51950538

