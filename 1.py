import os
from typing import Tuple

from numpy import random

os.system('cls')

marxes = ['Groucho', 'Chico', 'Harpo', 'kuingi']
print("Старт программы \n" + str(marxes) + '\n')

marxes.append('zippo')
print(
    "marxes.append ('zippo') is:\n"
    + str(marxes)
    + '\n'
)

b = marxes[::-1]
marxes.extend(b)
print('marxes.extend(b) is \n '
      + str(marxes)
      + '\n'
      )

marxes.insert(5, 'Goliaff')

print(
    "marxes.insert(5,'Goliaff')\n"
    + str(marxes)
    + "\n Длина списка: " + str(len(marxes))
    + "\n"
)

print(
    'del marxes [5] is = '
    + marxes[5]
    + '\n'
)

del marxes[5]

print(
    'result after del:\n'
    + str(marxes)
    + "\nДлина списка: " + str(len(marxes))
    + "\n"
)

marxes.remove('zippo')

print(
    "marxes.remove('zippo')"
    + "\n"

)

print(
    'marxes.pop(0) is = '
    + str(marxes.pop(0))
    + "\n"
    + str(marxes)
    + "\nДлина списка: "
    + str(len(marxes))

    + 'после удоаления с применением.pop(0)'
    + "\n"
)

print(
    'Применение функции index'
    + '\n'
    + "результат функции marxes.index('Harpo') = "
    + str(marxes.index('Harpo'))
    + '\n'
)

print(
    'Add "zippo 20 times" '
    + "\n"
)

for i in range(20):
    marxes.append('zippo')
    i += 1

print(
    'Use for and "in" to remove zippo '
    + 'list before execute: '
    + '\n'
    + str(marxes)
    + "\nДлина списка: " + str(len(marxes))
    + "\n"
)

counter = 0
broname = 'zippo'

for broname in range(len(marxes)):
    try:
        del marxes[marxes.index('zippo')]
        counter += 1
    except:
        break
print(
    'success!!! '
    + str(counter)
    + ' times \n'
    + 'list  after execute: '
    + '\n'
    + str(marxes)
    + "\nДлина списка: " + str(len(marxes))
    + "\n"
)
x = 0
x2 = random.randint(12)

print(
    'Starting random insertion x= '
    + str(x)
    + '\n x2= '
    + str(x2)
)

while x < x2:
    r = random.randint(len(marxes))
    marxes.insert(r, 'zhoppa')
    # print (r)
    x += 1

print(
    'ranmom num is '
    + str(x)
    + 'list  after execute: '
    + '\n'
    + str(marxes)
    + "\nДлина списка: " + str(len(marxes))
    + "\n"
)

print(
    "marxes.count('zhoppa') is ==  "
    + str(marxes.count('zhoppa'))
    + '\n'
    + ','.join(marxes)
    + '\n\n\n'
)

str_maexes = ','.join(marxes)

coma_separator = ','
marxes_from_str = str_maexes.split(coma_separator)

print(
    str_maexes
    + '\n'
    + str(marxes_from_str)
    + '\n' + '\n' + '\n'
    + str(marxes == marxes_from_str)

)

marxes_from_str.sort()

print(
    'this is 2nd listing '
    + '\n'
    + str(sorted(marxes))
    + '\n\n\n original marxes: \n '
    + str(marxes)
    + '\n'
    + 'this is .sort str_maexes listing '
    + '\n'
    + str(marxes_from_str)
    + '\n' + '\n' + '\n'
    + 'this is "marxes_from_str"'
    + '\n'
    + str(marxes_from_str)
)

print('hello-git \n')

a = [1, 2, 3, 4]
print(a)
b = a.copy()
c = list(a)
d = a[:]
a[0] = 'kuku'
print(
    '{0}\n{1}\n{2}\n{3}\n{4}'.format(str(a), str(b), str(c), str(d), str(marxes))
)

########################corteges
print(
    '#########################################corteges###############################\n\n'
)

ecortege = ()
print(ecortege)

tpl1 = ('odin', 'dva', 'tris')

print(
    "{}\n{}\n ".format(str(tpl1), str(type(tpl1))))

a, b, c = tpl1



print(
    '{},{},{}'.format(str(a), str(b), str(c))
      )

marx_list = ['Groucho', 'Chico', 'Harpo']
#convert list to tuple
qq=tuple(marx_list)

print(
    '{},\n{},'.format(str(marx_list), str(qq))
      )

