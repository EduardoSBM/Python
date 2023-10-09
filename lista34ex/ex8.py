#Faça um programa que leia a largura e a altura de uma parede em metros, e calcule a sua área e a
#quantidade da tinta necessária para pinta-la, sabendo que cada litro de tinta, pinta uma área de 2m².

print(f'digite os valores a seguir para determinar a área da parede!')
h = int(input("Digite a altura da parede em metros: "))
l = int(input("Digite a largura da parede em metros: "))

print(f'A quantidade de tinta necessária sera de: {(h * l) // 2} litros')