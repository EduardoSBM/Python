# Faça 4 listas:
#A. Filmes
#B. Jogos
#C. Livros
#D. Esporte
#a. Adicione no mínimo 2 itens em cada lista.
#b. Crie uma lista das 4 listas criadas acima.
#c. Acesse (mostrar) algum item da lista livros.
#d. Remova um item da lista esporte.


#a
a = [ 'velozes e furiosos', 'barbie' ]
b = [ 'gta', 'free fire']
c = [ 'diário de um banana', 'Deus esta morto']
d = [ 'futebol' , 'handbol']

#b
e = a + b + c + d
print(e)

#c
print(c[0])
print(c)

#d
print(d)
del d[1]
print(d)