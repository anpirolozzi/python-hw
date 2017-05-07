#! /usr/bin/env python -B

from testlib import check, run, runtests

def test_pad_r_01():
    '''Check a simple input'''
    import program03
    check(program03.pad_r(5,7),'......5')
    return 2

def test_pad_r_02():
    '''Check a simple input'''
    import program03
    check(program03.pad_r(127,7),'....127')
    return 2

def test_pad_r_03():
    '''Check a simple input'''
    import program03
    check(program03.pad_r(123,9),'......123')
    return 2

tests = [test_pad_r_01,test_pad_r_02,test_pad_r_03]

if __name__ == '__main__': runtests(tests)
