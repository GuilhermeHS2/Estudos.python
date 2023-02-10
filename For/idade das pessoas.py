from datetime import date
atual = date.today().year
tot = 0
tol = 0
for c in range (1, 8):
    ano = int(input('Em que ano a {} pessoa nasceu? '.format(c)))
    idade = atual - ano
    if idade >= 18:
        tot += 1
    elif idade <= 18:
        tol += 1
print('Ao todo tivemos {} pessoas maiores de idade'.format(tot))
print('E tambem tivemos {} pessoas menores de idade'.format(tol))

