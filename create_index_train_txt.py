import os
import numpy as np
import glob

# per fare i file index.txt
path = "/Users/stefanozhao/Desktop/dataset/prove" #pwd sul terminale
directory_contents = os.listdir(path)
all_subDirectory = list

for item in directory_contents:
    if not os.path.isdir(item):
        directory_contents.remove(item)
#directory_contents.remove("create_index_train_txt.py") #momentaneo
directory_contents.remove("labels__")

"""lista che contiene tutte le cartelle con le immagini per il training"""
all_subDirectory = directory_contents
all_subDirectory.sort()

"""lista che contiene tutte le lables delle immagini"""
labels__ = os.listdir(path + "/labels__") #lista che contiene tutte le lables__
labels__.sort() #ordino

"""creazione del file + scrittura del file"""
index = open("indexLabels.txt", "w+")

"""scrittura del file"""
for i in all_subDirectory:

    """TUTTI GLI elementi delle singole subDirectory"""
    subDirectory = os.listdir( path + "/{}".format(i))
    subDirectory.sort()
    print(subDirectory)
    print(subDirectory[5])


    index.write("./data/traningset_duck/train_duck/{}/{} ".format(i,subDirectory[8]))
    index.write("./data/traningset_duck/train_duck/{}/{} ".format(i,subDirectory[9]))
    index.write("./data/traningset_duck/train_duck/{}/{} ".format(i,subDirectory[10]))
    index.write("./data/traningset_duck/train_duck/{}/{} ".format(i,subDirectory[11]))
    index.write("./data/traningset_duck/train_duck/{}/{} ".format(i,subDirectory[12]))
    index.write("./data/traningset_duck/labels__/{}\n".format(subDirectory[12]))

    index.write("./data/traningset_duck/train_duck/{}/{} ".format(i,subDirectory[4]))
    index.write("./data/traningset_duck/train_duck/{}/{} ".format(i,subDirectory[6]))
    index.write("./data/traningset_duck/train_duck/{}/{} ".format(i,subDirectory[8]))
    index.write("./data/traningset_duck/train_duck/{}/{} ".format(i,subDirectory[10]))
    index.write("./data/traningset_duck/train_duck/{}/{} ".format(i,subDirectory[12]))
    index.write("./data/traningset_duck/labels__/{}\n".format(subDirectory[12]))

    index.write("./data/traningset_duck/train_duck/{}/{} ".format(i,subDirectory[0]))
    index.write("./data/traningset_duck/train_duck/{}/{} ".format(i,subDirectory[3]))
    index.write("./data/traningset_duck/train_duck/{}/{} ".format(i,subDirectory[6]))
    index.write("./data/traningset_duck/train_duck/{}/{} ".format(i,subDirectory[9]))
    index.write("./data/traningset_duck/train_duck/{}/{} ".format(i,subDirectory[12]))
    index.write("./data/traningset_duck/labels__/{}\n".format(subDirectory[12]))

    """inizia le labels con la 20"""

    index.write("./data/traningset_duck/train_duck/{}/{} ".format(i,subDirectory[15]))
    index.write("./data/traningset_duck/train_duck/{}/{} ".format(i,subDirectory[16]))
    index.write("./data/traningset_duck/train_duck/{}/{} ".format(i,subDirectory[17]))
    index.write("./data/traningset_duck/train_duck/{}/{} ".format(i,subDirectory[18]))
    index.write("./data/traningset_duck/train_duck/{}/{} ".format(i,subDirectory[19]))
    index.write("./data/traningset_duck/labels__/{}\n".format(subDirectory[19]))

    index.write("./data/traningset_duck/train_duck/{}/{} ".format(i,subDirectory[11]))
    index.write("./data/traningset_duck/train_duck/{}/{} ".format(i,subDirectory[13]))
    index.write("./data/traningset_duck/train_duck/{}/{} ".format(i,subDirectory[15]))
    index.write("./data/traningset_duck/train_duck/{}/{} ".format(i,subDirectory[17]))
    index.write("./data/traningset_duck/train_duck/{}/{} ".format(i,subDirectory[19]))
    index.write("./data/traningset_duck/labels__/{}\n".format(subDirectory[19]))

    index.write("./data/traningset_duck/train_duck/{}/{} ".format(i,subDirectory[7]))
    index.write("./data/traningset_duck/train_duck/{}/{} ".format(i,subDirectory[10]))
    index.write("./data/traningset_duck/train_duck/{}/{} ".format(i,subDirectory[13]))
    index.write("./data/traningset_duck/train_duck/{}/{} ".format(i,subDirectory[16]))
    index.write("./data/traningset_duck/train_duck/{}/{} ".format(i,subDirectory[19]))
    index.write("./data/traningset_duck/labels__/{}\n".format(subDirectory[19]))


index.close()