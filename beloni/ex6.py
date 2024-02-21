#As maçãs custam R$ 1,30 cada se forem compradas menos de uma dúzia, e R$ 1,00 se forem compradas pelo menos 12. Escreva um programa que leia o número de maçãs compradas, calcule e escreva o custo total da compra.
maca = int(input("Digte o número de maçãs que você deseja comprar: "))

if (maca >= 12):
    print(f" Sua compra de {maca} maçãs, custa {maca * 1}")
else:
    print(f" Sua compra de {maca} maçãs, custa {maca * 1.30}")