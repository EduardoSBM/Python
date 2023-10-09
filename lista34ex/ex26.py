#Faça um programa que leia e valide as seguintes informações:
#a. Nome: maior que 3 caracteres;
#b. Idade: entre 0 e 150;
#c. Salário: maior que zero;
#d. Sexo: 'f' ou 'm';
#e. Estado Civil: 's', 'c', 'v', 'd';
#Use a função len(string) para saber o tamanho de um texto (número de caracteres).



nome = input('Digite seu nome: ')
cash = float(input('Digite seu salario: '))
sexo = input('Digite seu sexo: m / f ')
estciv = input('Digite seu estado civil: s / c / v / d ')

if len(nome) < 3:
    print('O nome obtem menos de 3 caracteres')
else:
    print('O nome obtem mais de 3 caracteres')
if cash > 0:
    print('O salario é maior que 0')
else:
    print('O salario é menor ou igual a 0')

if sexo == 'm' or sexo == 'f':
    if sexo == 'm':
        print('O sexo é masculino')
    else:
        print('O sexo é feminino')
else:
    print('O sexo informado não existe :)')

if estciv == 's' or estciv == 'c' or estciv == 'v' or estciv == 'd':
    if estciv == 's':
        print('O estado civil é de  solteiro')
    if estciv == 'c':
        print('O estado civil é de casado')
    if estciv == 'v':
        print('O estado civil é viuvo')
    if estciv == 'd':
        print('O estado civil é de divorciado')
else:
    print('Erro!')