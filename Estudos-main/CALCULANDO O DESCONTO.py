vlr = float(input('Digite o valor do produto R$'))
desc = vlr - (vlr * 5 / 100)
print('O produto que custava R${:.2f}, na promocao com desconto de 5% vai custar R${:.2f}'.format(vlr,desc))