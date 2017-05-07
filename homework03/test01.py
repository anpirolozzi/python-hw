#! /usr/bin/env python -B

from testlib import check, run, runtests

def test_tuples_to_dict_01():
    '''Check a simple input'''
    import program01
    check(program01.tuples_to_dict([ ('Rossi','Mario',1974), ('Blu','Felice',1974), ('Bianchi','Giacomo',1974) ]),
                                   ({1974: 3}, {1974: [('Bianchi', 'Giacomo'), ('Blu', 'Felice'), ('Rossi', 'Mario')]}) )
    return 2

def test_tuples_to_dict_02():
    '''Check a simple input'''
    import program01
    check(program01.tuples_to_dict([ ('Rossi','Mario',1974), ('Blu','Felice',1981), ('Bianchi','Giacomo',1974) ] ),({1981: 1, 1974: 2}, {1981: [('Blu', 'Felice')], 1974: [('Bianchi', 'Giacomo'), ('Rossi', 'Mario')]})
)
    return 4

tests = [test_tuples_to_dict_01,test_tuples_to_dict_01]

if __name__ == '__main__': runtests(tests)
