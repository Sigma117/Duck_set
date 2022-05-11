import os
import numpy as np
import glob

path = "<path>/Duck"
directory_contents = os.listdir(path)
all_subDirectory = list

for item in directory_contents:
    if not os.path.isdir(item):
        directory_contents.remove(item)
    if item == "labels":
        directory_contents.remove(
            "labels")  


all_subDirectory = directory_contents
all_subDirectory.sort()
print(all_subDirectory)

"""copy and extraction """

for i in all_subDirectory:
    bashCommand_mv1 = ("cp <path>/Duck/{}/{}_13.jpg <path>/Duck/{}/{}_20.jpg <path>/Duck/labels".format(i, i, i, i))
    os.system(bashCommand_mv1)
b
