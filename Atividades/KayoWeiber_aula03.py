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
            print(f"O quarto {self.numero_quarto} foi reservado.")
    def liberar_quarto(self):
            if not self.ocupado:
                self.ocupado=False
                print(f"O quarto {self.numero_quarto} foi liberado.")
            else:
                print(f"O quarto {self.numero_quarto} já está disponível.")
    def verificar_status(self):
        status="ocupado" if self.ocupado else "disponível"
        print(f"O quarto{self.numero_quarto}")

        




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


#atividade-06
lista_aluno=[]
lista_matricula=[]
class aluno:
    def __init__(self,nome,matricula):
        self.nome=nome
        self.matricula=matricula
        lista_aluno.append(nome)
        lista_matricula.append(matricula)
    def exibir_detalhes(self):
        num=0
        for i in lista_aluno:
            print("nome:",lista_aluno[num],"\nmátricula:",lista_matricula[num])
            num+=1
class Curso:
    def __init__(self,nome_curso,alunos_curso):
        self.nome_curso=nome_curso
        self.alunos=alunos_curso
        nome_curso=[]

dados=aluno("KAyo",10)
dados.exibir_detalhes()

#TERMINAR EXERCÍCIOS 06







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
'''
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
