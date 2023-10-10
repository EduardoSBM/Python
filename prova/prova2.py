# Dobrar todos os elementos de uma lista
lista = [1, 2, 3, 4, 5]
dobro = list(map(lambda x: x * 2, lista))
filtro = list(filter(lambda lista: lista > 1 and lista < 3, lista))
print(filtro)
print(dobro) # Output: [2, 4, 6, 8, 10]