n1 = float(input('Digite a sua nota: '))
n2 = float(input('Digite a sua segunda nota: '))
m = (n1 + n2)/2
if m >=6.0:
     print('Voce passou de serie')
else:
    print('Voce nao passou de serie')
print('A sua media foi {:.1f}'.format(m))