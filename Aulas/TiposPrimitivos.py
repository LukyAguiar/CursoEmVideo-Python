#Praticas

## type trás o tipo da variável
n1 = input('Digite um valo: ')
print(type(n1));

#----------
# Utilizando format -
n1 = int(input('Digite um valor para N1: '))
n2 = int(input('Digite um valor para N2: '))
result = n2 + n1
print('O resultado da soma de {} + {} é {} '.format(n1, n2, result))

#----------
# Praticando tipagem na entrada de dados
a = bool(input('Digite um valor: '))  #bool - Booleano - Condicional - True, False
b = str(input('Digite um valor: '))  #Str - 'Olá', '7,5', ''
c = int(input('Digite um valor: ')) #int - Inteiro = 7, -4, 0, 9875
d = float(input('Digite um valor: ')) #float - Decimais = 4.5, 0.076, -15.223, 7.0
print(a)
print(type(b))
print(c)
print(d)

# Validando com is
t = input('Digite algo:')
print(t.isnumeric()) #Verifica se ele é número ou se existe a possibilidade de conversão
print(t.isalpha()) #Verficia se ele é alphabetico
print(t.isalnum()) #Verifica se ele faz parte do alfabeto numerico
print(t.isupper()) #Verifica se ele está totalmente em letra maiscula
