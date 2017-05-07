#! /usr/bin/env python -B

from testlib import check, run, runtests

def test_list_for_if_01():
    '''Check a simple input'''
    import program05
    check(program05.list_for_if([3, 0, 2, -6]),5)
    return 2

def test_list_for_if_02():
    '''Check a simple input'''
    import program05
    check(program05.list_for_if([-1, 0, 2, -4, 7]),9)
    return 2

def test_list_for_if_03():
    '''Check a simple input'''
    import program05
    check(program05.list_for_if([]),0)
    return 2

tests = [test_list_for_if_01,test_list_for_if_02,test_list_for_if_03]

if __name__ == '__main__': runtests(tests)
