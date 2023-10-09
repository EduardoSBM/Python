#Crie um programa que leia dois valores e mostre na tela um menu :
#a. Somar
#b. Multiplicar
#c. Maior
#d. Menor
#e. Sair do programa

while True:

    a = int(input("Insira o primeiro valor:"))
    b = int(input("Insira o segundo valor:"))

    print(f'Escolha uma das opções a seguir:')

    print(f'1- Somar'        )
    print(f'2- Multiplicar')
    print(f'3- Maior'  )
    print(f'4- Menor'  )
    print(f'5- encerrar'  )
    escolha = int(input('Digite o número de sua escolha a seguir: '))

    if (escolha == 1):
        print(f'A soma dos valores é: {a+b}')

    elif (escolha == 2):
        print(f'A multiplicação entre os números é de: {a*b}')   

    elif (escolha == 3):
        if (a>b):
            print(f' O maior valor é {a}')

        elif (b>a):
            print(f' O maior valor é {b}')

        else:
            print(f'Os valores são iguais!')        

    elif (escolha == 4):
        if (a>b):
            print(f' O menor valor é {b}')

        elif (b>a):
            print(f' O menor valor é {a}')

        else:
            print(f'Os valores são iguais!') 

    elif ( escolha == 5):
        print(f'Você desejou encerrar.')
        break;   

    else:
        print(f'erro!')