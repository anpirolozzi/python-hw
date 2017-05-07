#! /usr/bin/env python -B

from testlib import check, run, runtests, check_img

def test_tile_mosaic_01():
    '''Check a simple input'''
    import program05
    program05.tile_mosaic('img05_01_in.png','img05_01_out.png',16,16,224,224,16,16)
    check_img('img05_01_out.png','img05_01_check.png')
    return 2

def test_tile_mosaic_02():
    '''Check a simple input'''
    import program05
    program05.tile_mosaic('img05_02_in.png','img05_02_out.png',148,10,32,32,9,9)
    check_img('img05_02_out.png','img05_02_check.png')
    return 4

tests = [test_tile_mosaic_01,test_tile_mosaic_02]

if __name__ == '__main__': runtests(tests)
