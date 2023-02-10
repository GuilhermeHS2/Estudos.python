from random import randint
print('-'*35)
print('Bem vindo ao jogo de Adivinhação!')
print('-'*35)
numsecreto = randint(1,101)
tentativas = nivel = pontosper = 0
pontos = 1000
para = False
print('Qual NV de dificuldade?\n'
      '[1] Facil\n'
      '[2] Medio\n'
      '[3] Dificil')
while True:
    nivel =int(input('Defina um nivel: '))
    if nivel == 1:
        tentativas+=20
    elif nivel == 2:
        tentativas+=10
    elif nivel == 3:
        tentativas+=5
    else:
        print('Digite um numero valido')
    for rodada in range (1, tentativas +1):
        print(f'tentativas {rodada} de {tentativas}')

        chute = int(input('Digite um numero de 1 a 100: '))
        print(f'Voce digitou {chute}')
        if chute > 100 or chute < 1:
            print('Voce deve digitar um numero entre 1 a 100')
            continue
        elif chute == numsecreto:
            print('Voce acertou parabens')
            break
        elif tentativas == 0:
            break


        else:
            if chute > numsecreto:
                print('Você errou! O seu chute foi MAIOR do que o número secreto. ')
            elif chute < numsecreto:
                print('Você errou! O seu chute foi MENOR do que o número secreto.')
        pontosper = numsecreto - chute
        pontos = pontos - pontosper
        print('Fim do jogo\n '
            f'Voce fez um total de {pontos} pontos')


    print(f'Voce fez {pontos}')
