dis = float(input('Qual e a distancia da sua viagem? '))
print('Voce esta prestes a comecar um viagem de {}Km'.format(dis))
if dis <=200:
    valo = dis * 0.50
else:
    valo = dis * 0.45
print('E o preco da sua passagem sera de R${:.2f}'.format(valo))