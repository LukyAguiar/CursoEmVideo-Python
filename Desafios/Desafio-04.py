print("========== DESAFIO 04 ==========")

something = input("Digite algo:")
print('{} O tipo primitivo desse valor é'.format(something), type(something))
print("{} é númerico ou pode ser convertido? {}".format(something, something.isalnum()))
print("{} faz parte do Alfabeto? {}".format(something, something.isalpha()))
print("{} faz parta da tabela Ascii? {}".format(something, something.isascii()))
print("{} está totalmente maiusculo? {}".format(something, something.isupper()))
print("{} está totalmente em minusculo? {}".format(something, something.islower()))
print("{} está capitalizada? ? {}".format(something, something.istitle()))
print("{} é decimal? {}".format(something, something.isdecimal()))
print("{} apenas digitos? {}".format(something, something.isdigit()))
print("{} passa pelo Print? {}".format(something, something.isprintable()))
print("{} só tem espaços? {}".format(something, something.isspace()))
