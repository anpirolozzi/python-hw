#! /usr/bin/env python -B

from testlib import check, run, runtests, check_file

def test_img_01():
    '''Check a simple input'''
    import program01
    program01.imagegrab('http://pellacini.di.uniroma1.it/teaching/fondamenti12/_homework06_support/assignment06_page01.html')
    check_file('img01_01a_out.png', 'img01_01a_check.png')
    return 2

def test_img_02():
    '''Check a simple input'''
    import program01
    program01.imagegrab('http://pellacini.di.uniroma1.it/teaching/fondamenti12/_homework06_support/assignment06_page02.html')
    check_file('img01_02a_out.png', 'img01_02a_check.png')
    check_file('img01_02b_out.png', 'img01_02b_check.png')
    return 4

tests = [test_img_01,test_img_02]

if __name__ == '__main__': runtests(tests)
