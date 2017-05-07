#! /usr/bin/env python -B

from testlib import check, run, runtests

def test_graph_01():
    '''Check a simple input'''
    import program02
    g = program02.load_graph('file02_01_in.txt')
    check(program02.distance(g, program02.Node(2)), [1, 2, 3, 3, 1])
    return 2

def test_graph_02():
    '''Check a simple input'''
    import program02
    g = program02.load_graph('file02_02_in.txt')
    check(program02.distance(g, program02.Node(8)), [1, 4, 3, 1, 1, 1, 2])
    return 3

tests = [test_graph_01,test_graph_02]

if __name__ == '__main__': runtests(tests)
