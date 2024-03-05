#Apresentação do programa ao usuário

print("Bem vindo ao programa de Notas e Médias! /n")

def inicio():
    escolha=(int(input("Escolha uma opção: Listar alunos (1) Pesquisar notas por aluno (2) Pesquisar média por aluno (3) Sair(4) Retornar ao menu (5)")))
    if escolha > 5:
        print("Essa opção é inválida. Escolha novamente!")
        inicio()

    elif escolha == 4:
        #fechar programa
        print("O programa será fechado!")


inicio()







