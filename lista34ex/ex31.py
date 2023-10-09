#Faça um programa que jogue par ou impar com o computador. O jogo será interrompido quando o jogador 
#perder. Mostre ao final, o total de vitórias consecutivas que o jogador conquistou no jogo.


import random
a = int(input(": "))
b = int(random.randint(-100, 100))
c = a+b

if (c%2) == 0:
    print(c)
    print("par")
else:
    print(c)
    print("impar")