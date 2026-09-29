# Lista de Exercícios - Funções em Python


# Questão 01

def apresentar():
    print("Bem-vindo à disciplina de Programação!")


# Questão 02

def saudacao(nome):
    return f"Olá, {nome}! Seja bem-vinda à programação."


# Questão 03

def somar(a, b):
    return a + b


# Questão 04

def verificar_par(numero):
    if numero % 2 == 0:
        return True
    else:
        return False


# Questão 05

def calcular_media(n1, n2, n3):
    return (n1 + n2 + n3) / 3


def verificar_situacao(media):
    if media >= 7:
        return "Aprovado"
    elif media >= 5:
        return "Recuperação"
    else:
        return "Reprovado"


# Questão 06

def maior_numero(a, b, c):
    maior = a

    if b > maior:
        maior = b

    if c > maior:
        maior = c

    return maior


# Questão 07

def somar_calculadora(a, b):
    return a + b


def subtrair(a, b):
    return a - b


def multiplicar(a, b):
    return a * b


def dividir(a, b):
    if b == 0:
        return None
    return a / b


# Questão 08

def celsius_para_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32


def fahrenheit_para_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9


# Questão 09

alunos = []


def cadastrar_aluno():
    nome = input("Nome: ")
    idade = int(input("Idade: "))
    curso = input("Curso: ")

    aluno = {
        "nome": nome,
        "idade": idade,
        "curso": curso
    }

    alunos.append(aluno)

    print("Aluno cadastrado com sucesso!")


def listar_alunos():
    if len(alunos) == 0:
        print("Nenhum aluno cadastrado.")
        return

    for aluno in alunos:
        print("Nome:", aluno["nome"])
        print("Idade:", aluno["idade"])
        print("Curso:", aluno["curso"])
        print()


def buscar_aluno():
    nome = input("Digite o nome do aluno: ")

    for aluno in alunos:
        if aluno["nome"].lower() == nome.lower():
            print("Nome:", aluno["nome"])
            print("Idade:", aluno["idade"])
            print("Curso:", aluno["curso"])
            return

    print("Aluno não encontrado.")


