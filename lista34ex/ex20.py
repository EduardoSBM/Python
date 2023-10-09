# Leia a idade e o tempo de servic¸o de um trabalhador e escreva se ele pode ou nao se aposentar.
#As condições para aposentadoria são:
#• Ter pelo menos 65 anos,
#• Ou ter trabalhado pelo menos 30 anos,
#• Ou ter pelo menos 60 anos e trabalhado pelo menos 25 anos.

i = int(input(f"Digite sua idade: "))
tserviço = int(input(f"Digite o seu tempode serviço em anos: "))

if (i > 65):
    print(f"Você ja pode se aposentar")
else:
    print(f"Você não pode se aposentar")

if tserviço >= 30:
    print(f"Você pode se aposentar")
else:
    print(f"Você não pode se aposentar")

if i >= 60 and tserviço >= 25:
    print(f"Você ja pode se aposentar")
else:
    print(f"Você não pode se aposentar")