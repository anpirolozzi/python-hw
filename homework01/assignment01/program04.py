'''
Ritorna una nuova lista i cui valori sono le stringhe della
lista di input lst precedute e seguite da due spazi.
list_for(['a', 'bb', 'c'])  --> ['  a  ', '  bb  ', '  c  ']
'''
def list_for(lst):
    space=(" " * 2)
    for i in range(0,len(lst)):
        lst[i]= space + lst[i] + space
    return lst
