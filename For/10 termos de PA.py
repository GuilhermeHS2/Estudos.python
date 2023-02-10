n = int(input('Digite um termo: '))
t = int(input('Digite uma razao: '))
d = n + (10 - 1) * t
for c in range (n,d + t,t):
    print('{}'.format(c), end=' --> ')
print('ACABOU')