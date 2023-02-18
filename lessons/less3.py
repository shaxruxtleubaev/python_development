import random
'''
print('TASK 1')
a = ['a', 'b', 'c', 'd', 'e']
print(*a)
p = ' '.join(a)
p.replace(' ','')
print(p)

print('TASK 2')
name = input('Введите имя: ')
surname = input('Введите фамилию: ')
print(f'{name}{surname}')
print()

print('TASK 3')
inp = int(input('Введите число: '))
lst = []
for i in range(inp):
    lst.append(i)

with open('Number.txt', mode='a') as file:
    file.write(f'\n{inp}')
    for i in range(inp):
        file.write(f'\n{i}')
    file.close()
print()
'''

'''
raw = []
for i in range(3):
    col = []
    for j in range(3):
        col.append(int(input('Введите число: ')))
    raw.append(col)
for i in raw:
    print(i)
a1 = raw[0][0] + raw[0][1] + raw[0][2]
a2 = raw[1][0] + raw[1][1] + raw[1][2]
a3 = raw[2][0] + raw[2][1] + raw[2][2]
a4 = raw[0][0] + raw[1][0] + raw[2][0]
a5 = raw[0][1] + raw[1][1] + raw[2][1]
a6 = raw[0][2] + raw[1][2] + raw[2][2]
a7 = raw[2][0] + raw[1][1] + raw[0][2]
a8 = raw[0][0] + raw[1][1] + raw[2][2]
print(a1, a2, a3, a4, a5, a6, a7, a8)

if a1 == a2 and a2 == a3 and a3 == a4 and a4 == a5 and a5 == a6 and a6 == a7 and a7 == a8:
    print(f'Magic function: {True}')
else:
    print(f'Magic function: {False}')
print()
'''

a = "abcd"
print(a)
g = a.replace('', ' ')
print(g)
l = g.split(' ')
print(l)
l.pop(0)
l.pop(-1)
print(l)

print(f'{l[0].upper()} - {l[1].upper()}{l[1]} - {l[2].upper()}{l[2]}{l[2]}{l[2]} - {l[3].upper()}{l[3]}{l[3]}{l[3]}')





