import argparse, csv, glob, image

msg_ok =  '{test:<30} ok -> {points} points'
msg_err = '{test:<30} error -> {exname}\n    {exmsg}'

def run(tests,verbose):
    results = []
    for test in tests:
        try:
            v = test()
            print msg_ok.format(test=test.func_name,points=v)
        except Exception as e: 
            print msg_err.format(test=test.func_name,
                                 exname=e.__class__.__name__,
                                 exmsg=unicode(e) if unicode(e) else '')
            v = 0
        results.append( (test.func_name,v) )
    return results

def description(tests):
    for test in tests:
        print test.func_name + ': ' + test.__help__

def log(results,filename):
    with open(filename,'wb') as f:
        writer = csv.writer(f)
        writer.writerows(results)
        
def check(a,b):
    assert a == b, '%r != %r' % (a, b)

def check_img(a,b):
    img_a = image.load(a)
    img_b = image.load(b)
    assert img_a == img_b, 'images differ: ' + a + ' ' + b

def check_file(a,b):
    with open(a,'rU') as f: txt_a = f.read()
    with open(b,'rU') as f: txt_b = f.read()
    lines_a = [l.strip() for l in txt_a.splitlines()]
    lines_b = [l.strip() for l in txt_b.splitlines()]
    assert lines_a == lines_b, 'text differ: ' + a + ' ' + b

def runtests(tests,verbose=True,logfile=''):
    results = run(tests,verbose)
    if logfile: log(results,logfile)
