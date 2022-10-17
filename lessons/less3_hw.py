a = input(': ')
g = a.replace('', ' ')
l = g.split(' ')
l.pop(0)
l.pop(-1)

asd = []
for i in range(len(l)):
    x = i+1
    s = l[i] * x
    asd.append(s.capitalize())
fin = ' '.join(asd)
x = fin.replace(' ', '-')
print(x)