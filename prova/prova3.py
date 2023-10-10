lista = [["artur", "123", "@gmail"], ["joao", "321", "@gay"]]

def cadastrar(): # criando a função
    nome = input("nome: ")
    telefone = input("telefone")
    email = input("email: ")
    lista.append([nome, telefone, email]) #adicionando com append a ultima posição uma lista com nome, telefone e email

def mostrar():
    print(lista) #[["artur", "123", "@gmail"], ["joao", "321", "@gay"]]
    print(lista[0]) #["artur", "123", "@gmail"]
    print(lista[0][0]) #artur
    lista[0][0] = "jonas" # altera o valor [0][0]
    print(lista[0]) #["jonas", "123", "@gmail"]

def editar():
    for i in range(len(lista)):
        print(i, lista[i])
    ls = int(input("lista a ser editada: "))
    print(lista[ls]) #printa a lista selecionada
    op = int(input("valor a ser editado: (0-nome/1-telefone/2-email) ")) #escolha valor pelo indice
    valor = input(": ") #recebe oque tu vai colocar nesse indice
    lista[ls][op] = valor #muda o valor

while True:
    print("1 = cadastrar")
    print("2 = mostrar")
    print("3 = editar")
    op = int(input("op = :"))

    if op == 1:
        cadastrar() #chamando a função
    if op == 2:
        mostrar()
    if op == 3:
        editar()