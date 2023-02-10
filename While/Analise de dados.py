'''conti = conth = contm = 0
while True:
    sexo = ' '
    idade = int(input('Idade: '))
    while sexo not in 'MF':
        sexo = str(input('[M/F]: ')).strip().upper()[0]
    if idade >= 18:
        conti+=1
    if sexo == 'M':
        conth+=1
    if idade <= 18 and sexo == 'F':
        contm+=1
    sair = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if sair == 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {conti}\n Ao todo temos {conth} homens cadastrados\n E temos {contm} mulheres com menos de 20 anos')'''
tot18 = toth = totm = 0
while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    if idade >=18:
        tot18+=1
    if sexo == 'M':
        toth+=1
    if sexo == 'F' and idade < 18:
        totm+=1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {tot18}')
print(f'Ao todo temos {toth} homens cadastrados')
print(f'E temos {totm} mulheres com menos de 20 anos')