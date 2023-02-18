import random

print('TASK 1, 2')
class RimCel:

    def __init__(self, n):
        self.n = n
    
    def solve(self):
        u = {'l' : 1,'V' : 5, 'X' : 10, 'L' : 50, 'C' : 100, 'D' : 500, 'M' : 1000}
        a = self.n
        b = a.replace('', ' ')
        c = b.split()
        e = []

        for i in range(len(c)):
            if c[i] in u:
                e.append(u[c[i]])
        
        if e[-1] > e[-2]:
            e[-1] -= e[-2]
            e.remove(e[-2])

        return f'{sum(e)}'

if __name__ == '__main__':
    y = input('enter rimic number: ')
    p = RimCel(y)
    print(p.solve())
    with open('Itog.txt', mode='a', encoding='utf-8') as file:
        file.write(f'\n{y}')
        file.write(f'\n{p.solve()}')
        file.write(f'\n')
        file.close()
print()

print('TASK 3')
class couple_numbers_eq:

    def __init__(self, lst, inp):
        self.lst = lst
        self.inp = inp
    
    def find(self):
        lst = self.lst
        for i in range(len(lst)):
            for j in range(len(lst)):
                if lst[i] + lst[j] == self.inp:
                    return f'{lst[i]} + {lst[j]} == {self.inp}'
                else:
                    pass

if __name__ == '__main__':
    lst = [random.randint(-10, 50) for i in range(5)]
    print(lst)
    inp = int(input('Введите целевое число: '))
    print(couple_numbers_eq(lst, inp).find())
    with open('couple_number.txt', mode='a', encoding='utf-8') as file:
        file.write(f'\n{lst}')
        file.write(f'\n{inp}')
        file.write(f'\n{couple_numbers_eq(lst, inp).find()}')
print()

print('TASK 4')
class triple_num:

    def __init__(self, lst):
        self.lst = lst
    
    def solve(self):
        fin = []
        lst = self.lst
        try:
            for i in range(len(lst)):
                for j in range(len(lst)):
                    for x in range(len(lst)):
                        if lst[i] + lst[j] + lst[x] == 0:
                            fin.append([lst[i], lst[j], lst[x]])
        except TypeError:
            print(f'Ошибка при вводе!')
        finally:          
            return f'{fin}'
        # Если бы я не пользовался try, то в итоге вышло бы только 
        # одна пара трех чисел, остальные не добавились бы
        
if __name__ == '__main__':
    lst = [-25, -10, -7, -3, 2, 4, 8, 10]
    print(lst)
    print(triple_num(lst).solve())
    with open('triple_num.txt', mode='a', encoding='utf-8') as file:
        file.write(f'\n{lst}')
        file.write(f'\n{triple_num(lst).solve()}')
        file.close()
print()

print('TASK 5')
class Python:

    def __init__(self, a):
        self.a = a

    def get_string(self):
        pass                  #Не понял зачем нужно было это

    def print_String(self):
        return f'{self.a.upper()}'
        
if __name__ == '__main__':
    h = input('str: ')
    print(Python(h).print_String())
    with open('Str.txt', mode='a', encoding='utf8') as file:
        file.write(f'\n{h}')
        file.write(f'\n{Python(h).print_String()}')
print()