from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0,2)
print('''Suas opcoes:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogador = int(input('Qual a sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
sleep(1)
print('-=' * 11)
print('Computador Jogou {}'.format(itens[computador]))
print('Jogador jogou {}'.format(itens[jogador]))
print('-=' * 11)
if computador ==0:
   if jogador ==0:
       print('EMPATE')
   elif jogador ==1:
       print('Jogador GANHOU')
   elif jogador ==2:
       print('Computador GANHOU')


elif computador ==1:
    if jogador == 0:
        print('Computador GANHOU')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('Jogador GANHOU')


elif computador ==2:
    if jogador == 0:
        print('Jogador Ganhou')
    elif jogador == 1:
        print('Computador Ganhou')
    elif jogador == 2:
        print('EMPATE')

else:
    print('Jogada invalida')