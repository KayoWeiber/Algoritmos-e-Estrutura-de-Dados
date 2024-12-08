class NodoArvore:
    def __init__(self,dado):
        self.dado=dado
        self.esquerda=None
        self.direita=None
class arvoreBinaria:
    def __init__(self):
        self.raiz=None
        
    def inserir(self,dado):
        self.raiz=self.inseriRecursivamente(self.raiz,dado)
        print(f"{dado} foi inserido com sucesso ")
        
    def inseriRecursivamente(self,raiz,dado):
        if raiz is None: return NodoArvore(dado)
        if dado<raiz.dado:raiz.esquerda=self.inseriRecursivamente(raiz.esquerda,dado)
        else:raiz.direita=self.inseriRecursivamente(raiz.direita,dado)
        return raiz
    
    def procurar(self, dado):
        nodo = self.procurarRecursivamente(self.raiz, dado)
        if nodo:print(f"O valor {dado} foi encontrado.")
        else: print(f"O valor {dado} não existe.")
        return nodo

    def procurarRecursivamente(self, raiz, dado):
        if raiz is None or raiz.dado == dado:
            return raiz
        if dado<raiz.dado:
            return self.procurarRecursivamente(raiz.esquerda, dado)
        return self.procurarRecursivamente(raiz.direita, dado)
    def excluir(self,dado):
        if not self.procurar(dado):
            print(f"O valor {dado} não pode ser apagado porque não existe.")
            return
        self.raiz=1
        self.excluirRecursivamente(self.raiz, dado)
        print(f"O valor {dado} foi excluído.")
        
    def excluirRecursivamente(self,raiz,dado):
        if raiz is None: 
            return raiz
        if dado<raiz.dado: raiz.esquerda=self.excluirRecursivamente(raiz.esquerda,dado)
        elif dado>raiz.dado: raiz.direita=self.excluirRecursivamente(raiz.direita,dado)
        else:
            if raiz.esquerda is None:return raiz.direita
            elif raiz.direita is None:return raiz.esquerda
            raiz.dado=self.minimoValorNodo(raiz.direita)
            raiz.direita=self.excluirRecursivamente(raiz.direita,raiz.dado)
            return raiz
    
    
"""teste=ArvoreBinaria()
teste.inserir(15)
teste.inserir(16)
teste.inserir(17)
teste.inserir(18)
teste.inserir(19)
teste.procurar(17)"""

Arvore=arvoreBinaria()
while True:
    try:
        menu=int(input("Menu:\n1 - Inserir\n2 - Buscar\n3 - Excluir\n4 - Sair\n Digite o valor que deseja: "))
        if menu>4 or menu<1:
            print("O valor digitado não é válido.")
        else:
            if menu==1:
                numInserir=int(input("Digite o número que deseja inserir: "))
                Arvore.inserir(numInserir)
            elif menu==2:
                numBuscar=int(input("Digite o número que deseja Buscar: "))
                Arvore.procurar(numBuscar)
            elif menu==3:
                numExcluir=int(input("Digite o número que deseja excluir: "))
                Arvore.excluir(numExcluir)
            else:
                print("O programa finalizou.")
                break
            
    except ValueError:
        print("O valor digitado não é válido")
        