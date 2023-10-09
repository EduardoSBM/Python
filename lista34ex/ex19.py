#Escreva o menu de opções abaixo. Leia a opção do usuario e execute a operação escolhida. 
#Escreva uma mensagem de erro se a opção for inválida. Escolha a opção: 
#a. Soma de 2 n´umeros. 
#b. Diferença entre 2 números (maior pelo menor). 
#c.Produto entre 2 números. 
#d. Divisão entre 2 números (o denominador não pode ser zero).

a = int(input('Olá, digite o primeiro número:' ))
b = int(input('Olá, digite o segundo número:' ))

print(f'Escolha uma das opções a seguir:')

print(f'1- Soma de 2 números'        )
print(f'2- Diferença entre 2 números')
print(f'3- Produto entre 2 números'  )
print(f'4- Divisão entre 2 números'  )
escolha = int(input('Digite o número de sua escolha a seguir: '))

if (escolha == 1):
    print(f'A soma dos valores é: {a+b}')
elif (escolha == 2):
    print(f'A diferença dos número é de: {a-b}')   
elif (escolha == 3):
    print(f'O produto entre os números é de: {a*b}')
elif (escolha == 4):
    if ( b == 0):
        print(f'erro')
    else:    
        print(f'A divisão entre os dois números é de: {a/b}') 
else:
    print(f'erro')           