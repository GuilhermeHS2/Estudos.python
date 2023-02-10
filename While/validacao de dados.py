'''sexo = str(input('Digite seu Sexo [M/F]: ')).upper().strip()[0]
while sexo != 'M' and sexo != 'F':
    sexo = str(input('Digite um sexo Valido! ')).upper().strip()[0]
print('Sexo {} registrado com sucesso!'.format(sexo))'''
sexo = str(input('Digite seu Sexo [M/F]: ')).upper().strip()[0]
while sexo not in 'MmFf':
    sexo = str(input('Digite um sexo Valido! ')).upper().strip()[0]
print('Sexo {} registrado com sucesso!'.format(sexo))


