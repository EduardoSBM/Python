intervalo= 0
fora = 0

for i in range(10):
    valor = float(input(f"Digite o {i+1}º valor: "))
    if (valor >= 10 & valor <= 20):
        intervalo += 1
    else:
        fora = 0

print(f"Total de valores no intervalo de 10 a 20: {intervalo}, total de valores fora do intervalo: {fora}")