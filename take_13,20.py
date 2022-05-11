import os
import numpy as np
import glob

# per creare una liste di tutte le cartelle
path = "/Users/stefanozhao/Desktop/dataset/Duck" #pwd sul terminale
directory_contents = os.listdir(path)
all_subDirectory = list

for item in directory_contents:
    if not os.path.isdir(item):
        directory_contents.remove(item)
    if item == "labels":
        directory_contents.remove(
            "labels")  # per rimuore la cartella labels da quelle in qui dobbiamo estrarrre le immagini


all_subDirectory = directory_contents
all_subDirectory.sort()
print(all_subDirectory)
"""copia e estrazione """
for i in all_subDirectory:
    bashCommand_mv1 = ("cp /Users/stefanozhao/Desktop/dataset/Duck/{}/{}_13.jpg /Users/stefanozhao/Desktop/dataset/Duck/{}/{}_20.jpg /Users/stefanozhao/Desktop/dataset/Duck/labels".format(i, i, i, i))
    os.system(bashCommand_mv1)
b