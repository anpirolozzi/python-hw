#! /usr/bin/env python -B

from testlib import check, run, runtests, check_file

def test_tw_01():
    '''Check a simple input'''
    import program02
    stats = program02.tw_stats('file02_01_in.json')
    check(stats, {'retweeted': {'count': 273,'max': 58402,'name': u'NiallOfficial',
                               'text': u"#privacy ! Doesn't exist"},
                  'tweets': 1000,
                  'users': {'max_followers': 331310, 'name': u'stinsonsays'},
                  'words': {'count': 2167, 'most_freq': [u'about', u'christmas', u'people']}})
    return 2

def test_tw_02():
    '''Check a simple input'''
    import program02
    stats = program02.tw_stats('file02_02_in.json')
    check(stats, {'retweeted': {'count': 368,'max': 57057,'name': u'Louis_Tomlinson',
                                'text': u"It's my birthday tomorrow ahhhhhh !! How is everyone?"},
                  'tweets': 1500,
                  'users': {'max_followers': 105293, 'name': u'Kuwaiti1DLover'},
                  'words': {'count': 2926,
                            'most_freq': [u'about', u'christmas', u'follow', u'people']}})
    return 3

tests = [test_tw_01,test_tw_02]

if __name__ == '__main__': runtests(tests)
