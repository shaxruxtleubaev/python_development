import random

print('TASK 1')
class numbers(object):
    def __init__(self, lst):
        self.lst = lst
    
    def final(self):
        a = sorted(self.lst)
        b = []
        for i in range(len(a)-1):
            b.append(a[i+1] - a[i])
        b.append(a[-1] - a[-2])
        e = max(b)
        f = b.index(e)
        return f'Наибольшая разность - {e}, между {a[f]} и {a[f+1]}'

if __name__ == '__main__':
    d = [random.randint(0, 20) for i in range(10)]
    print(sorted(d))
    c = numbers(d)
    print(c.final())
    with open('text.txt', mode='a', encoding='utf8') as file:
        file.write(f'\n{d}')
        file.write(f'\n{c.final()}')
        file.close()
print()

print('TASK 2')
class words(object):
    def __init__(self, word1, word2):
        self.word1 = word1
        self.word2 = word2

    def intersection(self):
        a = self.word1.replace('', ' ')
        b = a.split()
        c = self.word2.replace('', ' ')
        d = c.split()
        e = []
        for i in range(len(b)):
            if b[i] in d:
                e.append(b[i])
        e.sort()
        f = "".join(e)
        return f

if __name__ == '__main__':
    word1 = input('word1: ').lower()
    word2 = input('word2: ').lower()
    q = words(word1, word2)
    l = q.intersection()
    print(q.intersection())
    with open('text.txt', mode='a', encoding='utf8') as file:
        file.write(f'\nword1: {word1}')
        file.write(f'\nword2: {word2}')
        file.write(f'\n{q.intersection()}')
        file.close()
print()

