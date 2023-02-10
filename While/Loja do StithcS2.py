soma = quanti =  menor = mil = 0
menos = ' '
print('{:-^40}'.format(' Bem vindo a loja do tio StitchS2 '))
while True:
    produto = str(input('Nome do produto: '))
    valor = float(input('preco: R$'))
    resp = ' '
    soma+=valor
    quanti+=1
    if quanti == 1 or valor < menor:
        menor = valor
        menos = produto
        if valor >= 1000:
            mil+=1
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print('{:-^40}'.format(' FIM DO PROGRAMA '))
print(f' O total da compra foi de R${soma:.2f}\n Temos {mil} produtos que custando mais de R$1000.00\n O produto mais barato foi {menos} que custa R${menor}')


