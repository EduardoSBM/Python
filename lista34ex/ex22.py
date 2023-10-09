#Crie um programa que leia vários números inteiros pelo teclado. O programa só pode para quando for 
#digitado o numero 1000. No final, mostre quantos números foram digitados e qual foi a soma deles. 
#Desconsiderando o valor 1000 da parada

i = []
while True:
    a = int(input('Digite um valor:' ))
    if a == 1000:
        print(sum(i))
        break
    i.append(a)