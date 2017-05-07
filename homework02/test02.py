#! /usr/bin/env python -B

from testlib import check, run, runtests

def test_addr_phone_01():
    '''Check a simple input'''
    import program02
    check(program02.addr_phone({'Giorgio': 'via Verdi, 23', 'M. Bianchi': 'Piazza Milano, 1',
                                'L. De La': 'via A. Einstein, 12', 'Ciro': 'via Pio'},
                               {'Marco': '347 8987989', 'giorgio': '06 89786765',
                                'Mauro B.': '3489878675', 'Ciro': '07897878',
                                'L. De La': '09877887'}),
          {'Giorgio':{'address': 'via Verdi, 23'}, 'Marco':{'phone': '347 8987989'},
           'giorgio':{'phone': '06 89786765'},
           'L. De La':{'phone': '09877887','address': 'via A. Einstein, 12'},
           'Ciro':{'phone': '07897878', 'address': 'via Pio'},
           'Mauro B.':{'phone': '3489878675'},
           'M. Bianchi': {'address': 'Piazza Milano, 1'}})
    return 3

def test_addr_phone_02():
    '''Check a simple input'''
    import program02
    check(program02.addr_phone({'blue': 'place', 'white': 'boh', 'BLACK': '1234',
                                'red': 'street'},
                               {'blue': 'number', 'gray': 'Num', 'red': 'Phone',
                                'Red': 'TEL'}),
          {'blue':{'phone': 'number', 'address': 'place'},
           'gray':{'phone': 'Num'}, 'BLACK':{'address': '1234'},
           'red':{'phone': 'Phone', 'address': 'street'},'white':{'address': 'boh'},
           'Red':{'phone': 'TEL'}})
    return 3

tests = [test_addr_phone_01,test_addr_phone_02]

if __name__ == '__main__': runtests(tests)
