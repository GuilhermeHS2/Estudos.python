larg = float(input('Largura da parede: '))
alt = float(input('Altura da parede: '))
area = larg * alt
print('Sua parede tem a dimensao de {}x{} e sua area e de {}m.'.format(larg,alt,area))
tinta = area / 2
print('Para pintar essa parede, voce precisara de {}L de tinras.'.format(tinta))