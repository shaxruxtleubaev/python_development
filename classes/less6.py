'''
class figure(object):
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def solve(self):
        return f'P = {(self.a+self.b)*2}, S = {self.a * self.b}'

class square(object):
    def __init__(self, a):
        self.a = a
    def solve(self):
        return f'P = {self.a * 4}, S = {self.a ** 2}'

class circle(object):
    def __init__(self, R):
        self.R = R
    def solve(self):
        P = 3.14
        return f'L = {2 * P * self.R}, S = {P * pow(self.R, 2)}'

if __name__ == '__main__':
    fin = figure(5, 10)
    dif = square(5)
    difff = circle(5)
    print(dif.solve())
    print(difff.solve())
    print(fin.solve())
'''
class squ(object):
    def __init__(self, x1, y1, x2, y2, x3, y3, x4, y4):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.x3 = x3
        self.y3 = y3
        self.x4 = x4
        self.y4 = y4

    def solve(self):
        ab = pow(pow(self.x2 - self.x1, 2) + pow(self.y2 - self.y1, 2), 0.5)
        bc = pow(pow(self.x3 - self.x2, 2) + pow(self.y3 - self.y2, 2), 0.5)
        cd = pow(pow(self.x4 - self.x3, 2) + pow(self.y4 - self.y3, 2), 0.5)
        ad = pow(pow(self.x4 - self.x1, 2) + pow(self.y4 - self.y1, 2), 0.5)
        P = ab + bc + cd + ad
        S = ab * bc * cd * ad
        return f'P = {int(P)} S = {int(S)}'
if __name__ == '__main__':
    x1, y1, x2, y2, x3, y3, x4, y4 = int(input('x1: ')), int(input('y1: ')), int(input('x2: ')), int(input('y2: ')), int(input('x3: ')), int(input('y3: ')), int(input('x4: ')), int(input('y4: '))
    final = squ(x1, y1, x2, y2, x3, y3, x4, y4)
    print(final.solve())
