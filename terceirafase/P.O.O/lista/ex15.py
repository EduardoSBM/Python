c=2
x=0
valor = []

for i in range (c):
    x +=1
    v = int(input(f"Digite o valor {x}: "))
    valor.append(v)
    while v == 0:
        valor.remove(0)
        v = int(input(f"Digite o valor {x}: "))
        valor.append(v)
print(f'A divisão de {valor[0]} por {valor[1]} é {valor[0]/valor[1]}')