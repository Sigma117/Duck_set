from PIL import Image, ExifTags
import os
import os.path
import glob
import numpy as np




path = "/Users/stefanozhao/Desktop/dataset/prove/gray scale"

all_img = os.listdir("/Users/stefanozhao/Desktop/dataset/prove/labels__") #lista che contiene tutte le lables__
all_img.remove(".DS_Store")
all_img.sort()
print(all_img)
print(len(all_img))

#all_glob = [i for i in glob.glob("*.jpg")]

print (all_img)
k = 1
j = 10
for img in all_img:
    strig = str(img) #se mettiamo str(img) direttamente non so perché crea dei file strani mentre assegando la sua str(img) a unal'tra variabile funziona
    img = Image.open("/Users/stefanozhao/Desktop/dataset/prove/labels__/"+str(img)).convert('L')
    img.save("/Users/stefanozhao/Desktop/dataset/prove/gray scale/{}.jpg".format(k))
    os.rename("/Users/stefanozhao/Desktop/dataset/prove/gray scale/{}.jpg".format(k), strig)
    k = k+1


"""img = Image.open("/Users/stefanozhao/Desktop/dataset/prove/labels__/3_3_13.jpg").convert('L')
img.save("3_3_13.jpg")"""