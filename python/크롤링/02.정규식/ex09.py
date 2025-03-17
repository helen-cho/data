import re

p = re.compile('ca.e')
m = p.search('good care')
if m:
    print('m.group()', m.group())
    print('m.string', m.string)
    print('m.start()', m.start())
    print('m.end()', m.end())
    print('m.span()', m.span())
else:
    print('no match')

p = re.compile('ca.e')
m = p.search('careless')
if m:
    print('m.group()', m.group())
    print('m.string', m.string)
    print('m.start()', m.start()) 
    print('m.end()', m.end())
    print('m.span()', m.span())
else:
    print('no match')