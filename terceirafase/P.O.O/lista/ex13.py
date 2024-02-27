#Ler 3 valores (considere que não serão informados valores iguais) e escrever a soma dos 2 maiores.
#queria usar 
lista = []

v1 = float(input(f"Digite o valor 1: "))
v2 = float(input(f"Digite o valor 2: "))
v3 = float(input(f"Digite o valor 3: "))

if (v1 != v2) and (v1 != v3) and (v2 != v3):
    lista.append(v1)
    lista.append(v2)
    lista.append(v3)
    lista.sort()
    print(f"A soma dos maiores número é: {lista[1] + lista[2]} ")
