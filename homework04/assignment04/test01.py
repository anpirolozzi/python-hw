#! /usr/bin/env python -B

from testlib import check, run, runtests

def test_tree_01():
    '''Check a simple input'''
    import program01
    d1 = {'name':'musica', 'children':[{'name':'rock', 'children':[{'name':'origini','children':[]},
                                                                   {'name':'rock&roll','children':[]},
                                                                   {'name':'hard rock', 'children':[]}]},
                                       {'name':'jazz', 'children':[{'name':'origini', 'children':[{'name':'1900', 'children':[]}]},
                                                                   {'name':'ragtime', 'children':[]}, {'name':'swing', 'children':[]}]}]}
    tree = program01.create_tree(d1)
    check(tree.count(), 10)
    check(tree.height(), 4)
    check(tree.get_children()[0].count(), 4)
    check(tree.get_children()[1].height(), 3)
    check(tree.count_by_name('origini'), 2)
    return 2

def test_tree_02():
    '''Check a simple input'''
    import program01
    d2 = {'name':'html', 'children':[{'name':'head', 'children':[{'name':'meta', 'children':[]}, 
                                                                 {'name':'title', 'children':[]}, 
                                                                 {'name':'style', 'children':[]}]}, 
                                     {'name':'body', 'children':[{'name':'h1', 'children':[]}, 
                                                                 {'name':'section', 'children':[{'name':'p', 'children':[{'name':'strong', 'children':[]},
                                                                                                                         {'name':'b', 'children':[]},
                                                                                                                         {'name':'em', 'children':[]},
                                                                                                                         {'name':'i', 'children':[]}]},
                                                                                                {'name':'p', 'children':[{'name':'q', 'children':[]},
                                                                                                                         {'name':'code', 'children':[]},
                                                                                                                         {'name':'kbd', 'children':[]}]},
                                                                                                {'name':'p', 'children':[{'name':'sup', 'children':[]},
                                                                                                                         {'name':'sub', 'children':[]}]},
                                                                                                {'name':'p', 'children':[{'name':'span', 'children':[]}]}]}, 
                                                                 {'name':'footer', 'children':[{'name':'a', 'children':[{'name':'strong', 'children':[]}]},
                                                                                               {'name':'a', 'children':[{'name':'strong', 'children':[]}]}]}]}]}
    tree = program01.create_tree(d2)
    check(tree.count(), 27)
    check(tree.height(), 5)
    check(tree.get_children()[1].count(), 22)
    check(tree.get_children()[1].height(), 4)
    check(tree.count_by_name('p'), 4)
    return 3

tests = [test_tree_01,test_tree_02]

if __name__ == '__main__': runtests(tests)
