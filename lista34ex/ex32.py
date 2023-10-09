#Foi feita uma estatística em cinco cidades brasileiras para coletar dados sobre acidentes de trânsito. Foram
#obtidos os seguintes dados:
#a. Código da cidade; (digitado pelo usuário)
#b. Número de veículos de passeio (em 1999); (digitado pelo usuário)
#c. Número de acidentes de trânsito com vítimas (em 1999). (digitado pelo usuário)
#Deseja-se saber:
#b. Qual o maior e menor índice de acidentes de transito e a que cidade pertence;
#c. Qual a média de veículos nas cinco cidades juntas;
#d. Qual a média de acidentes de trânsito nas cidades com menos de 2.000 veículos de passeio """

maior = 0
menor = 999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999


cd2 = []
mediatotal = []
i2 = []



for i in range(5):
    cod = int(input('digite o codigo da cidade: '))
    cd2.append(cod)
    vei = int(input('Digite quantos veiculos de passeio: '))
    aci = int(input('Digite o numero de acidentes: '))
    ind = vei/aci
    i2.append(ind)
    if ind < menor:
        menor = ind
        menorcidade = cod
    if ind > maior:
        maior = ind
        maiorcidade = cod
    if vei < 2000:
        mediatotal.append(aci)
m = sum(i2)/len(i2)
print(f'O maior índice de acidentes é {maiorcidade} sendo {maior}')
print(f'O menor índice de acidentes é da cidade {menorcidade} sendo {menor}')
print(f'A média dos índices das cinco cidades é {m}')
if len(mediatotal) > 0:
    twok = sum(mediatotal)/len(mediatotal)
    print(f'a média de acidentes com menos de 2000 carros é {twok}')