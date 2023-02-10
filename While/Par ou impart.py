from random import randint
'''cont = 0
while True:
    player = int(input('Digite um numero: '))
    pc = randint(0, 10)
    escolha = str(input('Par ou Impar? [P/I]: ')).strip().upper()
    resu = player + pc
    div = resu % 2
    if div == 0:
        if escolha == 'P':
            cont+=1
            print('Voce venceu!')
            print(f'Voce jogou {player} e o computador {pc}.Total de {resu}')
        else:
            break
    else:
        if escolha == 'I':
            cont+=1
            print('Voce venceu!')
            print(f'Voce jogou {player} e o computador {pc}.Total de {resu}')
        else:
            break
print(f'Voce jogou {player} e o computador {pc}.Total de {resu}\n Voce ganhou {cont} da maquina')
print('Voce perdeu')'''
v = 0
while True:
    jogador = int(input('Digite um valor: '))
    pc = randint(0,10)
    total = jogador + pc
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou IMPAR? [P/I] ')).strip().upper()[0]
    print(f'Voce jogou {jogador} e o computador {pc}. Total de {total}')
    print('Deu PAR'if total % 2 == 0 else 'Deu IMPAR')
    if tipo == 'P':
        if total % 2 ==0:
            v += 1
            print('Voce venceu')

        else:
            print('Voce perdeu')
            break
    if tipo == 'I':
        if total % 3 ==0:
            v += 1
            print('Voce venceu')

        else:
            print('Voce perdeu!')
            break
    print('Vamos jogar novamente...')
print(f'GAME OVER, Voce venceu {v} vezes')