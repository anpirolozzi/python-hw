#! /usr/bin/env python -B

from testlib import check, run, runtests

def test_cypher_01():
    '''Check a simple input'''
    import program02
    check(program02.caesar_cypher('ciao, ma che bello',3),'fldr, pd fkh ehoor')
    return 2

def test_cypher_02():
    '''Check a simple input'''
    import program02
    check(program02.caesar_cypher('fldr, pd fkh ehoor',-3),'ciao, ma che bello')
    return 2

def test_cypher_03():
    '''Check a simple input'''
    import program02
    check(program02.caesar_cypher('pippo e pluto --- kdkkj y kgpoj',5),'unuut j uqzyt --- pippo d pluto')
    return 2

tests = [test_cypher_01,test_cypher_02,test_cypher_03]

if __name__ == '__main__': runtests(tests)
