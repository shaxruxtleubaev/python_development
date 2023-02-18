class line:

    def __init__(self, a):
        self.a = a
    
    def ret(self):
        return f'{self.a}'
if __name__ == '__main__':
    t = line(5)
    print(t.ret())