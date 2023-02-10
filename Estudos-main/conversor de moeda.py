n1 = float(input('Quanto dinheiro voce tem na carteira? R$'))
n2 = n1 / 5.06
n3 = n1 / 5.05
print('Com R${:.2f} voce pode compar US${:.2f}'.format(n1,n2))
print('Com R${:2.f} voce pode comprar €${:.2f}'.format(n1,n3))
