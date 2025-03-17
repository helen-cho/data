import re

def check_match(p, word):
    print('단어:', word)
    m = p.search(word)
    if m:
        print('m.group():', m.group())
        print('m.string:', m.string)
        print('m.start():', m.start())
        print('m.end()', m.end())
        print('m.span()', m.span())
    else:
        print('no match', word)

print('정규식:ca.e', '-' * 50)
p = re.compile('ca.e')
check_match(p, 'careless')

print('정규식:^de', '-' * 50)
p = re.compile('^de')
check_match(p, 'destination')

print('정규식:se$', '-' * 50)
p = re.compile('se$')
check_match(p, 'base')
check_match(p, 'face')