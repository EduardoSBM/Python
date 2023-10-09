#Crie um programa que leia vários números inteiros pelo teclado. No final, mostre a média entre todos os 
#valores lidos e qual foi o maior e o menor valor lido. O programa deve perguntar ao usuário se ele quer ou 
#não continuar a escrever valores

lista = []
contador = 0
while True:
    op = input("desligar (s/n) : ")
    contador +=1
    if op == "s":
        print(max(lista))
        print(min(lista))
        break
    a = int(input(": "))
    lista.append(a)