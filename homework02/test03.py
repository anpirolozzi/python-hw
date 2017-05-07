#! /usr/bin/env python -B

from testlib import check, run, runtests

def test_f_phone_addr_01():
    '''Check a simple input'''
    import program03
    check(program03.f_phone_addr('file03_01_in.txt', 'file03_02_in.txt'),
          {'Giorgio': {'address': 'via Verdi, 23'},
           'Marco': {'phone': '347 8987989'},
           'giorgio': {'phone': '06 89786765'},
           'L. De La': {'phone': '09877887', 'address': 'via A. Einstein, 12'},
           'Ciro': {'phone': '07897878', 'address': 'via Pio'},
           'Mauro B.': {'phone': '3489878675'},
           'M. Bianchi': {'address': 'Piazza Milano, 1'}})
    return 3

def test_f_phone_addr_02():
    '''Check a simple input'''
    import program03
    check(program03.f_phone_addr('file03_03_in.txt', 'file03_04_in.txt'),
          {'Trani': {'address': 'Gioia Tauro'}, 'Marco': {'phone': '347 8987989'},
           'Ugo': {'address': 'via Po, 346'}, 'trani': {'phone': '07897878'},
           'GG': {'phone': '06 89786765'},
           'Bianconi': {'address': 'Viale Milano, 10'},
           'Rosso G.': {'phone': '0988 97987 08098', 'address': 'via Verdi, 23'},
           'De Simoz': {'phone': '34898777777888888885', 'address': 'via B. Bolla'}})
    return 3

tests = [test_f_phone_addr_01,test_f_phone_addr_02]

if __name__ == '__main__': runtests(tests)
