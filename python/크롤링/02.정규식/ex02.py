import re

def print_match(p, word):
    m = p.match(word)
    if m:
        print(word, 'match')
    else:
        print(word, 'no match')

print('ca.e 정규식', '-' * 50)
p = re.compile('ca.e')
print_match(p, 'care')
print_match(p, 'cafe')
print_match(p, 'case')
print_match(p, 'caffe')

print('^de 정규식', '-' * 50)
p = re.compile('^de')
print_match(p, 'desk')
print_match(p, 'destination')
print_match(p, 'fade')

print('se$ 정규식', '-' * 50)
p = re.compile('se$')
print_match(p, 'case')
print_match(p, 'base')
print_match(p, 'face')