# Duck_set-
How to create a dataset to train a neural network to detect the roadway lines using Python

In this repository, I will explain how to create a dataset by extracting images from videos using Python. 
The dataset obtained with this procedure was used to train the CNN presented in [github Link](https://github.com/Sigma117/Robust-Lane-Detection))
The whole image extraction process was developed in Python via the following steps: 

1) **Resize video to 256x128 format.** This first step was necessary to extract images with a size of 256x128 pixels, as required by the neural network I  used. For this purpose, the video_size function was created. Then, through a for loop, all the videos are resized using the function just described and are duplicated in 256x128 format, not overwritten by the original videos (see Appendix A);

1)	Ridimensionamento del video in formato 256x128. Questo primo step è necessario per estrarre immagini che abbiano dimensione 256x128 pixel, come richiesto dalla rete neurale usata. Per questo scopo, è stata creata la funzione video_size. Dopodiché, tramite un ciclo for, tutti i video vengono ridimensionati usando la funzione appena descritta e vengono duplicati in formato 256x128, non sovrascritti ai video di partenza (vedi Appendice A);

2)	I video ridimensionati vengono tagliati in video da quattro secondi di durata. Questo passaggio viene fatto per avere la durata di tutti i video identica, in modo da semplificare i passaggi successivi. Anche in questo caso, i nuovi video di quattro secondi non sono stati sovrascritti ai precedenti, ma sono stati duplicati (vedi Appendice B); 

3)	Da ogni video di quattro secondi vengono ricavati venti frames che vengono salvati in una cartella appositamente creata, che ha lo stesso nome del video da cui i frames derivano. Questo è il primo vero passaggio per la realizzazione del training set, con cui vengono estratte le immagini dai video (vedi Appendice C);

4)	Il tredicesimo e il ventesimo frame di ogni video sono stati copiati in una cartella apposita per poi essere elaborati con un programma di photo editing al fine di creare le labels (vedi appendice D); 

5)	Le labels sono state convertite in scala di grigi. Questo step è necessario poiché le labels, che sono state estratte direttamente dai video di partenza, sono a colori, mentre la rete neurale richiede labels che siano in scala di grigi (vedi Appendice E); 

6)	Infine, sono stati creati i file txt train_index e val_index per l’addestramento (vedi Appendice F). 
![image](https://user-images.githubusercontent.com/71655239/167939550-bd4e65de-9d84-4acf-b9cd-3e531042478a.png)
