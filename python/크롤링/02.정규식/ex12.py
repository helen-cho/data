import re

p = re.compile('se$')
m = p.search('case')
if m:
    print('m.group()', m.group())
    print('m.string', m.string)
    print('m.start()', m.start()) 
    print('m.end()', m.end())
    print('m.span()', m.span())
else:
    print('no match')

m = p.search('base')
if m:
    print('m.group()', m.group())
    print('m.string', m.string)
    print('m.start()', m.start()) 
    print('m.end()', m.end())
    print('m.span()', m.span())
else:
    print('no match')