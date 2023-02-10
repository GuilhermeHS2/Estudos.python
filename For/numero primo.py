'''
n = int(input('Digite um numero:  '))
for c in range (1, n + 1):
    cont += 1
    print(cont, end=' ')
    if n / c == n or n / c == 1:
        print('O numero {} foi divisivel 2 vezes e por isso ele e primo'.format(n))'''
n = int(input('Digite um numero: '))
tot = 0
for c in range (1, n +1):
    if n % c == 0:
        print('\033[34m', end=' ')
        tot += 1
    else:
        print('\033[31m', end=' ')
    print('{}'.format(c), end=' ')
print('\n\033[mO numero {} foi divisivel {} vezes'.format(n, tot))
if tot == 2:
    print('E por isso ele e primo')
else:
    print('E por isso ele nao e primo')

