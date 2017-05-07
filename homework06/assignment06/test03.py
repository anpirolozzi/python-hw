#! /usr/bin/env python -B

from testlib import check, run, runtests, check_file

def test_g_01():
    '''Check a simple input'''
    import program03
    from program03 import Node
    g = program03.actor_graph('file03_01_in.json')
    check(len(g.nodes()), 1343)
    check(program03.degree(g, 50), set([u'Joseph Gordon-Levitt', u'Robert Downey Jr.']))
    check(program03.degree(g, 40), set([u'Brian Cox', u'Corey Feldman', u'Diedrich Bader',
                                        u'Jack Black', u'Joe Pesci', u'John Hurt',
                                        u'John Ratzenberger', u'Joseph Gordon-Levitt',
                                        u'Michael Biehn', u'Michael Kelly', u'Robert De Niro',
                                        u'Robert Downey Jr.', u'Sean Connery',
                                        u'Stellan Skarsg\xe5rd']))
    check(g.get_node(Node('Robert De Niro')).attr['titles'], set([u'Casino', u'Once Upon a Time in America', u'Ronin']))
    check(g.get_node(Node('Meryl Streep')).attr['titles'], set([u'Manhattan']))
    check(g.get_node(Node('Sharon Stone')).attr['titles'], set([u'Casino', u'Total Recall']))
    check(g.get_node(Node('Winona Ryder')).attr['titles'], set([u'A Scanner Darkly']))
    check(g.get_node(Node('Robert Downey Jr.')).attr['titles'], set([u'A Scanner Darkly', u'Good Night, and Good Luck.',
                                                                    u'Iron Man', u'Kiss Kiss Bang Bang']))
    return 2

def test_g_02():
    '''Check a simple input'''
    import program03
    from program03 import Node
    g = program03.actor_graph('file03_02_in.json')
    check(len(g.nodes()), 2551)
    check(program03.degree(g, 70), set([u'Brad Pitt', u'Chris Cooper', u'Christopher Plummer',
                                        u'Philip Seymour Hoffman', u'Tom Cruise']))
    check(program03.degree(g, 60), set([u'Brad Pitt', u'Chris Cooper', u'Christopher Plummer',
                                            u'Ed Harris', u'John Ratzenberger',
                                            u'Philip Seymour Hoffman', u'Tom Cruise']))
    check(g.get_node(Node('Robert De Niro')).attr['titles'], set([u'Meet the Parents', u'Sleepers', u'Stardust',
                                                                  u'The Deer Hunter']))
    check(g.get_node(Node('Meryl Streep')).attr['titles'], set([u'Adaptation.', u'The Deer Hunter']))
    check(g.get_node(Node('Sharon Stone')).attr['titles'], set([u'Total Recall']))
    check(g.get_node(Node('Winona Ryder')).attr['titles'], set([u'A Scanner Darkly', u'Beetle Juice',
                                                                u'Girl, Interrupted', u'Star Trek']))
    check(g.get_node(Node('Brad Pitt')).attr['titles'], set([u'Meet Joe Black', u'Megamind', u'Moneyball', u'Se7en',
                                                             u'Sleepers', u'True Romance']))
    check(g.get_node(Node('Meg Ryan')).attr['titles'], set([u'When Harry Met Sally...']))
    check(g.get_node(Node('Cameron Diaz')).attr['titles'], set([u'Being John Malkovich', u'Gangs of New York', u'Shrek',
                                                                u'Shrek 2']))
    return 3

tests = [test_g_01,test_g_02]

if __name__ == '__main__': runtests(tests)