def menu_cadastro():
    while True:
        print()
        print("1 - Cadastrar")
        print("2 - Listar")
        print("3 - Buscar")
        print("4 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_aluno()

        elif opcao == "2":
            listar_alunos()

        elif opcao == "3":
            buscar_aluno()

        elif opcao == "4":
            break

        else:
            print("Opção inválida.")


# Questão 10

alunos_academico = []


def cadastrar_aluno_academico():
    nome = input("Nome: ")
    idade = int(input("Idade: "))
    curso = input("Curso: ")
    nota1 = float(input("Nota 1: "))
    nota2 = float(input("Nota 2: "))
    nota3 = float(input("Nota 3: "))

    aluno = {
        "nome": nome,
        "idade": idade,
        "curso": curso,
        "nota1": nota1,
        "nota2": nota2,
        "nota3": nota3
    }

    alunos_academico.append(aluno)

    print("Aluno cadastrado com sucesso!")


def listar_alunos_academico():
    if len(alunos_academico) == 0:
        print("Nenhum aluno cadastrado.")
        return

    for aluno in alunos_academico:
        print("Nome:", aluno["nome"])
        print("Idade:", aluno["idade"])
        print("Curso:", aluno["curso"])
        print("Nota 1:", aluno["nota1"])
        print("Nota 2:", aluno["nota2"])
        print("Nota 3:", aluno["nota3"])
        print()


def buscar_aluno_academico():
    nome = input("Digite o nome do aluno: ")

    for aluno in alunos_academico:
        if aluno["nome"].lower() == nome.lower():
            return aluno

    return None


def calcular_media_academico(aluno):
    media = (
        aluno["nota1"] +
        aluno["nota2"] +
        aluno["nota3"]
    ) / 3

    return media


def verificar_situacao_academico(media):
    if media >= 7:
        return "Aprovado"
    elif media >= 5:
        return "Recuperação"
    else:
        return "Reprovado"


def menu_academico():
    while True:
        print()
        print("1 - Cadastrar aluno")
        print("2 - Listar alunos")
        print("3 - Calcular média")
        print("4 - Verificar situação")
        print("5 - Buscar aluno")
        print("6 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_aluno_academico()

        elif opcao == "2":
            listar_alunos_academico()

        elif opcao == "3":
            aluno = buscar_aluno_academico()

            if aluno is not None:
                media = calcular_media_academico(aluno)
                print("Média:", media)
            else:
                print("Aluno não encontrado.")

        elif opcao == "4":
            aluno = buscar_aluno_academico()

            if aluno is not None:
                media = calcular_media_academico(aluno)
                situacao = verificar_situacao_academico(media)

                print("Média:", media)
                print("Situação:", situacao)
            else:
                print("Aluno não encontrado.")

        elif opcao == "5":
            aluno = buscar_aluno_academico()

            if aluno is not None:
                print("Nome:", aluno["nome"])
                print("Idade:", aluno["idade"])
                print("Curso:", aluno["curso"])
                print("Nota 1:", aluno["nota1"])
                print("Nota 2:", aluno["nota2"])
                print("Nota 3:", aluno["nota3"])
            else:
                print("Aluno não encontrado.")

        elif opcao == "6":
            break

        else:
            print("Opção inválida.")


# Menu principal

while True:
    print()
    print("Lista de Exercícios")
    print("1 - Questão 01")
    print("2 - Questão 02")
    print("3 - Questão 03")
    print("4 - Questão 04")
    print("5 - Questão 05")
    print("6 - Questão 06")
    print("7 - Questão 07")
    print("8 - Questão 08")
    print("9 - Questão 09")
    print("10 - Questão 10")
    print("0 - Sair")

    opcao = input("Escolha uma questão: ")

    if opcao == "1":
        apresentar()

    elif opcao == "2":
        nome = input("Digite seu nome: ")
        print(saudacao(nome))

    elif opcao == "3":
        numero1 = float(input("Primeiro número: "))
        numero2 = float(input("Segundo número: "))
        print("Resultado:", somar(numero1, numero2))

    elif opcao == "4":
        numero = int(input("Digite um número: "))

        if verificar_par(numero):
            print("O número é par.")
        else:
            print("O número é ímpar.")

    elif opcao == "5":
        nota1 = float(input("Nota 1: "))
        nota2 = float(input("Nota 2: "))
        nota3 = float(input("Nota 3: "))

        media = calcular_media(nota1, nota2, nota3)

        print("Média:", media)
        print("Situação:", verificar_situacao(media))

    elif opcao == "6":
        numero1 = float(input("Primeiro número: "))
        numero2 = float(input("Segundo número: "))
        numero3 = float(input("Terceiro número: "))

        print("Maior número:", maior_numero(numero1, numero2, numero3))

    elif opcao == "7":
        while True:
            print()
            print("Calculadora")
            print("1 - Somar")
            print("2 - Subtrair")
            print("3 - Multiplicar")
            print("4 - Dividir")
            print("5 - Sair")

            escolha = input("Escolha uma opção: ")

            if escolha == "5":
                break

            numero1 = float(input("Primeiro número: "))
            numero2 = float(input("Segundo número: "))

            if escolha == "1":
                print("Resultado:", somar_calculadora(numero1, numero2))

            elif escolha == "2":
                print("Resultado:", subtrair(numero1, numero2))

            elif escolha == "3":
                print("Resultado:", multiplicar(numero1, numero2))

            elif escolha == "4":
                resultado = dividir(numero1, numero2)

                if resultado is None:
                    print("Não é possível dividir por zero.")
                else:
                    print("Resultado:", resultado)

            else:
                print("Opção inválida.")

    elif opcao == "8":
        while True:
            print()
            print("Conversor")
            print("1 - Celsius para Fahrenheit")
            print("2 - Fahrenheit para Celsius")
            print("3 - Sair")

            escolha = input("Escolha uma opção: ")

            if escolha == "1":
                celsius = float(input("Temperatura em Celsius: "))
                print(
                    "Temperatura em Fahrenheit:",
                    celsius_para_fahrenheit(celsius)
                )

            elif escolha == "2":
                fahrenheit = float(input("Temperatura em Fahrenheit: "))
                print(
                    "Temperatura em Celsius:",
                    fahrenheit_para_celsius(fahrenheit)
                )

            elif escolha == "3":
                break

            else:
                print("Opção inválida.")

    elif opcao == "9":
        menu_cadastro()

    elif opcao == "10":
        menu_academico()

    elif opcao == "0":
        print("Programa encerrado.")
        break

    else:
        print("Opção inválida.")