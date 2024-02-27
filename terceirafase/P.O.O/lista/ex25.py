hve = 0
hn = 99999
mve = 0
mn = 99999
y=0
x=0
for i in range (2):
    x +=1
    homem = int(input(f"Digite a idade do homem {x}: "))
    if homem > hve:
        hve = homem
    if homem < hn:
        hn = homem
for i in range (2):
    y +=1
    mulher = int(input(f"Digite a idade da mulher {y}: "))
    if mulher > mve:
        mve = mulher
    if mulher < mn:
        mn = mulher
print(f'Soma do homem mais novo com a mulher mais velha: {hn + mve}')
print(f'Soma do homem mais velho com a mulher mais nova: {hve + mn}')
