#Faça um programa que pergunte ao usuário se ele quer passar uma temperatura de Fahrenheit
#para Celsius ou de Celsius para Fahrenheit, e que, a partir da resposta do usuário, faça a devida
#conversão

temp = float(input('digite a tempertaura que deseja converter: '))

print(f'1-Fahrenheit para Celsius')
print(f'2-Celsius para Fahrenheit')
escolha = int(input("Digite o número da opção aqui:"))

if escolha == 1:
    print(f' a temperatura de Fahrenheit para Celsius é: {temp *(9/5) +32}')

if escolha == 2:
    print(f' a temperatura de Celsius para Fahrenheit é: {(temp * (9/5)) + 32 }')