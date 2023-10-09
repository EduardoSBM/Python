#Escreva um Programa que verifique se um elemento está na lista e verifique a posição exata dele da lista

lista = ['1','2','3','4','5','6','7','8']

x = input('digite o que você quer procurar na lista:')

if x in lista:
    print(f'Já está na lista{lista}') 

else:
    lista.append(x)
    print(f'{lista}')  