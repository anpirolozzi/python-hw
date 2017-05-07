#! /usr/bin/env python -B

from testlib import check, run, runtests

def test_indices_01():
    '''Check a simple input'''
    import program01
    check(program01.indices(['pera', 'mela', 'uva', 'mela', 'pesca',
                             'pera', 'banana', 'pesca', 'mela']),
          {'uva': [2], 'pera': [0, 5], 'mela': [1, 3, 8], 'banana': [6],
           'pesca': [4, 7]})
    return 3

def test_indices_02():
    '''Check a simple input'''
    import program01
    check(program01.indices([1, 2, '', 13, 1, '', 3, 13, 'a', 13]),
          {'': [2, 5], 1: [0, 4], 2: [1], 3: [6], 13: [3, 7, 9], 'a': [8]})
    return 3

tests = [test_indices_01,test_indices_02]

if __name__ == '__main__': runtests(tests)
