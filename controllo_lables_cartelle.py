import os
import numpy as np
import glob
"""per controllare se le lables corrispondno alle cartelle"""

path = "/Users/stefanozhao/Desktop/dataset/train_duck" #pwd sul terminale
directory_contents = os.listdir(path)
all_elements = list

for item in directory_contents:
    if not os.path.isdir(item):
        directory_contents.remove(item)

"""lista che contiene tutte le cartelle con le immagini per il training"""
all_elements = directory_contents

#all_elements.remove((".DS_Store"))
all_elements.sort()
print(all_elements)

"""lista che contiene tutte le lables delle immagini"""
labels__ = os.listdir("/Users/stefanozhao/Desktop/dataset/labels__") #lista che contiene tutte le lables__
labels__.sort() #ordino
labels__.remove(".DS_Store")
print(labels__)

ciao = []
for i in range(len(labels__)):
    for j in range(len(all_elements)):
        if labels__[i][:-7] == all_elements[j]:
            print(all_elements[j])
            ciao.append(all_elements[j])

ciao = list(dict.fromkeys(ciao))
ciao.sort()
print(ciao)

print(all_elements)

for i in range(len(ciao)):
    if all_elements[i] != ciao[i]:
        print("fuck")