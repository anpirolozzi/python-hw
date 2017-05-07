'''
Ritorna la somma dei valori positivi della lista di input
lst.
list_for_if([3, 0, 2, -6])     --> 5
list_for_if([-1, 0, 2, -4, 7]) --> 9
'''
def list_for_if(lst):
    s=0
    for i in range(0,len(lst)): 
        if (lst[i] > 0):
            s+=(lst[i])
    return s
