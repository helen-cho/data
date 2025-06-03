import re

def print_match(p, word):
    print('단어:', word)
    m = p.search(word)
    if m:
        #일치하는 문자열 반환환
        print('m.group():', m.group())
        #입력받은 문자열(괄호없이 사용)
        print('m.string:', m.string)
        #일치하는 문자열의 시작 index
        print('m.start():', m.start())
        #일치하는 문자열의 끝 index
        print('m.end()', m.end())
        #일치하는 문자열의 시작, 끝 index
        print('m.span()', m.span())
    else:
        print('no match', word)

print('정규식:ca.e', '-' * 50)
p = re.compile('ca.e')
print_match(p, 'good care')
print_match(p, 'careless')

print('정규식:^de', '-' * 50)
p = re.compile('^de')
print_match(p, 'desk')
print_match(p, 'destination')

print('정규식:se$', '-' * 50)
p = re.compile('se$')
print_match(p, 'case')
print_match(p, 'base')
print_match(p, 'face')