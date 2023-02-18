from triangle import triangle

class square(triangle):

    def __init__(self, a, b, c, d):
        super().__init__(a, b, c)
        self.d = d

    def pot(self):
        return f'{self.a}, {self.b}, {self.c}, {self.d}'

if __name__ == '__main__':
    z = square(5, 6, 7, 8)
    print(z.pot())