#Ler o salário fixo e o valor das vendas efetuadas pelo vendedor de uma empresa. Sabendo-se que ele recebe uma comissão de 3% sobre o total das vendas até R$ 1.500,00 mais 5% sobre o que ultrapassar este valor, calcular e escrever o seu salário total.

fx = float(input(f"Digite o seu salário fixo: "))
vd = float(input(f"Digite o valor de vendas: "))

if (vd > 1500):
    vdf = vd - 1500
    vdp = vdf/ 100
    nvsalario = fx + 45 + vdp*5
    print(f"Seu novo salário é de: {nvsalario}")