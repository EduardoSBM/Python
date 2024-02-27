# class nada mais é que um modelo para a criação de objeto que podem ser manipulados dentro dela!
class Pessoa:
    pass #deixa a class vazia!porém permite o código "funcionar"

class Aluno:
    nome = "Eduardo"
    idade = 17
    sexo = "masculino" # class comum com uma função def para puxar pelo objeto (falar)

    def falar(self, mensagem):
        print(f"{self.nome} diz: {mensagem}")

aluno1 = Aluno()
#print(f"{aluno1.nome} tem {aluno1.idade} anos e é do sexo {aluno1.sexo}!")
# Saida: Eduardo tem 17 anos e é do sexo masculino!

#aluno1.nome = "Dudu"
#aluno1.falar("Olá!")
#Dudu diz: Olá!

class Pessoa:
    def __init__(self, nome, idade): # classe construtora Podemos utilizar o construtor para definir valores iniciais para os atributos da classe.
        self.nome = nome
        self.idade = idade

    def falar(self, mensagem):
        print(f"{self.nome} diz: {mensagem}")

#pessoa1 = Pessoa("João", 30)
#print(pessoa1.nome)
#print(pessoa1.idade)
#Saida: João
#       30

class Estudante(Pessoa): # esta classe herda o nome e idadeda classe pessoa!
    def __init__(self, nome, idade, matricula):
        super().__init__(nome, idade)
        self.matricula = matricula
    
estudante1 = Estudante("Maria", 18, "12345")
print(estudante1.nome)  
print(estudante1.idade)  
print(estudante1.matricula)  
estudante1.falar("Olá!")  
# Saida: maria
#        18
#        12345
#        Maria diz: Olá!