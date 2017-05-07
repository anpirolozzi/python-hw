'''Scrivere una funzione actor_graph(filename) che preso in input il nome
di un file in formato json che contiene una lista di film (per il formato
preciso vedere il file d'esempio 'file03_01_in.json'), crea un grafo di tipo
Graph i cui nodi sono gli attori dei film nel file e due attori sono connessi
se hanno recitato nello stesso film. Il dizionario di ogni film ha una chiave
'actors' il cui valore e' la lista dei nomi degli attori che hanno recitato
nel film. Ogni nodo, di tipo Node, deve anche contenere nell'attributo attr
un dizionario con una chiave 'titles' il cui valore e' un set dei titoli dei
film in cui l'attore ha recitato. Il titolo e' il valore della chiave 'title'
nel dizionario del film.
Ecco due esempi (la funzione degree(g, k) e' definita sotto e ritorna un set
con i nomi degli attori che hanno recitato insieme ad almeno k attori).
len(g.nodes())  --> 1343
degree(g, 50)  --> set([u'Joseph Gordon-Levitt', u'Robert Downey Jr.'])
degree(g, 40)  --> set([u'Brian Cox', u'Corey Feldman', u'Diedrich Bader',
                        u'Jack Black', u'Joe Pesci', u'John Hurt',
                        u'John Ratzenberger', u'Joseph Gordon-Levitt',
                        u'Michael Biehn', u'Michael Kelly', u'Robert De Niro',
                        u'Robert Downey Jr.', u'Sean Connery',
                        u'Stellan Skarsg\xe5rd'])
g.get_node(Node('Robert De Niro')).attr['titles']  -->
                    set([u'Casino', u'Once Upon a Time in America', u'Ronin'])
g.get_node(Node('Meryl Streep')).attr['titles']  --> set([u'Manhattan'])
g.get_node(Node('Sharon Stone')).attr['titles']  -->
                    set([u'Casino', u'Total Recall'])
g.get_node(Node('Winona Ryder')).attr['titles']  --> set([u'A Scanner Darkly'])
g.get_node(Node('Robert Downey Jr.')).attr['titles']  -->
                    set([u'A Scanner Darkly', u'Good Night, and Good Luck.',
                         u'Iron Man', u'Kiss Kiss Bang Bang'])

len(g.nodes())  --> 2551
degree(g, 70)  --> set([u'Brad Pitt', u'Chris Cooper', u'Christopher Plummer',
                        u'Philip Seymour Hoffman', u'Tom Cruise'])
degree(g, 60)  --> set([u'Brad Pitt', u'Chris Cooper', u'Christopher Plummer',
                        u'Ed Harris', u'John Ratzenberger',
                        u'Philip Seymour Hoffman', u'Tom Cruise'])
g.get_node(Node('Robert De Niro')).attr['titles']  -->
                     set([u'Meet the Parents', u'Sleepers', u'Stardust',
                          u'The Deer Hunter'])
g.get_node(Node('Meryl Streep')).attr['titles']  -->
                    set([u'Adaptation.', u'The Deer Hunter'])
g.get_node(Node('Sharon Stone')).attr['titles']  --> set([u'Total Recall'])
g.get_node(Node('Winona Ryder')).attr['titles']  -->
                    set([u'A Scanner Darkly', u'Beetle Juice',
                         u'Girl, Interrupted', u'Star Trek'])
g.get_node(Node('Brad Pitt')).attr['titles']  -->
                    set([u'Meet Joe Black', u'Megamind', u'Moneyball', u'Se7en',
                         u'Sleepers', u'True Romance'])
g.get_node(Node('Meg Ryan')).attr['titles']  --> set([u'When Harry Met Sally...'])
g.get_node(Node('Cameron Diaz')).attr['titles']  -->
                    set([u'Being John Malkovich', u'Gangs of New York', u'Shrek',
                         u'Shrek 2'])
'''

