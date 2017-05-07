'''
Ritorna una stringa lunga n in cui l'intero x e' giustificato a destra
e le posizioni a sinistra sono riempite con il carattere punto '.'
Suggerimento: potete usare solo stringhe, con
le operazioni di concatenamento (+), ripetizione (*) e la funzione len().
Il ciclo for non e' necessario.
pad_r(5, 7)   -->  '......5'
pad_r(123, 7) -->  '....123'
pad_r(123, 9) -->  '......123'
'''
def pad_r(x, n):
    s2=str(x)
    s1=('.'*(n-len(s2)))
    return s1+s2
