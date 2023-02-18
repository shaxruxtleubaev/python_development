import random

print('1.')
list = []
for i in range(5):
    a = int(input(':'))
    list.append(a)
print(list)
list.sort()
list.reverse()
print(list)

print('2.')
b = [random.randint(-20, 20) for i in range(5)]
for i in range(len(b)):
    print(b[i])

print('3.')
lst = []
f = True
while f:
    c = int(input(':'))
    if c in range(10, 21):
        lst.append(c)
    if c not in range(10, 21):
        print('Вне диапазона!')
    if len(lst) == 5:
        print('Спасибо')
        print(lst)
        break

print('4.')
massive = [2, 2, 5, 7, 7]
print(massive)
t = int(input('Введите какое нибудь число из массива: '))
x = 0
for i in range(5):
    if t == massive[i]:
        x += 1
print(x)

print('5.')
d = []
for i in range(3):
    d.append(int(input('Введите число: ')))
r = [random.randint(-20, 20) for i in range(5)]
d.extend(r)
d.sort()
for i in range(len(d)):
    print(d[i])