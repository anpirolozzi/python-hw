'''
La stringa s di input si assume contenga una frase fatta da
caratteri alfabetici, spazio e punteggiatura (solamente i caratteri
'.,;:?!'), la funzione ritorna la lista delle parole i cui caratteri
sono stati resi tutti minuscoli.
print list_str_methods('Ciao Pippo, come stai?')
 -->  ['ciao', 'pippo', 'come', 'stai']
print list_str_methods('Questa funzione usa metodi su stringhe.')
 --> ['questa', 'funzione', 'usa', 'metodi', 'su', 'stringhe']
'''
def list_str_methods(s):
    s=s.lower()
    l=s.split()
    for i in range(0,len(l)):
        punctuation=[".",",",";",":","?","!"]
        for p in range(0,len(punctuation)):
            l[i]=l[i].replace(punctuation[p],"")       
    return l
