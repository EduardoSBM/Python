#Faça um programa que leia algo pelo teclado e mostre na tela seu tipo de dado e todas as informações sobre
#ele.

x = input("Digite algo:")


print(type(x))
print(x.isnumeric()) #verifica se é numérico
print(x.isalpha()) #verifica se é letra
print(x.isspace()) #se é só espaço
print(x.isalnum()) # se é alpha numerico por exemplo 
print(x.isupper()) # se esta em letras minuscula
print(x.istitle()) # palavra capitalizada por exemplo, Python