'''lst =[]
for c in range(1,6):
   peso = float(input('Peso da pessoa{}: '.format(c)))
   lst+=[peso]
print('')
print('O maior peso foi:', max(lst))
print('O menor peso foi:',min(lst))'''
maior = 0
menor = 0
for c in range (1,6):
   peso = float(input('Peso da pessoa{}: '.format(c)))
   if c == 1:
      maior = peso
      menor = peso
   else:
      if peso > maior:
         maior = peso
      if peso < menor:
         menor = peso
print('O maior peso lido foi {}'.format(maior))
print('O menor peso lido foi {}'.format(menor))


