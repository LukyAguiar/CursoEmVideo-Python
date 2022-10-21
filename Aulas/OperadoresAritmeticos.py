#Soma
print("==== SOMA ====")
n1 = int(input("Digite um valor para N1: "))
n2 = int(input("Digite um valor para N2: "))
result = n1 + n2;
print('O Resultado da Soma entre {} e {} é igual a {}'.format(n1, n2, result))
print()

#Subtração
print("==== SUBTRAÇÃO ====")
result = n1 - n2;
print('O Resultado da Soma entre {} e {} é igual a {}'.format(n1, n2, result))
print()

#Multiplicação
print("==== MULTIPLICAÇÃO ====")
result = n1 * n2;
print('O Resultado da Mutiplicação entre {} e {} é igual a {}'.format(n1, n2, result))
print()

#Divisão
print("==== DIVISÃO ====")
result = n1 / n2;
print('O Resultado da Divisão entre {} e {} é igual a {:.3f}'.format(n1, n2, result))
print()

#Potencia
print("==== POTÊNCIA ====")
result = n1 ** n2;
print('O Resultado da Potência entre {} e {} é igual a {}'.format(n1, n2, result))
print()

#Divsão Inteira
print("==== DIVISÃO INTEIRA ====")
result = n1 // n2;
print('O Resultado da Divisão Inteira entre {} e {} é igual a {}'.format(n1, n2, result))
print()

#Porcentagem
print("==== PORCENTAGEM ====")
result = n1 % n2;
print('O Resultado da Porcentagem entre {} e {} é igual a {}'.format(n1, n2, result))
print()

#Raiz Quadrada
print("==== RAIZ QUADRADA ====")
result = n1**(1/2)
print('O Resultado da Raiz Quadrada de {} é igual a {:.3f}'.format(n1, result))

print("ORDEM DE PRECEDÊNCIA")
print("()")
print("**")
print("Multiplicação")
print("Divisão")
print("Divisão Inteira")
print("Porcentagem")
print("adição")
print("subtração")

#Possibilidades
nome = input('Qual é seu nome: ')
print('Prazer em te conhecer {:20}'.format(nome)) #Em 20 espaços
print('Prazer em te conhecer {:>20}'.format(nome)) #Em 20 espaços
print('Prazer em te conhecer {:<20}'.format(nome)) #Em 20 espaços
print('Prazer em te conhecer {:^20}'.format(nome)) #Em 20 espaços
print('Prazer em te conhecer {:=^20}'.format(nome)) #Em 20 espaços

# ' end = '' ' faz a linha ir até o final
# ' \n '  quebra de linha