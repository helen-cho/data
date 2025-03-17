import re

#정규식 패턴을 컴파일하여 변수 p에 저장한다.
p = re.compile('ca.e')

#m.group() 함수는 정규식을 만족하면 해당 단어가 출력되고 만족하지 않으면 에러가 발생한다.
m = p.match('care')
print(m.group())

m = p.match('cafe')
print(m.group())

m = p.match('caffe')
if m:
    print('match')
else:
    print('no match')