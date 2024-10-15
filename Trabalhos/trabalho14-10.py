alunos = []
matriculas = []
alunos_objetos = []

class Aluno:
    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula
        self.disciplinas = []
        alunos.append(nome)
        matriculas.append(matricula)
        alunos_objetos.append(self)
    def adicionar_disciplina(self, disciplina):
        self.disciplinas.append(disciplina)
        print(f"Disciplina {disciplina} adicionada para o aluno {self.nome}.")
    def remover_disciplina(self, disciplina):
        if disciplina in self.disciplinas:
            self.disciplinas.remove(disciplina)
            print(f"Disciplina {disciplina} removida do aluno {self.nome}.")
        else:
            print(f"Disciplina {disciplina} não encontrada para o aluno {self.nome}.")
    def alterar(self):
        while True:
            pedido = int(input("menu\n1-Alterar nome\n2-Alterar matrícula\n3-Sair\nDigite a opção desejada: "))
            if pedido < 1 or pedido > 3:
                print("O valor digitado não é válido")
            else:
                if pedido == 1:
                    novo_nome = str(input("Digite o novo nome: "))
                    alunos[alunos.index(self.nome)] = novo_nome
                    self.nome = novo_nome
                    print("Alteração realizada com sucesso")
                    lista_enca.adicionar_aluno(novo_nome)
                elif pedido == 2:
                    nova_matricula = str(input("Digite a nova matrícula: "))
                    matriculas[matriculas.index(self.matricula)] = nova_matricula
                    self.matricula = nova_matricula
                    print("Alteração realizada com sucesso")
                elif pedido == 3:
                    break
class Nodo:
    def __init__(self, dado, proximo=None):
        self.dado = dado
        self.proximo = proximo
class ListaEncadeadaDeAlunos:
    def __init__(self):
        self.cabeca = None
    def adicionar_aluno(self, valor):
        novo_aluno = Nodo(valor)
        novo_aluno.proximo = self.cabeca
        self.cabeca = novo_aluno
    def remover_aluno(self, valor):
        corrente = self.cabeca
        anterior = None
        if corrente and corrente.dado == valor:
            self.cabeca = corrente.proximo
            print(f"Aluno {valor} removido!")
            return
        while corrente and corrente.dado != valor:
            anterior = corrente
            corrente = corrente.proximo
        if corrente:
            anterior.proximo = corrente.proximo
            print(f"Aluno {valor} removido!")
        else:
            print(f"Aluno {valor} não encontrado para remover!")
    def buscar_aluno(self, valor):
        corrente = self.cabeca
        sts = False
        while corrente:
            if corrente.dado == valor:
                print(f"Aluno encontrado: {valor}")
                sts = True
                break
            corrente = corrente.proximo
        if not sts:
            print("Aluno NÃO encontrado")
    def listar_alunos(self):
        corrente = self.cabeca
        while corrente:
            print(corrente.dado)
            corrente = corrente.proximo
lista_enca = ListaEncadeadaDeAlunos()

while True:
    try:
        menu_principal = int(input("Menu:\n1-Cadastrar um novo aluno\n2-Adicionar uma disciplina a um aluno\n3-Remover uma disciplina de um aluno\n4-Alterar dados do aluno(nome ou matrícula)\n5-Remover aluno\n6-Listar todos os alunos\n7-Sair do sistema\nDigite sua opção desejada: "))
        if menu_principal < 1 or menu_principal > 7:
            print("O valor digitado não é válido")
        else:
            if menu_principal == 1:
                nome_aluno = str(input("Digite o nome do Aluno: "))
                matr = int(input("Digite a Matrícula do aluno:"))
                novo_aluno = Aluno(nome_aluno, matr)
                lista_enca.adicionar_aluno(novo_aluno.nome)
            elif menu_principal == 2:
                nome_aluno = str(input("Digite o nome do Aluno: "))
                if nome_aluno in alunos:
                    disciplina = str(input("Digite o nome da disciplina: "))
                    for aluno in alunos_objetos:
                        if aluno.nome == nome_aluno:
                            aluno.adicionar_disciplina(disciplina)
                            break
                else:
                    print("Aluno não encontrado.")
            elif menu_principal == 3:
                lista_enca.listar_alunos()
                nome_aluno = str(input("Digite o nome do Aluno: "))
                if nome_aluno in alunos:
                    disciplina = str(input("Digite o nome da disciplina: "))
                    for aluno in alunos_objetos:
                        if aluno.nome == nome_aluno:
                            aluno.remover_disciplina(disciplina)
                            break
                else:
                    print("Aluno não encontrado.")
            elif menu_principal == 4:
                lista_enca.listar_alunos()
                aluno_alterar = str(input("Digite o nome do aluno que deseja alterar: "))
                if aluno_alterar in alunos:
                    for aluno in alunos_objetos:
                        if aluno.nome == aluno_alterar:
                            lista_enca.remover_aluno(aluno_alterar)
                            aluno.alterar()
                            break
                else:
                    print("Aluno não encontrado.")
            elif menu_principal == 5:
                lista_enca.listar_alunos()
                aluno_select = str(input("Digite o nome do Aluno que deseja remover: "))
                lista_enca.remover_aluno(aluno_select)
            elif menu_principal == 6:
                lista_enca.listar_alunos()
            else:
                print("Programa finalizado")
                break
    except ValueError:
        print("Valor inválido!")