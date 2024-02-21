#Ler as notas da 1a. e 2a. avaliações de um aluno. Calcular a média aritmética simples e escrever uma mensagem que diga se o aluno foi ou não aprovado (considerar que nota igual ou maior que 6 o aluno é aprovado). Escrever também a média calculada.

n1 = float(input(f"Digita a nota 1: "))
n2 = float(input(f"Digita a nota 2: "))

media = (n1 + n2) / 2

if (media >= 6 ):
    print(f"Parabéns, você foi aprovado! Sua média foi {media}")
else:
    print(f"infelizmente, você foi reprovado! Sua média foi {media}") 