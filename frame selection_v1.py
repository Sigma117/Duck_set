import os
import numpy as np
import glob




bashCommand="mkdir 3_1"
#bashCommand1=" ffmpeg -i *.mp4 -vf thumbnail=6,setpts=N/TB -r 1 -vframes 20 3_%03d.jpeg"

all_video = [i for i in glob.glob("*.mp4")]

j = 1
for i in all_video:
    bashCommand1 = ("ffmpeg -i {} -vf thumbnail=6,setpts=N/TB -r 1 -vframes 20 {}_%03d.jpeg".format(i,i[:-4]))
    os.system(bashCommand1)
    j = j+1

print("done")

#https://stackoverflow.com/questions/35912335/how-to-extract-a-fixed-number-of-frames-with-ffmpeg
#https://stackoverflow.com/questions/32047137/need-to-use-a-variable-in-an-os-system-command-in-python
#https://stackoverflow.com/questions/4256107/running-bash-commands-in-python/51950538

