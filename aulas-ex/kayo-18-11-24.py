'''
#ATIVIDADE 1 FIFO
fila=[]
while True:
    try:
        menu=int(input("\nMenu:\n1-Inserir elemento\n2-Remover elemento\n3-Verificar tamanho da lista\n4-Localicar elemento\n5-Verificar a posição do elemento\n6-sair\n Digite o item desejável:"))
        if menu<0 or menu>6:
            print("O válor digitado não é válido")
        else:
            if menu==1:
                elementoInser=int(input("Digite o número que deseja adicionar na fila: "))
                fila.append(elementoInser)
            elif menu==2:
                fila.pop(0)
                print("O primeiro elemento foi removido")
            elif menu==3:
                
                print(f"O tamanho da fila é: {len(fila)}")
            elif menu==4:
                elementoLoc=int(input("Digite o valor que deseja localizar posição:"))
                count=0
                for i,a in enumerate(fila):
                    if a==elementoLoc:
                        print(f"Posição:{i+1} - elemento {a}")
                    else:
                            count+=1
                if count==len(fila):
                    print("Item não encontrado")
                
            elif menu==5:
                for i,a in enumerate(fila):
                    print(f"Posição:{i+1} - elemento {a}")
            else:
                print("Programa finalizado")
                break      
    except ValueError:
        print("Valor inválido")
        
#ATIVIDADE 2 FIFO
from collections import deque
class banco:
    def __init__(self):
        self.fila=deque([])
    def adicionarCliente(self,nome):
        self.fila.append(nome)
        print("Cliente adicionado com sucesso!")
    def atenderCliente(self):
        self.fila.popleft()
        print("Cliente atendido!")
    def exibirFila(self):
        for i in self.fila:
            print(i)
Bank=banco()
while True:
    try:
        menu=int(input("\nMenu:\n1-Adicionar Cliente a fila\n2-Atender próximo cliente\n3-Exibir fila de cliente\n4-sair\n Digite a operação desejada: "))
        if menu<0 or menu>5:
            print("Por favor, digite um número válido!")
        else:
            if menu==1:
                while True:
                    try:
                        cliente=str(input('Digite o nome do cliente:'))
                        break
                    except ValueError:
                        print("O valor digitado está incorreto.")
                Bank.adicionarCliente(cliente)
            elif menu==2:
                Bank.atenderCliente()
            elif menu==3:
                Bank.exibirFila()
            else:
                print("Programa Finalizado.")
                break      
    except ValueError:
        print("O válor digitado não é válido!")
    


#ATIVIDADE LIFO
class Hist:
    
    def __init__(self):
        self.dicio=[]

    def adicionar(self,id,url,timestamp):
        Historico={"id":id,"url":url,"timestamp":timestamp}
        self.dicio.append(Historico)
        print("Histórico atualizado")
        
    def exibirHistorico(self):
        if self.dicio:
            for i in self.dicio[::-1]:
                print(i)
        else:
            print("historico está vazio.")
            
    def removerPag(self):
        if self.dicio:
            self.dicio.pop()
            print("Ultimo item acessado foi removido")
        else:
            print("historico está vazio.")
            
    def limparHistorico(self):
        self.dicio.clear()
        print("historico limpo!")
        
historico=Hist()

while True:
    try:
        menu=int(input("\nMenu:\n1-Adicionar página ao histórico\n2-Remover a última página visitada\n3-Exibir histórico atual\n4-Limpar o Histórico\n5-SAIR\n Digite a operação desejada: "))
        if menu<0 or menu>5:
            print("Por favor, digite um número válido!")
        else:
            if menu==1:
                while True:
                    try:
                        id=int(input("Digite o ID do historico: "))
                        url=str(input("Digite a URL do historico: "))
                        timestamp=str(input("Digite a quantidade de tempo acessado: "))
                        break
                    except ValueError:
                        print("O valor digitado está incorreto.")
                historico.adicionar(id,url,timestamp)
            elif menu==2:
                historico.removerPag()
            elif menu==3:
                historico.exibirHistorico()
            elif menu==4:
                historico.limparHistorico()
            else:
                print("Programa Finalizado.")
                break
                
    except ValueError:
        print("O válor digitado não é válido!")
'''
