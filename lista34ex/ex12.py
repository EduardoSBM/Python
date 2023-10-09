#Escreve um Programa que leia uma lista com no minino 5 itens, contendo itens repetidos e mostre
#os itens repetidos. 

lista = [1, 'veloz', 'furioso', 4, 5, 'veloz', 'furioso']
repetidos = []

for i in lista: 
    if i not in repetidos:
        repetidos.append(i)
    else:
        repetidos.append(i) 
        print(i)