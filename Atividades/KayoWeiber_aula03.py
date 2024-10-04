'''
#atividade-01
class ContaBancaria:
    def __init__(self, titular,saldo,numero_conta):
        self.titular=titular
        self.saldo=saldo
        self.numero_conta=numero_conta
    def depositar(self,valor_depositar):
        self.saldo+=valor_depositar
        print(f"depósito de {valor_depositar} realizado com sucesso.")
    def sacar(self, valor_sacar):
        self.saldo-=valor_sacar
        print(f"saque de {valor_sacar} realizado com sucesso.")       
    def exibir_saldo(self):
        print(f"O saldo atual da conta é de {self.saldo}")
        
nome=str(input("Digite o nome do titular da conta: "))
saldo=int(input("Digite o saldo da conta: "))
numero_conta=int(input("Digite o número da conta: "))
while True:
    try:        
        dados=ContaBancaria(nome,saldo,numero_conta)
        while True:
            menu=int(input("Menu:\n1-depositar\n2-sacar\n3-exibir saldo\n4-sair do programa\n digite sua opção desejada: "))
            if menu<1 or menu>4:
                print("Por favor, digite uma das opções!")
            else:
                if menu==1:
                    valor_depositar=float(input("Digite o valor que desejar depositar:"))
                    if valor_depositar<=0:
                        print('Saldo não é válido')
                    else:
                        dados.depositar(valor_depositar)
                elif menu==2:
                    valor_sacar=int(input("Digite o valor que desejar depositar:"))
                    if valor_sacar<dados(saldo):
                        print('Saldo insúficiente')
                    else:
                        dados.sacar(valor_depositar)
                elif menu==3:
                    dados.exibir_saldo()  
                else:
                    break
            break             
    except ValueError:
        print("Valor inválido, digite um valor válido.")

#atividade-02
class QuartoHotel:
    def __init__(self,numero_quarto,tipo_quarto):
        self.numero_quarto=numero_quarto
        self.tipo=tipo_quarto
        self.ocupado=False
    def reservar(self):
        if not self.ocupado:
            self.ocupado=True
            print(f"O quarto {self.numero_quarto} foi reservado.")
        else:
            print(f"O quarto {self.numero_quarto} já está ocupado.")
    def liberar_quarto(self):
            if not self.ocupado:
                self.ocupado=False
                print(f"O quarto {self.numero_quarto} foi liberado.")
            else:
                print(f"O quarto {self.numero_quarto} já está disponível.")
    def verificar_status(self):
        status="ocupado" if self.ocupado else "disponível"
        print(f"O quarto{self.numero_quarto} está {status}")
while True:
    try:
        num_quarto=int(input(f"Digite o número do quarto: "))
        tip_quarto=str(input("Digite um tipo de quarto: "))
        quarto=QuartoHotel(num_quarto,tip_quarto)
        while True:
            menu=int(input("menu:\n1- Reservar quarto\n2- liberar quarto\n3-Verificar status\n4-sair\nresposta: "))
            if menu>0 and menu<5:
                if menu==1:
                    quarto.reservar()
                elif menu==2:
                    quarto.liberar_quarto()
                elif menu==3:
                    quarto.verificar_status()
                else:
                    print("Programa encerrando.")
                    break
            else:
                print("Válor digitado é inválido.")
        break
    
    except ValueError:
        print("Valor inválido, digite um valor válido.")
        




#atividade-03
cidade1=["Frutal","Uberlândia","Uberaba"]
cidade2=["Rio Preto","São Carlos","Barretos", "Rio Claro","São Paulo"]
cidade_res=cidade1+cidade2
print(cidade_res)


#atividade-04
carros=["Gol", "Fusca", "Onix","Uno","Voyage"]
carros[2:4]=["Toro","Virtus"]
print(carros)


#atividade-05
lst_user=[]
lst_user2=[]
for i in range(4):
    nome1=input(f"Digite o nome a ser colocado na lista:")
    lst_user.append(nome1)
for i in range(2):
    nome2=input("digite o nome a ser inserido na posição 1 e 2: ")
    lst_user.insert(i+1,nome2)
for i in range(3):
    nome3=input(f"Digite o nome a ser colocado na lista:")
    lst_user2.append(nome3)    
lst_user.extend(lst_user2)
print(lst_user)


#ex06
lista_alunos = []
lista_matriculas = []
cursos = []
contador_curso = 1
class Aluno:
    def __init__(self, nome, matricula):
        self.nome=nome
        self.matricula=matricula
        lista_alunos.append(self)
        lista_matriculas.append(self.matricula)
    @staticmethod
    def exibir_detalhes():
        if not lista_alunos:
            print("Nenhum aluno cadastrado.")
        else:
            for aluno in lista_alunos:
                print(f"Nome: {aluno.nome}\nMatrícula: {aluno.matricula}\n")
class Curso:
    def __init__(self, nome_curso):
        self.nome_curso=nome_curso
        self.alunos=[]
    def adicionar_aluno(self):
        if not lista_alunos:
            print("Não existe aluno a ser adicionado.")
            return
        for i, aluno in enumerate(lista_alunos, start=1):
            print(f"{i} - {aluno.nome}")
        try:
            aluno_add=int(input("Digite o número do aluno que deseja adicionar ao curso: "))
            if aluno_add<1 or aluno_add>len(lista_alunos):
                print("O valor digitado não é válido.")
            else:
                aluno_selecionado=lista_alunos[aluno_add-1]
                self.alunos.append(aluno_selecionado)
                print(f"Aluno '{aluno_selecionado.nome}' foi adicionado ao curso.")
        except ValueError:
            print("Digite um número válido.")
    def exibir_detalhes_curso(self):
        if not self.alunos:
            print(f"Nenhum aluno matriculado no curso {self.nome_curso}.")
        else:
            print(f"Alunos no Curso {self.nome_curso}:")
            for aluno in self.alunos:
                print(f"Nome: {aluno.nome}\nMatrícula: {aluno.matricula}")
def menu_alunos():
    while True:
        try:
            opcao_aluno=int(input("Menu Aluno:\n1 - Criar Aluno\n2 - Exibir Alunos\n3 - Sair\nEscolha uma opção: "))
            if opcao_aluno==1:
                nome_aluno=input("Digite o nome do aluno: ")
                matricula_aluno=input("Digite a matrícula do aluno: ")
                Aluno(nome_aluno, matricula_aluno)
            elif opcao_aluno==2:
                Aluno.exibir_detalhes()
            elif opcao_aluno==3:
                break
            else:
                print("Opção inválida.")
        except ValueError:
            print("Digite um valor válido.")

def menu_cursos():
    global contador_curso
    while True:
        try:
            opcao_curso=int(input("Menu Curso:\n1 - Criar Curso\n2 - Adicionar Aluno ao Curso\n3 - Exibir Alunos no Curso\n4 - Sair\nEscolha uma opção: "))
            if opcao_curso==1:
                nome_curso=input("Digite o nome do curso: ")
                curso=Curso(nome_curso)
                cursos.append(curso)
                contador_curso+=1
            elif opcao_curso==2:
                if cursos:
                    for idx, curso in enumerate(cursos, start=1):
                        print(f"{idx} - {curso.nome_curso}")
                    try:
                        curso_escolhido=int(input("Digite o número do curso: "))
                        if curso_escolhido<1 or curso_escolhido>len(cursos):
                            print("Número de curso inválido.")
                        else:
                            cursos[curso_escolhido-1].adicionar_aluno()
                    except ValueError:
                        print("Digite um número válido.")
                else:
                    print("Nenhum curso disponível.")
            elif opcao_curso==3:
                if cursos:
                    for idx, curso in enumerate(cursos, start=1):
                        print(f"{idx} - {curso.nome_curso}")
                    try:
                        curso_escolhido=int(input("Digite o número do curso para exibir: "))
                        if curso_escolhido<1 or curso_escolhido>len(cursos):
                            print("Número de curso inválido.")
                        else:
                            cursos[curso_escolhido - 1].exibir_detalhes_curso()
                    except ValueError:
                        print("Digite um número válido.")
                else:
                    print("Nenhum curso disponível.")
            elif opcao_curso==4:
                break
            else:
                print("Opção inválida.")
        except ValueError:
            print("Digite um valor válido.")
while True:
    try:
        menu_principal=int(input("Menu Principal:\n1 - Aluno\n2 - Curso\n3 - Sair\nEscolha uma opção: "))
        if menu_principal==1:
            menu_alunos()
        elif menu_principal==2:
            menu_cursos()
        elif menu_principal==3:
            print("Saindo...")
            break
        else:
            print("Opção inválida.")
    except ValueError:
        print("Digite um valor válido.")

    

#Atividade-07
#ex-7.1
num=[x for x in range(1,11)]
print(num)
#ex-7.2
num=[x for x in range(-50,51,5)]
print(num)
#ex-7.3
num=[x for x in range(1000) if(x%2==0) and (x%3==0)]
print(num)

#atividade-08
notas=[]
cont=1
for i in range(5):
    participante=float(input(f"Digite a nota do participante {cont}: "))
    cont+=1
    notas.append(participante)
notas.sort()
print("Ordem crescente")
notas.reverse()
print(f"Ordem descrecente:{notas}")
print(f"Melhor resultado,{notas[0]}")
print(f"pior desempenho,{notas[-1]}")
'''
#ex08
lista_titulo=[]
lista_prioridade=[]
class Tarefa: #classe que vou utilizar apenas para adicionar a tarefas em seus campos.
    def __init__(self,titulo,prioridade):
        self.titulo=titulo
        self.prioridade=prioridade
        lista_prioridade.append(self.prioridade)
        lista_titulo.append(self.titulo)
