import re

p = re.compile('^de')

m = p.match('desk')
if m:
    print('match')
else:
    print('no match')

m = p.match('fade')
if m:
    print('match')
else:
    print('no match')

m = p.match('destination')
if m:
    print('match')
else:
    print('no match')