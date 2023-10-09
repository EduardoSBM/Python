#24) Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e 
#continue pedindo até que o usuário informe um valor válido

repetido = 1

while repetido == 1:
    nota = float(input("Digite sua nota: "))

    if nota >= 0 and nota <= 10:
        repete = 0
        print("valor valido, continue!")

    else:
        repete = 1
        print("Erro, nota invalida!")