'''
Definire una classe Loom secondo le indicazioni qui sotto. Gli oggetti
di tipo Loom mantengono una "tela" di lato size che e' una matrice di interi
con size righe e size colonne. La tela puo' essere "tessuta" da dei tessitori
che sono oggetti di tipo Weaver. Gli oggetti di tipo Weaver hanno un metodo
point(r, c, v) che ritorna un valore intero in funzione della posizione r, c e
del valore v di un punto di una tela. Il metodo weave() di Loom "tesse" la tela
in modo tale che ad ogni punto di essa sono applicati i weaver al valore
precedente nell'ordine in cui sono stati aggiunti all'oggetto Loom. Cioe', se
i weaver sono w1, w2,...,wk, sul punto r, c con valore v e' applicato il metodo
point di w1 producendo il valore v1 ad esso e' applicato il metodo point di
w2 producendo il valore v2 e cosi' via fino a wk che produce vk e quest'ultimo
e' impostato come valore della tela nel punto r, c.
Ecco due esempi con i seguenti weaver:

class Weaver1(object):
    def point(self, r, c, v):
        return (r + c + v) % 275

class Weaver2(object):
       def point(self, r, c, v):
           return (r*c + v) % 323

class Weaver3(object):
       def point(self, r, c, v):
           return (r + c + (v//7)**2) % 437


Questo programma deve produrre un file (immagine) uguale a
file03_01_check.png:

s1 = Weaver1()
s2 = Weaver2()
l = Loom(300)
l.add_weaver(s1)
l.add_weaver(s2)
l.weave()
saveasimg('file03_01_out.png', l)


Quest'altro programma deve produrre un file (immagine) uguale a
file03_02_check.png:

s3 = Weaver3()
l = Loom(300)
l.add_weaver(s1)
l.add_weaver(s2)
l.add_weaver(s2)
l.add_weaver(s3)
l.weave()
saveasimg('file03_02_out.png', l)

La funzione saveasimg e' definita qui sotto
'''

import png
 
class Loom(object):
    '''Deve avere un attributo size che contiene il lato della tela.'''
    def __init__(self, size): 					          #costruttore tela Loom
        '''Crea un telaio per lavorare su una tela quadrata di lato
           size, inizializzata con il valore 0.'''
        self.size = size 			 	      #associa la dimensione size x size
        self.matrx = [] 					       #associa la griglia matrx
        for x in range(size): 				        #scansione la dimensione griglia
            matrxrow = [] 				  	  #inizializza la struttura riga
            for y in range(size): 			   #scansiona nuovamente dimensione size
                matrxrow.append(0)  			    #imposta a 0 gli elementi della riga
            self.matrx.append(matrxrow)     			    #aggiunge effetivamente riga
        self.lweaver = [] 				   	   #inizializza lista dei weaver
 
    def get_point(self, r, c):
        '''Ritorna il valore della tela nella riga r e colonna c.'''
        return self.matrx[r][c] 				      #accede quindi a matrx r,c
 
    def add_weaver(self, s):
        '''Aggiunge il weaver s. Si puo' aggiungere piu' volte
           lo stesso weaver.'''
        self.lweaver.append(s) 		 		      #aggiunge alla lweaver il weaver s
 
    def weave(self):
        '''Tesse la tela, cioe' applica su ogni punto della tela
           tutti i weavers nell'ordine in cui sono stati aggiunti.'''
        for x in range(self.size):                   			    #scansiona ogni riga
            for y in range(self.size):          			 #scansiona ogni colonna
                for p in self.lweaver: 			 		 #scansiona lista weaver
                    val = self.get_point(x,y) 				#prende il valore in x,y
                    self.matrx[x][y] = p.point(x,y,val)    #assegna a quel valore l'applicazione 
										   #del weaver p
 
def saveasimg(filename, loom): 					    #già definita salva immagine
    png_img = [] 					   		       #griglia immagine
    for r in range(loom.size):
        png_row = []            		#inizializza le righe arrivando a ncolonne==size
        for c in range(loom.size): 				   	   #scansiona le colonne
            v = loom.get_point(r, c) 				  	      #cattura il colore
            png_row.extend([v % 256, v % 256, v %256]) 		   #estende la riga con colore v
        png_img.append(png_row)  			 	     #aggiunge a png_img la riga
    with open(filename, 'wb') as f:  			      #apre il file in scrittura binaria
        png.Writer(loom.size, loom.size).write(f, png_img)       			 #scrive
