'''
Usando le classi Node e Graph visti a lezione e riportate qui sotto,
definire le seguenti due funzioni:

load_graph(filename)
crea e ritorna un grafo di tipo Graph definito nel file di nome filename.
Ogni nodo e' identificato da un intero. Ogni linea del file contiene una
sequenza di interi n0 n1 n2 ... separati da spazi, con il significato che i
nodi identificati da n1, n2, ... sono adiacenti al nodo n0. Se il file ha
n linee i nodi del grafo sono n e sono identificati dagli interi da 1 a n.

distance(graph, node)
ritorna una lista dist tale che dist[k] e' il numero di nodi a distanza k
dal nodo node.

Ecco due esempi:

g = load_graph('file02_01_in.txt')
distance(g, Node(2))  --> [1, 2, 3, 3, 1]

g = load_graph('file02_02_in.txt')
distance(g, Node(8))  --> [1, 4, 3, 1, 1, 1, 2]

Suggerimento: la funzione distance e' una semplice variazione della
funzione che visita un grafo vista a lezione.
'''

class Node(object):
    def __init__(self, name, attr=None):
        self.name = name
        self.attr = attr
        self._adjacent = []
    def add_adjacent(self, a):
        if a not in self._adjacent:
            self._adjacent.append(a)
    def adjacent(self):
        return self._adjacent[:]
    def __eq__(self, x):
        return x.name == self.name
    def __ne__(self, x):
        return not (x == self)
    def __hash__(self):
        return self.name.__hash__()
    
class Graph(object):
    def __init__(self):
        self._nodes = []
        self._indices = {}
    def get_node(self, u):
        return self._nodes[self._indices[u]]
    def add_node(self, u):
        if u not in self._indices:
            self._nodes.append(u)
            self._indices[u] = len(self._nodes) - 1
        return self.get_node(u)
    def add_edge(self, u, v):
        node_u = self.get_node(u)
        node_v = self.get_node(v)
        node_v.add_adjacent(self.get_node(u))
        node_u.add_adjacent(self.get_node(v))
    def nodes(self):
        return self._nodes[:]


def load_graph(filename):
    '''Definire la funzione qui.'''
    g = Graph()
    with open(filename,'U') as f:
        testo = f.readlines()
    for linea in testo:
        list = []
        lst = linea.split()
        for j in lst:
            var = Node(int(j))
            list.append(var)
            for i in list:
                g.add_node(i)
            for i in range(1,len(list)):
                g.add_edge(list[i],list[0])
    return g
       
def distance(graph, node):
    node = graph.get_node(node)
    visited = set([node])
    active = set([node])
    d = [1]
    while len(active) > 0:
        newactive = set()
        cont = 0
        while len(active) > 0:
            u = active.pop()
            for v in u.adjacent():
                if v not in visited:
                    cont += 1
                    visited.add(v)
                    newactive.add(v)
        active = newactive
        d.append(cont)
    return d
