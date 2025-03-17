import re

p = re.compile('^de')
m = p.search('desk')
if m:
    print('m.group()', m.group())
    print('m.string', m.string)
    print('m.start()', m.start()) 
    print('m.end()', m.end())
    print('m.span()', m.span())
else:
    print('no match')

p = re.compile('^de')
m = p.search('destination')
if m:
    print('m.group()', m.group())
    print('m.string', m.string)
    print('m.start()', m.start()) 
    print('m.end()', m.end())
    print('m.span()', m.span())
else:
    print('no match')