'''frase = str(input('Digite uma frase: ')).strip().upper()
pal = frase.split()
junto = ''.join(pal)
inverso = ''
for letra in range(len(junto) - 1, -1 , -1):
    inverso += junto[letra]
print('O inverso de {} e {}'.format(junto, inverso))
if inverso == junto:
    print('Temos um palindromo!')
else:
    print('A frase digitada nao e um palindromo!')'''
frase = str(input('Digite uma frase: ')).strip().upper()
pal = frase.split()
junto = ''.join(pal)
inverso = junto [::-1]
print('O inverso de {} e {}'.format(junto, inverso))
if inverso == junto:
    print('Temos um palindromo!')
else:
    print('A frase digitada nao e um palindromo!')