class GerenciadorDeTarefas: #classe principal de operações.
    def __init__(self):
        print("Tarefas atuais.")
        print(lista_titulo)
    def adicionar_tarefa(self):
        while True:
            try:
                while True:
                    try:
                        titulo_tarefa=str(input('Digite o título da tarefa: '))
                        grau_prioridade=int(input("De 1 à 5 qual o grau de prioridade dessa tarefa: "))
                        if grau_prioridade<1 or grau_prioridade>5:
                            print("Digite um válor entre 0 e 5, por favor.")
                        else:
                            break
                    except ValueError:
                        print("Por favor digite um valor válido")
                Tarefa(titulo_tarefa,grau_prioridade)
                print("Tarefa adionado com  sucesso.")
                break
            except ValueError:
                print("O válor digitado não é válido.")
    def remover_tarefa(self):
        if not lista_titulo:
            print("Não existe tarefa a ser removida.")
            return
        for i, tarefa in enumerate(lista_titulo, start=1):
            print(f"{i} - {tarefa}")
        while True:
            try:
                tarefa_remov=int(input("Digite o número da atividade que deseja remover: "))
                if tarefa_remov<1 or tarefa_remov>len(lista_titulo):
                    print("O valor digitado não é válido.")
                else:
                    tarefa_select=lista_titulo[tarefa_remov - 1]
                    index_tarefa=lista_titulo.index(tarefa_select) 
                    lista_titulo.remove(tarefa_select)
                    lista_prioridade.remove(lista_prioridade[index_tarefa])
                    print("Tarefa removida.")
                    break
    
            except ValueError:
                print("O Válor digitado não é válido.")
    def listar_tarefa(self):
        if not lista_titulo:
            print("Não existe lista!")
            return
        for i,(tarefa, prioridade) in enumerate(zip(lista_titulo,lista_prioridade),start=1):
            print(f"{i} - Tarefa: {tarefa} Prioridade: {prioridade}")
    def ordenar_tarefas(self):
        if not lista_titulo:
            print("Não existe lista!")
            return
        tarefas_prioridades=list(zip(lista_prioridade,lista_titulo))
        tarefas_prioridades.sort
        for i,(prioridade, tarefa) in enumerate(tarefas_prioridades, start=1):
            print(f"{i} - tarefa: {tarefa}  prioridade {prioridade}")

gerenciador = GerenciadorDeTarefas()
gerenciador.adicionar_tarefa()
#gerenciador.remover_tarefa()
#gerenciador.listar_tarefa()
gerenciador.ordenar_tarefas()
        