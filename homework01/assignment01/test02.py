#! /usr/bin/env python -B

from testlib import check, run, runtests

def test_prod_list_01():
    '''Check a simple input'''
    import program02
    check(program02.prod_list(7),[14, 21, 35, 49])
    return 2

def test_prod_list_02():
    '''Check a simple input'''
    import program02
    check(program02.prod_list(1),[2, 3, 5, 7])
    return 2

def test_prod_list_03():
    '''Check a simple input'''
    import program02
    check(program02.prod_list(10),[20, 30, 50, 70])
    return 2

tests = [test_prod_list_01,test_prod_list_02,test_prod_list_03]

if __name__ == '__main__': runtests(tests)
