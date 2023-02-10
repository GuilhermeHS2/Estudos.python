from random import randint
from time import sleep
computador = randint(0,5) # Faz o computador 'PENSAR'
print('-=-' *20)
print('Vou pensar em um numero entre 0 a 5. Tente adivinhar...')
print('-=-'*20)
jogador = int(input('Em que numero eu pensei? ')) # Jogador tenta adivinhar
print('PROCESSANDO...')
sleep(2)
if jogador == computador:
    print('Parabens! Voce conseguiu me vencer!')
else:
    print('Ganhei! Eu pensei no numero {} e nao no {}!'.format(computador, jogador))
