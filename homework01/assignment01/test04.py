#! /usr/bin/env python -B

from testlib import check, run, runtests

def test_list_for_01():
    '''Check a simple input'''
    import program04
    check(program04.list_for(['a', 'bb', 'c']),['  a  ', '  bb  ', '  c  '])
    return 4

def test_list_for_02():
    '''Check a simple input'''
    import program04
    check(program04.list_for([]),[])
    return 2

tests = [test_list_for_01,test_list_for_02]

if __name__ == '__main__': runtests(tests)
