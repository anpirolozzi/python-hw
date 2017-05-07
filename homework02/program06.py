'''
Creare un mosaico routando a righe alternate rettangoli di pixel nell'immagine input.
I rettangoli sono di dimensione (w,h). Potete assumere che non chiederemo mai di
routare con valori strani che uscirebbero dall'immagine (cioa' assumete che
se il programma e' coretto non dovete preoccuparvi di validare gli indirizzi dei pixels).
Per creare un mosaico a scacchiera, ruotiamo di 90 i rettangoli per i quali
(i+j)%2 != 0, dove (i,j) e' l'indice del rettangolo contando dall'alto.
In programma legge dal file filename_in e salva sul file filename_out.
Potete usare le funzioni di lettura e scrittura nel modulo image.py
presente nell'esercizio. Potete esare tutte le funzioni in image.py.
Esempi:
rotate_mosaic('img06_01_in.png','img06_01_out.png',128,32)
    -> 'img06_01_check.png'
rotate_mosaic('img06_02_in.png','img06_02_out.png',32,32)
    -> 'img06_02_check.png'
'''

import image

def rotate_mosaic(filename_in,filename_out,w,h):
    mettere_il_codice_qui = 0
