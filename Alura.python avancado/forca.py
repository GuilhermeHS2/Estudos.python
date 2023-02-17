import random





def jogar():

    boas_vindas()
    palavra_secreta = arquivo_com_txt_da_palavra_cruzada()

    letrasac = inicia_letras_AC(palavra_secreta)

    #outra maneira de colocar os _ na palavra secreta
    '''for letras in palavra_secreta:
        letrasac.append('_')'''

    print(letrasac)
    enforco = False
    acertou = False
    erro = 0




    while not enforco and not acertou:
        chute = str(input('Qual letra? ')).strip().upper()[0]
        if chute in palavra_secreta:
            poze = 0
            for letra in palavra_secreta.upper():
                if chute == letra.upper():
                    letrasac [poze] = letra
                poze+=1

        else:
            erro+=1
        enforco = erro ==6
        acertou = '_' not in letrasac
        print(f'{letrasac}')

    if acertou:
        print('Voce ganhou!')
    else:
        print('Voce perdeu!')
    print("Fim do jogo")


def boas_vindas():
    print('Bem vindo ao jogo de forca')


def inicia_letras_AC(palavra):
  return ['_' for letras in palavra]

def arquivo_com_txt_da_palavra_cruzada():
    arquivo = open('palavras.txt', 'r')
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()

    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()
    return palavra_secreta


if(__name__ == "__main__"):
    jogar()
