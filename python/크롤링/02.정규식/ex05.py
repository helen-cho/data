import re

p = re.compile('ca.e')

m = p.match('care')
if m:
    print('match')
else:
    print('no match')

m = p.match('caffe')
if m:
    print('match')
else:
    print('no match')