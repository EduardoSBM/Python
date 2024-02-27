t = int(input(f"Digite o numero de votos do municipio: "))
v = int(input(f"Digite o numero de votos validos: "))
b = int(input(f"Digite o numero de votos brancos: "))
n = int(input(f"Digite o numero de votos nulos: "))
tf = v + b + n

if ( t < tf):
    print(f"Erro, lembre-se que ao digitar não pode-se obter um número maior que numero de votos do múnicópio {t} ")
else:
    print(f" o percentual de votos validos foi {(t/100) * v }%")
    print(f" o percentual de votos brancos foi {(t/100) * b }%")
    print(f" o percentual de votos nulos foi {(t/100) * n }%")
