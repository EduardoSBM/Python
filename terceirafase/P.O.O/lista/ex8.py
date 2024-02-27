#Ler o ano atual e o ano de nascimento de uma pessoa. Escrever uma mensagem que diga se ela poderá ou não votar este ano (não é necessário considerar o mês em que a pessoa nasceu).

nv = int(input("Digite o ano atual: "))
id = int(input("Digite o ano em que você nasceu"))

vt = nv - id

if (vt >= 16):
    print(f"Você pode votar este ano!")
else:
    print(f"Você não pode votar este ano!")