
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


#Exercício 2 - Verificação de Expressões Matemáticas (Pilha)
def verificarExpressao(expressao):
    pilha=[]
    simbolos={')': '(', ']': '[', '}': '{'}
    for caractere in expressao:
        if caractere in "([{":
            pilha.append(caractere)
        elif caractere in ")]}":
            if not pilha or pilha.pop()!=simbolos[caractere]:
                return ("A expressão é balanceada")
    return ("A expressão não é balanceada")
expressao1="[(a + b) * (c - d)]"
expressao2="[a + b) * (c - d)]"
expressao3="{[()]}"
expressao4="{[({})]}"

print(verificarExpressao(expressao1))  
print(verificarExpressao(expressao2)) 
print(verificarExpressao(expressao3))  
print(verificarExpressao(expressao4))  


#Exercício 3 - Gerenciamento de Impressão (Fila de Prioridade Simples)

from collections import deque
class Impressora:
    def __init__(self):
        self.fila=deque()
        
    def adicionar_tarefa(self, descricao, urgencia):
        tarefa=(urgencia, descricao)
        inserido=False
        for i in range(len(self.fila)):
            if self.fila[i][0]<urgencia:
                self.fila.insert(i, tarefa)
                inserido=True
                break
        if not inserido:
            self.fila.append(tarefa)
        print(f"Tarefa '{descricao}' adicionada com urgência {urgencia}.")
        
    def imprimir_tarefa(self):
        if self.fila:
            urgencia, descricao=self.fila.popleft()
            print(f"Imprimindo tarefa: '{descricao}' (Urgência: {urgencia})")
        else:
            print("Nenhuma tarefa na fila de impressão.")
            
    def mostrar_fila(self):
        if self.fila:
            print("Fila de impressão:")
            for urgencia, descricao in self.fila:
                print(f"- {descricao} (Urgência: {urgencia})")
        else:
            print("A fila de impressão está vazia.")

impressora = Impressora()
impressora.adicionar_tarefa("Relatório", 3)
impressora.adicionar_tarefa("Contrato", 5)
impressora.adicionar_tarefa("Email", 1)
impressora.mostrar_fila()
impressora.imprimir_tarefa()
impressora.imprimir_tarefa()
impressora.imprimir_tarefa()
impressora.mostrar_fila()


#Exercício 4 - Desfazer e Refazer em um Editor de Texto (Pilha)

class EditorTexto:
    def __init__(self):
        self.realizadas = []
        self.desfeitas = []

    def realizar_acao(self, acao):
        self.realizadas.append(acao)
        self.desfeitas.clear()
        print(f"Ação realizada: '{acao}'")

    def desfazer(self):
        if self.realizadas:
            acao=self.realizadas.pop()
            self.desfeitas.append(acao)
            print(f"Ação desfeita: '{acao}'")
        else:
            print("Nenhuma ação para desfazer.")

    def refazer(self):
        if self.desfeitas:
            acao=self.desfeitas.pop()
            self.realizadas.append(acao)
            print(f"Ação refeita: '{acao}'")
        else:
            print("Nenhuma ação para refazer.")

    def mostrar_estado(self):
        print("\nEstado atual:")
        print(f"Ações realizadas: {self.realizadas}")
        print(f"Ações desfeitas: {self.desfeitas}")
        print()

editor=EditorTexto()
editor.realizar_acao("Escrever 'Olá'")
editor.realizar_acao("Escrever 'Mundo'")
editor.realizar_acao("Apagar 'Mundo'")
editor.mostrar_estado()
editor.desfazer()
editor.desfazer()
editor.mostrar_estado()
editor.refazer()
editor.realizar_acao("Escrever 'Python'")
editor.refazer()
editor.mostrar_estado()

#Exercício 5 - Organização de Vagões de Trem (Pilha e Fila)
from collections import deque

class EstacaoTrem:
    def __init__(self, vagoes):
        self.fila=deque(vagoes)
        self.pilha=[]
        self.resultado=[]

    def organizar_vagoes(self):
        while self.fila or self.pilha:
            if self.pilha and (not self.fila or self.pilha[-1]<self.fila[0]):
                self.resultado.append(self.pilha.pop())
            elif self.fila:
                self.pilha.append(self.fila.popleft())
            else:
                break

    def mostrar_resultado(self):
        if self.resultado==sorted(self.resultado):
            print(f"Vagões organizados: {self.resultado}")
        else:
            print("Não foi possível organizar os vagões em ordem crescente.")

vagoes=[4, 1, 3, 2, 5] 
estacao=EstacaoTrem(vagoes)
print(f"Vagões na entrada: {vagoes}")
estacao.organizar_vagoes()
estacao.mostrar_resultado()

#Exercício 6 - Simulação de Atendimento de Chamadas (Fila Circular)
class FilaCircular:
    def __init__(self, capacidade):
        self.capacidade=capacidade
        self.fila=[None]*capacidade 
        self.inicio=0
        self.fim=0
        self.tamanho=0 
        
    def adicionar_chamada(self, chamada):
        if self.tamanho==self.capacidade:
            print(f"Fila cheia. Substituindo chamada mais antiga: {self.fila[self.inicio]}")
            self.inicio = (self.inicio + 1) % self.capacidade
        else:
            self.tamanho+=1
        self.fila[self.fim]=chamada
        self.fim=(self.fim + 1) % self.capacidade
        print(f"Chamada '{chamada}' adicionada à fila.")

    def atender_chamada(self):
        if self.tamanho==0:
            print("Nenhuma chamada para atender.")
            return None
        chamada=self.fila[self.inicio]
        self.fila[self.inicio]=None
        self.inicio=(self.inicio + 1)%self.capacidade
        self.tamanho-=1
        print(f"Chamada '{chamada}' atendida.")
        return chamada

    def visualizar_fila(self):
        if self.tamanho==0:
            print("A fila está vazia.")
            return

        print("Fila de chamadas:")
        i=self.inicio
        for _ in range(self.tamanho):
            print(f"- {self.fila[i]}")
            i=(i + 1) % self.capacidade

