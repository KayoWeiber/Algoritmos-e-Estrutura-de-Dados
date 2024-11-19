
'''
#Exercício 1 - Atendendo Clientes no Banco (Fila)
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
        print("")
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
                Bank.exibirFila()
            elif menu==2:
                Bank.atenderCliente()
                Bank.exibirFila()
            elif menu==3:
                Bank.exibirFila()
            else:
                print("Programa Finalizado.")
                break      
    except ValueError:
        print("O válor digitado não é válido!")

'''
#Exercício 2 - Verificação de Expressões Matemáticas (Pilha)
def verificarExpressao(expressao):
    pilha=[]
    simbolos={')': '(', ']': '[', '}': '{'}
    for caractere in expressao:
        if caractere in "([{":
            pilha.append(caractere)
        elif caractere in ")]}":
            if not pilha or pilha.pop()!=simbolos[caractere]:
                return False
    return True
expressao1="[(a + b) * (c - d)]"
expressao2="[a + b) * (c - d)]"
expressao3="{[()]}"
expressao4="{[({})]}"

print(verificarExpressao(expressao1))  
print(verificarExpressao(expressao2)) 
print(verificarExpressao(expressao3))  
print(verificarExpressao(expressao4))  
