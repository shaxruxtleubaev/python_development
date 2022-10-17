class Armstrong:
     
    def __init__(self, num):
        self.num = num
    
    def solve(self):
        if self.num > 9:
            number = str(self.num)
            a = number.replace('', ' ')
            b = a.split()
            c = []
            for i in range(len(b)):
                c.append(pow(int(b[i]), 3))
        if self.num in range(1, 10):
            return f'This is an Armstrong number'
        else:
            if sum(c) == self.num:
                return f'{self.num} is an Armstrong number'
            else:
                return f'{self.num} is not an Armstrong number'

if __name__ == '__main__':
    inp = int(input('Enter a number: '))
    print(Armstrong(inp).solve())
    with open('Armstrong.txt', mode='a', encoding='utf-8') as file:
        file.write(f'\n{inp}')
        file.write(f'\n{Armstrong(inp).solve()}')
        file.close()