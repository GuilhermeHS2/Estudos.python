soma = 0
cont = 0
for c in range (1, 7):
        n = int(input('Digite o {} valor: '.format(c)))
        if n % 2 == 0:
         cont += 1
         soma += n
print('Dos 6 numeros digitados {} eram pares a soma de todos eles e igual a  {}'.format(cont,soma))

