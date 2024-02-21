#) Ler um valor e escrever se é positivo, negativo ou zero.
v = float(input(f"Digite um valor: "))

if (v == 0):
    print("O valor é zero")
elif (v > 0):
    print("O valor é positivo")
else:
    print("O valor é negativo")