#O custo de um carro novo ao consumidor é a soma do custo de fábrica com a porcentagem do distribuidor e dos impostos (aplicados ao custo de fábrica). Supondo que o percentual do distribuidor seja de 28% e os impostos de 45%, escrever um algoritmo para ler o custo de fábrica de um carro, calcular e escrever o custo final ao consumidor.

fa = float(input(f"digite preço de fabrica do carro: "))
fap = fa/100
dis = fap*28
imp = fap*45
car = fa + dis + imp
print(f"O valor final do carro é de {car}")