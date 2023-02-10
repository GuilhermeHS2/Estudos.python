nome = str(input('Qual e seu nome? '))
if nome == 'Guilherme':
    print('Que nome Bonito!')
elif nome == 'Pedro' or nome == 'Mario' or nome == 'Gabriel':
    print('Seu nome e bem popular no Brasil!')
else:
    print('Seu nome e bem normal')
print ('Tenha um Bom Dia {}'.format(nome))