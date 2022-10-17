import random
'''
print('TASK 1')
a = input(': ')
print(a)
g = a.replace('', ' ')
l = g.split(' ')
l.pop(0)
l.pop(-1)
print(l)
l.sort()
print(l[0], l[1])
'''




# exp_sum(1) # 1 
# exp_sum(2) # 2 -> 1+1 , 2 
# exp_sum(3) # 3 -> 1+1+1, 1+2, 3 
# exp_sum(4) # 5 -> 1+1+1+1, 1+1+2, 1+3, 2+2, 4 
# exp_sum(5) # 7 -> 1+1+1+1+1, 1+1+1+2, 1+1+3, 1+2+2, 1+4, 5, 2+3
'''print('5')
def f(a, n, p):
    if n:
        for i in range(n+1, 0, -1):
            if i <= p:
                f(a+[i], n-i, i)
    else:
        print(*a, sep=' + ')
n = int(input())
f([], n, n)'''



# pot = 23013203430201
# print(pot)
# b = list(map(int, str(pot)))
# u = b
# print(u)
# a = []
# b = []
# for i in range(len(u)):
#     if u[i] == 0:
#         a.append(u[i])
#     else:
#         b.append(u[i])
# b.extend(a)
# print(b)
# for i in range(len(u)):
#     if u[i] == 0:
#         u.remove(0)
#         u.append(0)
# print(u)



