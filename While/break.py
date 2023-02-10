n = soma = 0
while True:
    n = int(input('Digite um numero: '))
    if n == 999:
        break
    soma += n
#print('A soma vale {}'.format(soma))
print(f'A soma vale {soma:.2f}')