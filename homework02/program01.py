'''
Ritorna un dizionario che ad ogni valore distinto k della lista lst associa
la lista ordinata degli indici in cui si trova k. Esempi

indices(['pera', 'mela', 'uva', 'mela', 'pesca','pera', 'banana', 'pesca',
         'mela'])  -->
    {'uva': [2], 'pera': [0, 5], 'mela': [1, 3, 8], 'banana': [6], 'pesca': [4, 7]}
     
indices([1, 2, '', 13, 1, '', 3, 13, 'a', 13])  -->
    {'': [2, 5], 1: [0, 4], 2: [1], 3: [6], 13: [3, 7, 9], 'a': [8]}
    
'''

def indices(lst):
    d=dict()
    for k in range(0,len(lst)):
        if(lst[k] in d):
	    d[lst[k]]+=[k]
        else:
            d[lst[k]]=[k]
    return d
