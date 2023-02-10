sla = float(input('Qual e o salario do funcionario: '))
if sla <= 1250:
 n =  sla + (sla * 15 / 100)
else:
    n = sla + (sla * 10 / 100)
print('Quem ganhava R${:.2F} passa a ganhar R${:.2f} agora'.format(sla, n))