class Node(object): 				                          #classe definisce nodo
    def __init__(self, name, attr=None): 					    #costruttore
        self.name = name 				    #associa name al nodo in costruzione 
        self.attr = attr 				    #associa attr al nodo in costruzione
        self._adjacent = [] 		 #associa la lista nodi adiacenti al nodo in costruzione
    def add_adjacent(self, a): 						#aggiunge nodi adiacenti
        if a not in self._adjacent: 			       #se a non è nella lista adiacenti
            self._adjacent.append(a)						     #aggiungilo
    def adjacent(self): 							#lista adiacenti
        return self._adjacent[:] 	     #ritorna la lista degli adiacenti usando lo slicing
    def __eq__(self, x):						   #funzione uguaglianza
        return x.name == self.name 				#ritorna se due nomi sono uguali
    def __ne__(self, x): 						#funzione disuguaglianza
        return not (x == self) 					#ritona se due nomi sono diversi
    def __hash__(self): 				      #permette l'hashing della funzione
        return self.name.__hash__() 					#ritorna l'hash del nome
    
class Graph(object): 							 #classe definisce grafo
    def __init__(self): 							    #costruttore
        self._nodes = []		      #associa al grafo in costruzione la lista dei nodi
        self._indices = {}		  #associa al grafo in costruzione la lista degli indici
    def get_node(self, u): 						 #funzione aggiunta nodi
        return self._nodes[self._indices[u]] 			   #ritorna nodo avente indice u
    def add_node(self, u): 						 #funzione aggiunta nodi
        if u not in self._indices: 				 #se il nodo u non è nell'indice
            self._nodes.append(u) 						     #aggiungilo
            self._indices[u] = len(self._nodes) - 1 	 #e assegnali l'ultimo indice lista nodi
        return self.get_node(u) 				       #ottieni il nodo aggiunto
    def add_edge(self, u, v): 					  #aggiunge archi tra i nodi u,v
        node_u = self.get_node(u) 					      #ottiene il nodo u
        node_v = self.get_node(v) 					      #ottiene il nodo v
        node_v.add_adjacent(self.get_node(u)) 	      #aggiunge il nodo u tra gli adiacenti di v
        node_u.add_adjacent(self.get_node(v))	      #aggiunge il nodo v tra gli adiacenti di u
    def nodes(self): 							  #funzione ritorna nodi
        return self._nodes[:]				       #ritorna tutti i nodi della lista

import json

def actor_graph(filename):
    '''Scrivere il codice qui.'''
    ingrjson=open(filename).read() 		 #carico ingrjson leggendo il file json di input
    ingr = json.loads(ingrjson)			   #carica i film presenti nel file json in ingr
    grafo=Graph() 						     #inizializza il grafo grafo
    for film in ingr: 						   #scorro tutti i film presenti
            lstattori=[] 					       #inizializza lista attori
            for attore in film['actors']: 		  #per ogni attore che recita in un film
                    films=set() 		 #inizializza l'insieme films in cui ha recitato
                    for x in ingr: 			  #trovo tutti i film in cui ha recitato
                            if attore in x['actors']: films.add(x['title'])       #se l'attore e 
									      #presente nel film
                    x=grafo.add_node(Node(attore,attr={'titles':films}))  #creo un nodo relativo 
    								       #all'attore con attributo 
								     #un dizionario che contiene 
									   #l'insieme con i film 
									     #in cui ha recitato
                    lstattori.append(x) 			   #aggiungo x alla lista attori
            for i in range(len(lstattori)):          #creo i collegamenti (archi) tra gli attori 
						           #che hanno recitato nello stesso film
                    for j in range(i+1,len(lstattori)):
                            grafo.add_edge(lstattori[i],lstattori[j])
    return grafo 							       #ritorno il grafo
    
def degree(g, k): 					 #ritorna un set con i nomi degli attori 
						  #che hanno recitato insieme ad almeno k attori
    dset = set() 							    #definisce l'insieme
    for u in g.nodes(): 						          # ad ogni nodo
        deg = len(u.adjacent()) 				 #assegna a deg la sua lunghezza
        if deg >= k: 						      #se il deg è maggiore di k
            dset.add(u.name) 		   #aggiungo all'insieme il nome del nodo ricorsivamente
    return dset 							      #ritorno l'insieme
