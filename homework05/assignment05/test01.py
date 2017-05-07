#! /usr/bin/env python -B

from testlib import check, run, runtests, check_file

def test_img_01():
    '''Check a simple input'''
    import program01
    img = program01.Image(200, 100, program01.Color(0, 0, 255))
    program01.h_line(img, 20, program01.Color(255, 0, 0))
    c = img.get_pixel(20, 20)
    c.b = 200
    img2 = img.copy()
    program01.h_line(img, 40, program01.Color(255, 0, 0))
    program01.save('file01_01_out.png', img)
    check_file('file01_01_out.png', 'file01_01_check.png')
    return 2

def test_img_02():
    '''Check a simple input'''
    import program01
    img = program01.Image(100, 80, program01.Color(128, 128, 255))
    img2 = img.copy()
    program01.h_line(img2, 50, program01.Color(100, 20, 20))
    program01.h_line(img, 70, program01.Color(20, 128, 0))
    program01.save('file01_02_out.png', img2)
    check_file('file01_02_out.png', 'file01_02_check.png')
    return 3

tests = [test_img_01,test_img_02]

if __name__ == '__main__': runtests(tests)
