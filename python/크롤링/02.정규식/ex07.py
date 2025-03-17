import re

p = re.compile('se$')

m = p.match('case')
if m:
    print('match')
else:
    print('no match')

m = p.search('case')
if m:
    print('match')
else:
    print('no match')

m = p.search('seek')
if m:
    print('match')
else:
    print('no match')


