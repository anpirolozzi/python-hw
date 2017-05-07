'''
Ritorna una lista con i prodotti di n per 2, 3, 5 e 7.
prod_list(7)   --> [14, 21, 35, 49]
prod_list(1)   --> [2, 3, 5, 7]
prod_list(10)  --> [20, 30, 50, 70]
'''
def prod_list(n):
    l = [2,3,5,7]
    for i in range(len(l)):
        l[i]= n * l[i]
    return l
