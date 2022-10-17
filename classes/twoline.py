from line import line
class twoline(line):
    def __init__(self, a, b):
        super().__init__(a)
        self.b = b
    
    def did(self):
        return f'{self.a}, {self.b}'

if __name__ == '__main__':
    h = twoline(5, 6)
    print(h.did())
