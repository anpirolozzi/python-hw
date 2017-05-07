#! /usr/bin/env python -B

from testlib import check, run, runtests, check_img

def test_rotate_mosaic_01():
    '''Check a simple input'''
    import program06
    program06.rotate_mosaic('img06_01_in.png','img06_01_out.png',128,32)
    check_img('img06_01_out.png','img06_01_check.png')
    return 3

def test_rotate_mosaic_02():
    '''Check a simple input'''
    import program06
    program06.rotate_mosaic('img06_02_in.png','img06_02_out.png',32,32)
    check_img('img06_02_out.png','img06_02_check.png')
    return 3

tests = [test_rotate_mosaic_01,test_rotate_mosaic_02]

if __name__ == '__main__': runtests(tests)
