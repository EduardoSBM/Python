def div():
    a = int(input("Digite um número: "))
    b = int(input("Digite um número: "))
    c = a//b
    return c

def soma():
    a = int(input("Digite um número: "))
    b = int(input("Digite um número: "))
    c = a+b
    return c

def x():
    a = int(input("Digite um número: "))
    b = int(input("Digite um número: "))
    c = a * b
    return c

def menos():
    a = int(input("Digite um número: "))
    b = int(input("Digite um número: "))
    c = a-b
    return c
def main():
    while True:
        print("Bem-vindo a sua calculadora.")
        print("1 - divisão")
        print("2 - soma")
        print("3 - multiplicação")
        print("4 - subtração")
        print("5 - encerrar")
        op = int(input("Digite a opção desejada: "))

        if ( op ==1):
            print(div())

        if ( op ==2):
            print(soma())

        if ( op ==3):
            print(x())

        if ( op ==4):
            print(menos())

        if ( op ==5):
            break;
main()
