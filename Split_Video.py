import os
import numpy as np
import glob

bashCommand="mkdir 3_1"


all_video = [i for i in glob.glob("*.mp4")]

j = 1
for i in all_video:
    bashCommand1 = ("ffmpeg -i {} -c copy -map 0 -segment_time 4 -f segment -reset_timestamps 1 {}_%d.mp4".format(i,i[:-4]))
    #output = str(j) + ".mp4"
    os.system(bashCommand1)
    j = j+1

print("done")
