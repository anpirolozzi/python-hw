#! /usr/bin/env python -B

from testlib import check, run, runtests, check_file

class Weaver1(object):
    def point(self, r, c, v):
        return (r + c + v) % 275

class Weaver2(object):
       def point(self, r, c, v):
           return (r*c + v) % 323

class Weaver3(object):
       def point(self, r, c, v):
           return (r + c + (v//7)**2) % 437

def test_loom_01():
    '''Check a simple input'''
    import program03
    s1 = Weaver1()
    s2 = Weaver2()
    l = program03.Loom(300)
    l.add_weaver(s1)
    l.add_weaver(s2)
    l.weave()
    program03.saveasimg('file03_01_out.png', l)
    check_file('file03_01_out.png', 'file03_01_check.png')
    return 2

def test_loom_02():
    '''Check a simple input'''
    import program03
    s1 = Weaver1()
    s2 = Weaver2()
    s3 = Weaver3()
    l = program03.Loom(300)
    l.add_weaver(s1)
    l.add_weaver(s2)
    l.add_weaver(s2)
    l.add_weaver(s3)
    l.weave()
    program03.saveasimg('file03_02_out.png', l)
    check_file('file03_02_out.png', 'file03_02_check.png')
    return 3

tests = [test_loom_01,test_loom_02]

if __name__ == '__main__': runtests(tests)
