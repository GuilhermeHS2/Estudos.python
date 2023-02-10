soma = 0
media = 0
maiorh = 0
nomev = ''
totm = 0
for c in range (1,5):
    print('-----{} PESSOA -----'.format(c))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    soma+=idade
    if c == 1 and sexo in 'Mm':
        maiorh = idade
        nomev = nome
    if sexo in 'Mm' and idade > maiorh:
        maiorh = idade
        nomev = nome
    if sexo in 'Ff' and idade < 20:
        totm += 1
media = soma / 4
print('A media de idade do grupo e de {}'.format(media))
print('O Homen mais velho tem {} anos e se chama {}'.format(maiorh,nomev))
print('Ao todo sao {} com menos de 20 anos'.format(totm))