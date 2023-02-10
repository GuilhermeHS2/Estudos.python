p = int(input('Primeiro termo: '))
r = int(input('razao de PA: '))
t = p
cont = 1
while cont <= 10:
    print('{} ->'.format(t),end='')
    t += r
    cont += 1


