print('Digite 0 para termina o programa')
p = int(input('Primeiro termo: '))
r = int(input('razao de PA: '))
t = p
cont = 1
mais = 10
total = 0
while mais != 0:
    total = total + mais
    while cont <= total:
        print('{} ->'.format(t),end='')
        t += r
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos voce quer mostrar a mais? '))
print('Progressao finalizada com {} termos mostrados.'.format(total))
