contador_negativos = 0

for i in range(10):
    valor = float(input(f"Digite o {i+1}º valor: "))
    if valor < 0:
        contador_negativos += 1

print(f"Total de valores negativos: {contador_negativos}")