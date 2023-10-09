#Em uma eleição presidencial existem quatro candidatos. Os votos são informados por meio de código. Os
#códigos utilizados são:

""" a. O total de votos para cada candidato;
b. O total de votos nulos;
c. O total de votos em branco;
d. A percentagem de votos nulos sobre o total de votos;
e. A percentagem de votos em branco sobre o total de votos. Para finalizar o conjunto de votos tem-se o
valor zero. """
from pickle import TRUE


neves = 0
nunes = 0
luan = 0
ruan = 0
branco = 0
nulo = 0
print(f'bem vindo as eleições!')

while TRUE :
    print(f'1 - neves'   )
    print(f'2 - nunes'   )
    print(f'3 - luan'    )
    print(f'4 - ruan'    )
    print(f'5 - branco'  )
    print(f'6 - nulo'    )
    print(f'7 - encerrar')
    opcao = int(input("Digite sua escolha:"))

    if (opcao == 1):
        neves = neves + 1

    if (opcao == 2):
        nunes = nunes + 1

    if (opcao == 3):
        luan = luan + 1

    if (opcao == 4):
            ruan = ruan + 1

    if (opcao == 5):
        branco = branco + 1

    if (opcao == 6):
        nulo = nulo + 1

    if (opcao == 7):
        break;

print(f'A quantidade de votos do candidato neves é: {neves}')
print(f'A quantidade de votos do candidato nunes é: {nunes}')
print(f'A quantidade de votos do candidato luan é: {luan}')
print(f'A quantidade de votos do candidato ruan é: {ruan}')
print(f'A quantidade de votos brancos é: {branco}')
print(f'A quantidade de votos nulos é: {nulo}')