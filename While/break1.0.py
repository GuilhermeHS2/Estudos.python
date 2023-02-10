soma = cont = 0
while True:
    n = int(input('Digite um numero: [digite 999 para parar]  '))
    if n == 999:
        break
    cont += 1
    soma+=n
print(f'Voce digitou {cont} numeros e a soma entre eles foi de {soma}')
