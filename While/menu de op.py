'''certo = False
num = int(input('Primeiro valor: '))
nun = int(input('Segundo valor: '))
op = 5
print(Escolha sua opcao:
[1] Somar
[2] Multiplicar
[3] Maior
[4] Novos numeros
[5] Sair do programa)
while not certo:
    op = int(input('Qual e a sua opcao? '))
    if op == 1:
        soma = num + nun
        print('A soma {} e {} e igual a {}'.format(num, nun, soma))
    elif op == 2:
        soma = num * nun
        print('A multiplicacao {} e {} e igual {}'.format(num, nun, soma))
    elif op == 3:
            if num > nun:
                print('O maior numero e {}'.format(num))
            else:
                print('O mairo numero e {}'.format(nun))
    elif op == 4:
        certo = False
    elif op ==5:
        certo = True
    else:
        print('Digite uma opaco valida')
print('Programa finalizado')'''
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
op = 0
while op != 5:
    print('''Escolha sua opcao:
    [1] Somar
    [2] Multiplicar
    [3] Maior
    [4] Novos numeros
    [5] Sair do programa''')
    op = int(input('Qual sua opcao? '))
    if op == 1:
            soma = n1 + n2
    print('A soma entre {} e {} e {}'.format(n1,n2,soma))
    elif op == 2:
        soma = n1 * n2
    print('A soma entre {} e {} e {}'.format(n1, n2, soma))
    elif op == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('Entre {} e {} o maior valor e {}'.format(n1,n2,maior))
    elif op == 4:
        print('Informe os numeros novamente: ')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))

    elif op == 5:

        print('Finalizando')
    else:
            print('Opcao invalida')



