import random
'''
print('TASK 1')
num = [random.randint(0, 100) for i in range(5)]
with open('Numbers.txt', mode='a') as file:
    file.write(f'\n{num[0]}, {num[1]}, {num[2]}, {num[3]}, {num[4]}')
    file.close()
print()

print('TASK 2')
n1 = input('Enter name: ')
n2 = input('Enter name: ')
n3 = input('Enter name: ')
n4 = input('Enter name: ')
n5 = input('Enter name: ')
with open('Names.txt', mode='a') as file:
    file.write(f'\n{n1}')
    file.write(f'\n{n2}')
    file.write(f'\n{n3}')
    file.write(f'\n{n4}')
    file.write(f'\n{n5}')
    file.close()
print()

print('TASK 3')
f = open('Names.txt')
print(f.read())
print()

print('TASK 4')
h = open('Names.txt', mode='a')
inp = input('Введите имя чтобы добавить в файл Names.txt: ')
h.write(f'\n{inp}')
h.close()
print()

print('TASK 5')
while True:
    ask = input('Введите число 1, 2 или 3: ')
    if ask == '1':
        subject = input('Введите имя школьного предмета: ')
        with open('Subject.txt', mode='w') as file:    #mode='w' это удаляет прошлый файл и создает новый
            file.write(f'\n{subject}')
            file.close()
        break
    elif ask == '2':
        n = open('Subject.txt', mode='r')              #mode='r' это открытия файла на чтение
        print(n.read())
        break
    elif ask == '3':
        asking = input('Введите новую тему: ')
        with open('Subject.txt', mode='a') as file:
            file.write(f'\n{asking}')
            file.close
        final = open('Subject.txt')
        print(final.read())
        break
    else:
        print('Ошибка при вводе, повторите попытку!')
        continue
print()
'''
print('TASK 6')



