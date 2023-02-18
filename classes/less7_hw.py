
print('TASK 1')
class Soda:
    def __init__(self, soda, additive):
        self.soda = soda
        self.additive = additive

    def show_my_drink(self):
        if self.additive == '00':
            return f'Обычная газировка {self.soda}'
        else:
            return f'{self.soda} и {self.additive}'

if __name__ == '__main__':
    a = input('Какую газировку вы хотите: ')
    b = input('Напишите имя добавки. Если не хотите добавки, то просто напишите 00: ')
    c = Soda(a, b)
    with open('Soda.txt', mode='a', encoding='utf8') as file:
        file.write(f'\n{c.show_my_drink()}')
        file.close()
    print(c.show_my_drink())
print()

print('TASK 2')
class TriangleChecker:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    
    def is_triangle(self):
        l = 1
        
        if self.a < 0 or self.b < 0 or self.c < 0:
            return f'С отрицательными числами ничего не выйдет'
        elif self.a + self.b < self.c or \
            self.a + self.c < self.b or\
                self.b + self.c < self.a:
                return f'Жаль, но из этого треугольник не сделать!'
        else:
            return f'Ура, можно построить треугольник: '
                
if __name__ == '__main__':
    p = None
    try: 
        a, b, c = int(input('a: ')), int(input('b: ')), int(input('c: '))     
        q = TriangleChecker(a, b, c)
        print(q.is_triangle())
        p = q.is_triangle()
    except ValueError:
        print('Нужно вводить только числа!')
        p = 'Нужно вводить только числа!'
    finally:
        with open('TriangleChecker.txt', mode='a', encoding='utf8') as file:
            file.write(f'\n{p}')
            file.close()
print()



        
        






