import os
import numpy as np
import glob

# per fare i file index.txt
path = "/Users/stefanozhao/Desktop/dataset/Duck" #pwd sul terminale
directory_contents = os.listdir(path)
all_subDirectory = list

for item in directory_contents:
    if not os.path.isdir(item):
        directory_contents.remove(item)
    if item == "labels":
        directory_contents.remove(
            "labels")  # per rimuove la cartella labels da quelle in qui dobbiamo estrarrre le immagini


all_subDirectory = directory_contents
all_subDirectory.sort()
print(all_subDirectory)

index = open("indexLabels.txt", "w+")


for i in all_subDirectory:
    for j in range(5):
        index.write("./data/testset/labels/{}_13.jpg ".format(i))
    index.write("./data/testset/truth/1_13.jpg\n")

    for k in range(5):
        index.write("./data/testset/labels/{}_20.jpg ".format(i))
    index.write("./data/testset/truth/1_13.jpg\n")


index.close()