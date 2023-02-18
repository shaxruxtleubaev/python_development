from twoline import twoline

class triangle(twoline):

    def __init__(self, a, b, c):
        super().__init__(a, b)
        self.c = c
    
    def jui(self):
        return f'{self.a}, {self.b}, {self.c}'

if __name__ == '__main__':
    n = triangle(5, 6, 7)
    print(n.jui())