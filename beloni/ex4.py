temp = float(input('digite o valor tempertaura que deseja converter e após escolha o tipo de conversão: '))

print(f'1-Fahrenheit para Celsius')
print(f'2-Celsius para Fahrenheit')
escolha = int(input("Digite o número da opção aqui:"))

if escolha == 1:
    print(f' a temperatura de Fahrenheit para Celsius é: {temp *(9/5) +32}')

if escolha == 2:
    print(f' a temperatura de Celsius para Fahrenheit é: {(temp * (9/5)) + 32 }')