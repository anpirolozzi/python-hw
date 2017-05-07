#! /usr/bin/env python -B

from testlib import check, run, runtests

def test_list_str_methods_01():
    '''Check a simple input'''
    import program06
    check(program06.list_str_methods('Ciao Pippo, come stai?'),['ciao', 'pippo', 'come', 'stai'])
    return 4

def test_list_str_methods_02():
    '''Check a simple input'''
    import program06
    check(program06.list_str_methods('Questa funzione usa metodi su stringhe.'),['questa', 'funzione', 'usa', 'metodi', 'su', 'stringhe'])
    return 4


tests = [test_list_str_methods_01,test_list_str_methods_02]

if __name__ == '__main__': runtests(tests)
