#Construir um programa que leia nome e valor em dinheiro (reais) de uma pessoa. Calcule e retorne uma
#mensagem com o valor convertido para Dólar e calcule e retorne uma mensagem com o valor convertido para
#Euros.

print("Olá, seja bem vindo!!")
x = float(input("Insira o valor desejado para conversão em doláres e euros: "))

print(f'O valor que você pode comprar em dolares é de: {x // 5.41} e em euros é de: {x // 5.43}')