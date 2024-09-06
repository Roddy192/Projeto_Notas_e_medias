#Importar funções
import time

#variáveis
alunos={}


#Apresentação do programa ao usuário

print("Bem vindo ao programa de Notas e Médias! /n")


#Funções das opções do menu

  #listar
def listar_alunos(list_student):
    for key in alunos:
        print(key)

    time.sleep(5)
    inicio()

  #exibir notas por aluno
def notas_aluno(list_alunos):
    aluno_n=str(input("Digite o nome do aluno: "))
    for key, values in alunos.items():
        if aluno_n==key:
            esc_aluno=alunos[aluno_n]
            print(f"As notas do aluno {aluno_n} são:")
            print(esc_aluno)
        
        else:
            print("Aluno inexistente!")
            notas_aluno()
            
    time.sleep(5)
    inicio()

  #Exibir média no aluno
def media_aluno(list_alunos):
    aluno_m=str(input("Digite o nome do aluno: "))
    media_final=0
    for key, value in alunos.items():
        if key==aluno_m:
            media=0
            notas=alunos[aluno_m]
            media=sum(notas)

        else:
            print("Aluno inexistente!")
            media_aluno()

    media_final=media/4
    print(f"A média do aluno {aluno_m} é: {media_final}")
    print("Retornando ao menu inicial.....")

    time.sleep(5)
    inicio()

  #Adicionar aluno
def add_aluno(list_alunos):
    aluno=(input("Digite o nome do aluno a ser adicionado: "))
    alunos.update({aluno : ""})
    n1=float(input("Digite a nota 1 do aluno: "))
    n2=float(input("Digite a nota 2 do aluno: "))
    n3=float(input("Digite a nota 3 do aluno: "))
    n4=float(input("Digite a nota 4 do aluno: "))
    n_all=[n1, n2, n3, n4]
    alunos[aluno]=n_all
    print("O aluno abaixo foi adicionado com sucesso a Base de dados!")
    print(f"{aluno} -> {n_all}")
    print("Retornando ao menu inicial.....")

    time.sleep(5)
    inicio()











#Função do menu
def inicio():
    escolha=(int(input("Escolha uma opção: Listar alunos (1) Adicionar aluno (2) Listar notas por aluno (3) Listar média por aluno (4) Sair (5)  : ")))
    if escolha > 5:
        print("Essa opção é inválida. Escolha novamente!")
        inicio()

    elif escolha == 5:
        #fechar programa
        print("O programa será fechado!")
    
    elif escolha == 1:
        listar_alunos(alunos)

    elif escolha == 2:
        add_aluno(alunos)
    
    elif escolha == 3:
        notas_aluno(alunos)

    elif escolha == 4:
        media_aluno(alunos)




    



inicio()







