#! /usr/bin/env python -B

from testlib import check, run, runtests, check_img, check_file

def test_items_01():
    '''Check a simple input'''
    import program04
    program04.items('file04_01_in.txt', 'file04_01_out.txt')
    check_file('file04_01_out.txt','file04_01_check.txt')
    return 3

def test_items_02():
    '''Check a simple input'''
    import program04
    program04.items('file04_02_in.txt', 'file04_02_out.txt')
    check_file('file04_02_out.txt','file04_02_check.txt')
    return 3

tests = [test_items_01,test_items_02]

if __name__ == '__main__': runtests(tests)
