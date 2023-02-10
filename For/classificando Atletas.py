from datetime import date
ano = date.today().year
nasc = int(input('Ano de Nascimento: '))
idade = ano - nasc
print('O atleta tem {} anos'.format(idade))
if idade == 9:
    print('Classificacao: mirim')
elif idade > 9 and idade <= 14:
    print('Classificacao: iNFANTIL')
elif idade > 14 and idade <= 19:
    print('Classificacao: JUNIOR')
elif idade > 19 and idade <= 25:
    print('Classificacao: SENIOR')
elif idade > 25:
    print('Classificacao: MASTER')
else:
    print('Nao tem idade para competir')
