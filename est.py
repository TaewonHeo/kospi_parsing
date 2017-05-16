import re

a = ['2016/05/05', '2016/05/04', '2016/05/02']
m = re.search('\d\d\d\d/\d\d/\d\d', a[1])
print m.group()