from PIL import Image, ExifTags
import os
import os.path
import glob
import numpy as np

path = "<path>/gray scale"

all_img = os.listdir("<path>/labels__") 
all_img.remove(".DS_Store")
all_img.sort()
print(all_img)
print(len(all_img))

print (all_img)
k = 1
j = 10
for img in all_img:
    strig = str(img)
    img = Image.open("<path>/labels__/"+str(img)).convert('L')
    img.save("<path>/gray scale/{}.jpg".format(k))
    os.rename("<path>/gray scale/{}.jpg".format(k), strig)
    k = k+1
