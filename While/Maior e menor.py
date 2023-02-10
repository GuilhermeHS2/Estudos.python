'''n = int(input('Digite um nuemro: '))
conti = str(input('Quer continuar? [S/N]  ')).strip().upper()[0]
cont = 1
soma = 0
while conti not in 'N':
    n =  int(input('Digite outro numero: '))
    conti = str(input('Quer continuar? [S/N]  ')).upper().strip()[0]
    cont +=1
    soma +=n
    soma = soma/cont
print('Voce digitou {} numeros e a media foi {:.2f}\n O maior valor foi {} e o menor foi {}'.format(cont,soma,ma,me))'''
resp = 'S'
soma = quanti = media = maior = menor = 0
while resp in 'Ss':
    n = int(input('Digite um numero: '))
    soma +=n
    quanti +=1
    if quanti == 1:
        maior = menor = n
    else:
        if n > maior:
           maior = n
        if n < menor:
            menor = n
    resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
media = soma / quanti
print('Voce digitou {} numeros e a media foi {:.2f}\n O maior valor foi {} e o menor foi {} '.format(quanti,media,maior,menor))


