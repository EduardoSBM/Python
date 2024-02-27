lista = []

for i in range(8):
    valor = float(input(f"Digite o {i+1}º valor: "))
    if (valor < 40):
        lista.append(valor)

print(f"lista: {lista}, valores somados: {sum(lista)}")