#Faça um programa que pergunte a temperatura atual para o usuário e mostre uma mensagem na
#tela dizendo se está “quente”, “frio” ou “agradável”.

temp = float(input('Digite a temperatura: '))

if ( 23 <= temp <= 26):
    print(f'tempertura agradavel!')

elif ( temp > 26 ):
    print(f'tempertura quente!')

else:
    print(f'tempertura fria!')  