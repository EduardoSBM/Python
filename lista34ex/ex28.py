# Numa eleição existem três candidatos. Faça um programa que peça o número total de eleitores. Peça para
#cada eleitor votar e ao final mostrar o número de votos de cada candidato.

nunes = 0
luan = 0
matheus = 0
x = int(input('Digite o numero total de eleitores: '))
i = 1
while i < x:
    voto = int(input(f'Voto {i}\n'
                     '1 - nunes 1\n'
                     '2 - luan 2\n'
                     '3 - matheus 3\n'))
    if voto == 1:
        nunes = nunes + 1
    elif voto == 2:
        luan = luan + 1
    elif voto == 3:
        matheus = matheus + 1
    else:
        print('Voto nulo')
    i =i+1
print(f'total do candidato nunes: {nunes}')
print(f'total do candidato luan: {luan}')
print(f'total do candidato matheus: {matheus}')