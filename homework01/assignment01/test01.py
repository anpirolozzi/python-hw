#! /usr/bin/env python -B

from testlib import check, run, runtests

def test_sum_prod_01():
    '''Check a simple input'''
    import program01
    check(program01.sum_prod(7),119)
    return 2

def test_sum_prod_02():
    '''Check a simple input'''
    import program01
    check(program01.sum_prod(1),17)
    return 2

def test_sum_prod_03():
    '''Check a simple input'''
    import program01
    check(program01.sum_prod(10),170)
    return 2

tests = [test_sum_prod_01,test_sum_prod_02,test_sum_prod_03]

if __name__ == '__main__': runtests(tests)
