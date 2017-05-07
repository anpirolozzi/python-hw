#! /usr/bin/env python -B

from testlib import check, run, runtests, check_file

def test_text_01():
    '''Check a simple input'''
    import program03
    program03.text('wpHTML_in.html', 'wpHTML_out.txt')
    check_file('wpHTML_out.txt','wpHTML_check.txt')
    return 2

def test_text_02():
    '''Check a simple input'''
    import program03
    program03.text('wpTimBernersLee_in.html', 'wpTimBernersLee_out.txt')
    check_file('wpTimBernersLee_out.txt', 'wpTimBernersLee_check.txt')
    return 3

tests = [test_text_01,test_text_02]

if __name__ == '__main__': runtests(tests)
