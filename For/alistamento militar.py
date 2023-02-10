from datetime import date
atual = date.today().year
nasc = int(input('Ano de nascimento: '))
idade = atual - nasc
print('Quem nasceu em {} tem {} anos em {}'.format(nasc, idade, atual))
if idade == 18:
    print('Voce tem que se alistar IMEDIATAMENTE!')
elif idade < 18:
    saldo = 18 - idade
    ano = atual + saldo
    print('Ainda faltam {} anos para o alistamento'.format(saldo))
    print('Seu alistamento sera em {}'.format(ano))
elif idade > 18:
    saldo = idade - 18
    ano = atual - saldo
    print('Voce ja deveria ter se alistado ha {} anos'.format(saldo))
    print('Seu alistamento foi em {}'.format(ano))







'''ano = int(input('Ano de nascimento: '))
idade = 2022 - ano
alis = idade - 18
fo = ano + 18
if idade > 18:
    print('Voce nasceu em {} tem {} anos em 2022'.format(ano,idade))
    print('Voce ja deveria ter se alistado ha {} anos'.format(alis))
    print('Seu alistamento foi em {}'.format(fo))
elif idade < 18:
    print('Voce nasceu em {} tem {} anos em 2022'.format(ano, idade))
    print('ainda falta {} anos para o alistamento'.format(alis))
    print('Seu alistamento sera em {}'.format(fo))
elif idade == 18:
    print('Voce nasceu em {} tem {} anos em 2022'.format(ano, idade))
    print('Esta na hora do alistamento solado')'''
