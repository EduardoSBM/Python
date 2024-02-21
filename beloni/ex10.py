#Faça um algoritmo para ler: número da conta do cliente, saldo, débito e crédito. Após, calcular e escrever o saldo atual (saldo atual = saldo - débito + crédito). Também testar se saldo atual for maior ou igual a zero escrever a mensagem 'Saldo Positivo', senão escrever a mensagem 'Saldo Negativo'.
conta = int(input("Digite o número de sua conta:")) 
saldo = float(input("Digite o saldo de sua conta:")) 
débito = float(input("Digite o débito a pagar de de sua conta:")) 
crédito = float(input("Digite o crédito de sua conta:"))

saldonv = saldo - débito + crédito

if (saldonv >= 0):
    print("Saldo positivo!")
else:
    print("Saldo negativo!")