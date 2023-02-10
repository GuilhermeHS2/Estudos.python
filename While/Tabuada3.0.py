while True:
    print('Digite 0 para terminar')
    n = int(input('Digite um numero para calcular a tabuada: '))
    print('-'*30)
    if n <= 0:
        break
    for c in range(1,11):
        print(f'{n} x {c} = {n*c}')
    print('-'*30)
print('PROGRAMA DE TABUADA ENCERRADO. Volte sempre!')