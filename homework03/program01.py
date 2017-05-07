'''
Data una lista di tuple contenenti (cognome,nome,anno), 
ritornare una tupla di due dizionari. Il primo ha come
chiavi gli anni e come valori il numero di elementi della
lista per quell'anno. Il secondo, ha come chiavi gli anni
e come valori una lista ordinata di tuple (cognome,nome)
degli elementi corrispondenti a quell'anno. Ad esempio:
tuples_to_dict([ ('Rossi','Mario',1974), ('Blu','Felice',1974), ('Bianchi','Giacomo',1974) ] ) ->
    ( {1974: 3}, {1974: [('Bianchi', 'Giacomo'), ('Blu', 'Felice'), ('Rossi', 'Mario')]} )
tuples_to_dict([ ('Rossi','Mario',1974), ('Blu','Felice',1981), ('Bianchi','Giacomo',1974) ] ) ->
    ( {1981: 1, 1974: 2}, {1981: [('Blu', 'Felice')], 1974: [('Bianchi', 'Giacomo'), ('Rossi', 'Mario')]} )
'''

def tuples_to_dict(lst):
    num = dict()
    elem = dict()
    for t in lst:
        iyear = t[2]
        if not iyear in num:
            num[iyear]=1
        else:
            num[iyear]+=1

    for t in lst:
        iyear = t[2]
        cognome,nome,anno=t
        tupla = (cognome,nome)
        if not anno in elem:
            elem[anno]=[]
        elem[anno].append(tupla)
        elem[anno].sort()
    return (num,elem)
