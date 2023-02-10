nub = cont = soma = 0
nub = int(input('Digite um numero [999 para parar]:  '))
while nub != 999:
    soma += nub
    cont += 1
    nub = int(input('Digite um numero [999 para parar]:  '))
print('Voce digitou {} numeros e a soma entre eles {}'.format(cont,soma))