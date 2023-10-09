#Faça um programa que receba como entrada os dados de um funcionário: nome, numero de horas
#trabalhadas, valor da hora trabalhada. Após calcule seu salário bruto. Calcule um desconto de 2% de INSS. E
#ao final mostrar seu nome e salário final calculado.

nome = input('Olá, digite seu nome:')

hr = int(input('Digite o valor de horas que você trabalha no mês:'))
phr = int(input('Digite o valor que você ganha por hora: '))

salbr = phr * hr

print(f'{nome}, seu salário com desconto do INSS é de: {salbr - salbr * 0.02}')