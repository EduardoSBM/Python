#Faca um algoritmo que calcule a media das notas de 3 provas. A primeira e a segunda prova tem 
#peso 5 e a terceira tem peso 10. Ao final, mostrar a média do aluno e indicar se o aluno foi 
#aprovado ou reprovado. A nota para aprovação deve ser igual ou superior a 6.0 pontos.


nota1 = float(input("Digite a nota de sua prova peso 10:"))
nota2 = float(input("Digite a nota de sua prova peso 5:"))
nota3 = float(input("Digite a sua outra nota peso 5:"))

if ( nota2 > 5 or nota2 < 0):
    print(f'error')
elif ( nota3 > 5 or nota3 < 0):
    print(f'error')
else:
    nota4 = nota2 + nota3 


final = (nota1 + nota4)/2    

print(f'A média final do aluno é de:{final}')

if (final >= 6):
    print(f'O aluno passou com média: {final}')
else:
    print(f'O aluno reprovou com média: {final}')