print("======== DESAFIO 11 ========")
largura = float(input('Digite a largura da sua parede em metros: '));
altura = float(input('Digite quanto de altura tem sua parede em metros: '));
area = largura * altura
print('Sua parede tem a dimensão de {}x{} e sua área é de {}m.'.format(largura, altura, area))
tinta = area / 2
print('Para pintar essa parede, você precisará de {}l de tinta.'.format(tinta))