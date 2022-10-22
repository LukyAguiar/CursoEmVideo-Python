preco = float(input("Digite o preço do produto: "))
desconto = ((preco / 100) * 5)
print("O novo preço do produto vai de {} para {} com 5% de desconto ".format(preco, preco - desconto))
