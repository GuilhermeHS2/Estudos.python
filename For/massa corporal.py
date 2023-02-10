peso = float(input('Qual o seu peso? (Kg)  '))
altura = float(input('Qual a sua altura? (m)  '))
imc = peso / (altura ** 2)
print('O IMC dessa pessoa e de {:.1f}'.format(imc))
if imc < 18.5:
    print('Abaixo do peso')
elif 18.5 <= imc < 24.9:
    print('Peso Normal')
elif 24.9 <= imc < 29.9:
    print('Acima do peso')
elif  29.9 <= imc < 34.9:
    print('Obesidade I')
elif  34.9 <= imc < 39.9:
    print('Obesidade II')
else:
    print('Obesidade III')