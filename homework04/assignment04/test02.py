#! /usr/bin/env python -B

from testlib import check, run, runtests

def test_count_attr_01():
    '''Check a simple input'''
    import program02
    check(program02.count_attr('wpHTML_in.html', [('class', None), ('class', 'image'), ('href', None), ('title', 'HTML')]),
          {('href', None): 1303, ('title', 'HTML'): 72, ('class', 'image'): 3, ('class', None): 1163})
    return 2

def test_count_attr_02():
    '''Check a simple input'''
    import program02
    check(program02.count_attr('wpTimBernersLee_in.html', [('class', None), ('class', 'image'), ('href', None), ('title', 'HTML')]),
          {('href', None): 1095, ('title', 'HTML'): 0, ('class', 'image'): 6, ('class', None): 1016})
    return 3

tests = [test_count_attr_01,test_count_attr_02]

if __name__ == '__main__': runtests(tests)
