print('{:=^40}'.format('LOJA TIO STITCH '))
compra = float(input('Preco das compras: R$'))
print('''Escolha sua forma de pagamento:
[1] a vista dinheiro/cheque
[2] a vista no cartao
[3] 2x no cartao
[4] 3x ou mais no cartao''')
paga = int(input('Qual e a opcao? '))
if paga == 1:
    desc =  compra -  (compra * 10 / 100)
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final'.format(compra, desc))
elif paga == 2:
    desc = compra - (compra * 5 / 100)
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final'.format(compra, desc))
elif paga == 3:
    parcela = compra / 2
    print('Sua compra sera parcelado em 2x de R${:.2f}'.format(parcela))
elif paga == 4:
    juros = compra + (compra * 20 / 100)
    par = int(input('Quantas parcelas? '))
    parcela = juros / par
    print('Sua compra sera parcelada em {} de R${:.2f} COM JUROS ''Sua compra de R${:.2f} vai custar R${:.2f} no final'.format(par,parcela,compra,juros))
else:
    print('Escolha uma opcao valida')

