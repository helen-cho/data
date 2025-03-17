import re

p = re.compile('ca.e')

list = p.findall('careless')
print(list)

list = p.findall('good care')
print(list)

list = p.findall('good care cafe')
print(list)

list = p.findall('case care cafe')
print(list)

list = p.findall('caffe')
print(list)
