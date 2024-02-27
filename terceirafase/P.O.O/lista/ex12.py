#Ler 3 valores (considere que não serão informados valores iguais) e escrevê-los em ordem crescente.
lista = []

v1 = float(input(f"Digite o valor 1: "))
v2 = float(input(f"Digite o valor 2: "))
v3 = float(input(f"Digite o valor 3: "))

if (v1 != v2) and (v1 != v3) and (v2 != v3):
    lista.append(v1)
    lista.append(v2)
    lista.append(v3)
    lista.sort()
    print(lista)
else:
    print("Não informe valores repetidos")