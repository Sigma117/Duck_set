import os
import numpy as np
import glob

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
