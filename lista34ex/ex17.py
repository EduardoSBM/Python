#) Fac¸a um programa que receba a altura e o sexo de uma pessoa e calcule e mostre seu peso ideal,
#utilizando as seguintes formulas (onde h corresponde à altura):
#• Homens: (72.7 ∗ h) − 58
#• Mulheres: (62, 1 ∗ h) − 44, 7

print("Olá, seja bem vindo ao seu exame de IMC!!")
h = float(input("Insira o valor de sua altura: "))
print("escolha o número seu sexo a seguir:\n 1- Masculino\n 2-Feminino")
sex = int(input("Digite o número do seu sexo aqui:"))

if sex == 1:
    print(f' seu peso ideal é: {(h * 72.7) - 58}')

if sex == 2:
    print(f' seu peso ideal é: {(h *62.1) - 44.7}')