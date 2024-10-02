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
#atividade-06
lista_aluno=[]
lista_matricula=[]
cursos=[]
contador_curso=1
class aluno:
    def __init__(self,nome,matricula):
        self.nome = nome
        self.matricula = matricula
        lista_aluno.append(self)
        lista_matricula.append(self.matricula)
    def exibir_detalhes(self):
        for aluno in lista_aluno:
            print(f"Nome: {aluno.nome}\nMatrícula: {aluno.matricula}\n")
class Curso:
    def __init__(self, nome_curso):
        self.nome_curso=nome_curso
        self.alunos=[]
    def adionar_aluno(self):
        if not lista_aluno:
            print("Não existe aluno a ser adicionado.")
            return
        for i, aluno in enumerate(lista_aluno, start=1):
            print(f"{i} - {aluno.nome}")
        try:
            aluno_add=int(input("Digite o número do aluno que deseja adicionar ao curso: "))
            if aluno_add<1 or aluno_add>len(lista_aluno):
                print("O valor digitado não é válido.")
            else:
                aluno_selecionado=lista_aluno[aluno_add-1]
                self.alunos.append(aluno_selecionado)
                print(f"Aluno '{aluno_selecionado.nome}' foi adicionado ao curso.")
        except ValueError:
            print("Digite um número válido.")
    def exibir_detalhes_curso(self):
        for aluno in self.alunos:
            print(f"Alunos no Curso {self.nome_curso}\nNome: {aluno.nome}\nMatrícula: {aluno.matricula}")
while True:
    try:
        while True:
            menu=int(input("menu:\n1- aluno\n2- Curso\n3-sair\nDigite a opção desejada: "))
            if menu<1 or menu>3:
                print("O válor digitado não é válido.")
            else:
                if menu==1:
                    count=0
                    while True:
                        try:
                            menu_aluno=int(input("menu:\n1-criar aluno\n2-exibir alunos\n3-sair"))
                            if menu_aluno>3 or menu_aluno<1:
                                print("Digite um valor válido")
                            else:
                                if menu_aluno==1:
                                    add_aluno=str(input(f"Digite o nome do aluno {count}: "))
                                    add_matricula=str(input(f"Digite a matricula do aluno {count}: "))
                                    aluno_class = aluno(add_aluno,add_matricula)
                                    count+=1
                                elif menu_aluno==2:
                                    aluno_class.exibir_detalhes()
                                
                                else:
                                    break
                        except ValueError:
                            print("O valor digitado não é válido.")
                elif menu==2:
                    while True:
                        try:
                            menu_curso=int(input("Menu:\n1-criar curso\n2-Adionar aluno ao curso\n3-exibir alunos\n4-sair"))
                            if menu_curso>4 or menu_curso<1:
                                print("Por favor, digite uma opção válida.")
                            elif menu_curso==1:
                                nome_curso=str(input("Digite o nome do curso"))
                                num_curso=nome_curso+str(contador_curso)
                                num_curso=Curso(nome_curso)
                                cursos.append(nome_curso)
                            elif menu_curso==2:
                                if cursos:
                                    for idx, curso in enumerate(cursos, start=1):
                                        print(f"{idx} - {curso.nome_curso}")
                                    try:
                                        curso_escolhido = int(input("Digite o número do curso ao qual deseja adicionar alunos: "))
                                        if curso_escolhido<1 or curso_escolhido>len(cursos):
                                            print("Número de curso inválido.")
                                        else:
                                            cursos[curso_escolhido - 1].adicionar_aluno()
                                    except ValueError:
                                        print("Digite um número válido.")
                                else:
                                    print("Nenhum curso disponível.")  
                            elif menu_curso==3:
                                if cursos:
                                    for idx, curso in enumerate(cursos, start=1):
                                        print(f"{idx} - {curso.nome_curso}")
                                    try:
                                        curso_escolhido=int(input("Digite o número do curso que deseja exibir: "))
                                        if curso_escolhido<1 or curso_escolhido>len(cursos):
                                            print("Número de curso inválido.")
                                        else:
                                            cursos[curso_escolhido - 1].exibir_detalhes_curso()
                                    except ValueError:
                                        print("Digite um número válido.")
                                else:
                                    print("Nenhum curso disponível.")
                            else:
                                break
                        except ValueError:
                            print("Digite um válor válido.")            
    except ValueError:
        print("Digite um valor válido")          
            
        
