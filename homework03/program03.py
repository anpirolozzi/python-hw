'''
Calcolo delgi istogrammi delle immagini.

Data un'immagine di input in filename, caricare 
l'immagine e ritornare una tupla di tre istogrammi,
uno per ogni canale dell'immagine. Un istogramma
e' una lista di conteggi. Ogni elemento i della lista
e' il conteggio dei valori tra i*step e (i+1)*step-1.
Nel caso delle immagini, l'istogramma avra' 256/step elementi.

Gil istogrammi sono fondamentali e usati in tutti i software
di image processing. Potete visualizzare gli istogrammi calcolati
salvandoli in una file .csv (come da esempio a lezione) e
caridoli su Excel, Google Spreadsheet o LibreOffice.

Ad esempio:
image_histos('img03_01_in.png',16) -> 
([0, 0, 0, 0, 1, 1, 6, 8, 7, 11, 22, 25, 28, 74, 52, 21], 
 [0, 0, 0, 0, 1, 0, 4, 10, 12, 13, 16, 23, 21, 27, 78, 51], 
 [7, 0, 1, 3, 4, 4, 4, 9, 4, 15, 13, 12, 17, 16, 16, 131])
image_histos('img03_02_in.png',8) -> 
([6, 9, 10, 30, 96, 79, 125, 167, 191, 312, 578, 866, 1053, 1258, 1888, 1921, 1719, 1517, 1341, 1222, 1048, 1111, 1018, 1125, 1246, 2451, 10088, 8983, 10298, 6783, 3130, 3867], 
 [122, 102, 174, 235, 350, 478, 472, 393, 526, 442, 511, 634, 840, 1026, 1152, 1079, 1141, 1459, 1939, 1828, 1504, 1390, 1353, 891, 717, 725, 840, 1220, 12006, 14249, 10246, 5492], 
 [481, 667, 1179, 1363, 1227, 1185, 1174, 1139, 1153, 1072, 907, 836, 745, 675, 660, 635, 502, 538, 547, 540, 488, 574, 628, 715, 672, 620, 554, 664, 682, 779, 1225, 40710])

'''

import image

def image_histos(filename,step):
    mettere_il_codice_qui = 0