fila = FilaCircular(3)
fila.adicionar_chamada("Chamada 1")
fila.adicionar_chamada("Chamada 2")
fila.adicionar_chamada("Chamada 3")
fila.visualizar_fila()
fila.adicionar_chamada("Chamada 4")
fila.visualizar_fila()
fila.atender_chamada()
fila.visualizar_fila()
fila.adicionar_chamada("Chamada 5")
fila.visualizar_fila()

#Exercício 7 - Verificação de Palíndromo (Pilha e Fila)
from collections import deque

def verificar_palindromo(palavra):
    fila=deque()  
    pilha=[]      
    for caractere in palavra:
        fila.append(caractere)
        pilha.append(caractere)
    while fila:
        if fila.popleft()!=pilha.pop():
            return False
    return True

palavras=["radar", "arara", "python", "nivel", "palindromo"]
for palavra in palavras:
    if verificar_palindromo(palavra):
        print(f"'{palavra}' é um palíndromo.")
    else:
        print(f"'{palavra}' não é um palíndromo.")


#exercício 8 - Análise de Pedidos em um Restaurante (Fila e Pilha)
from collections import deque

class Restaurante:
    def __init__(self):
        self.fila_pedidos=deque()  
        self.pilha_pratos=[]       
    def adicionar_pedido(self, pedido):
        self.fila_pedidos.append(pedido)
        print(f"Pedido '{pedido}' adicionado à fila.")

    def preparar_pedido(self):
        if not self.fila_pedidos:
            print("Nenhum pedido na fila para preparar.")
            return
        pedido=self.fila_pedidos.popleft()
        self.pilha_pratos.append(pedido)
        print(f"Pedido '{pedido}' foi preparado e adicionado à pilha de pratos servidos.")

    def servir_prato(self):
        if not self.pilha_pratos:
            print("Nenhum prato pronto para servir.")
            return
        prato=self.pilha_pratos.pop()
        print(f"Prato '{prato}' foi servido.")

    def mostrar_estado(self):
        print("\nEstado atual:")
        print(f"Fila de pedidos: {list(self.fila_pedidos)}")
        print(f"Pilha de pratos servidos: {self.pilha_pratos}")
        print()

restaurante = Restaurante()
restaurante.adicionar_pedido("Pizza")
restaurante.adicionar_pedido("arroz")
restaurante.adicionar_pedido("Salada")
restaurante.mostrar_estado()
restaurante.preparar_pedido()
restaurante.preparar_pedido()
restaurante.mostrar_estado()
restaurante.servir_prato()
restaurante.mostrar_estado()
restaurante.preparar_pedido()
restaurante.servir_prato()
restaurante.servir_prato()
restaurante.mostrar_estado()

#Exercício 9 - Filtragem de Dados em Lote (Fila e Pilha)
from collections import deque

class ProcessamentoSensores:
    def __init__(self):
        self.fila_dados=deque()
        self.pilha_dados_validos=[]

    def receber_dados(self, dados):
        for dado in dados:
            self.fila_dados.append(dado)
        print(f"Dados recebidos: {dados}")

    def verificar_qualidade(self):
        while self.fila_dados:
            dado=self.fila_dados.popleft()
            if self.eh_valido(dado):
                self.pilha_dados_validos.append(dado)
                print(f"Dado '{dado}' é válido e foi adicionado à pilha.")
            else:
                print(f"Dado '{dado}' é inválido e foi descartado.")

    def eh_valido(self, dado):
        return isinstance(dado, (int, float)) and dado>=0

    def enviar_dados(self):
        if not self.pilha_dados_validos:
            print("Nenhum dado válido para enviar.")
            return
        print(f"Enviando dados válidos: {self.pilha_dados_validos}")
        self.pilha_dados_validos.clear()

    def mostrar_estado(self):
        print("\nEstado atual:")
        print(f"Fila de dados: {list(self.fila_dados)}")
        print(f"Pilha de dados válidos: {self.pilha_dados_validos}")
        print()

processador = ProcessamentoSensores()
processador.receber_dados([10, -5, 20.5, "erro", 15, 0])
processador.mostrar_estado()
processador.verificar_qualidade()
processador.mostrar_estado()
processador.enviar_dados()
processador.mostrar_estado()
'''


#Exercício 10 - Caminho de Labirinto (Pilha)
def encontrar_saida(labirinto, inicio, fim):
    pilha = []
    caminho_percorrido = []
    movimentos = [(0, 1), (1, 0), (0, -1), (-1, 0)]  #direita, baixo, esquerda, cima
    pilha.append(inicio)
    while pilha:
        atual = pilha.pop()
        caminho_percorrido.append(atual)
        if atual == fim:
            return caminho_percorrido
        x, y = atual
        labirinto[x][y]=1
        for dx, dy in movimentos:
            novo_x, novo_y = x + dx, y + dy
            if 0 <= novo_x < len(labirinto) and 0 <= novo_y < len(labirinto[0]) and labirinto[novo_x][novo_y] == 0:
                pilha.append((novo_x, novo_y))
    return "Não há caminho possível até a saída."
labirinto = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [1, 1, 0, 1, 0],
    [0, 0, 0, 0, 0],
]
inicio = (0, 0)
fim = (4, 4)

caminho = encontrar_saida(labirinto, inicio, fim)
print("Caminho percorrido:", caminho)
