litros = int(input("Digite total de litros vendidos: "))

op = input("Escolha combustivel:\n"
               "A-álcool\n"
               "G-gasolina\n"
               "")
if(op == "A"):
    valor = litros * 2.90
    print(f"Litros: {litros}, Combustivel: Alcool, Preço p/ litro: 2.90, total: {valor}")
elif(op == "G"):
    valor = litros * 3.30
    print(f"Litros: {litros}, Combustivel: Gasolina, Preço p/ litro: 3.30, total: {valor}")