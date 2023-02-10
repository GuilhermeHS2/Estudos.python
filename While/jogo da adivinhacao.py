from random import randint
computador = randint(0,10)
cont = 0
acertou = False
print('Sou seu computador. \n Acabei de pensar em um numero de 0 e 10.\n sera que voce consegue adivinhar qual foi?')
while not acertou:
    jogador = int(input('Qual o seu palpite? '))
    cont += 1
    if jogador == computador:
        acertou = True
    elif jogador < computador:
        print('Mais... tente mais uma vez.')
    elif jogador > computador:
        print('Menos... Tente mais uma vez.')
print('Acertou com {} tentativas. Parabens!'.format(cont))
