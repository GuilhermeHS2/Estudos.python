def jogar():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")
    palavra_secreta = 'Guilherme'
    enforco = False
    acertou = False


    while not enforco and not acertou:
        chute = str(input('Qual letra? ')).strip().upper()[0]
        index = 0
        for letra in palavra_secreta.upper():
            if chute == letra.upper():
                print(f'Encontrei a letra {letra} na posicao {index}')
            index+=1
        print('Jogando...')










    print("Fim do jogo")

if(__name__ == "__main__"):
    jogar()
