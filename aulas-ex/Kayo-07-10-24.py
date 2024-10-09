
class NodoLista:
    def __init__(self,dado,proximno_nodo=None):
        self.dado=dado
        self.proximo= proximno_nodo
    def __repr__(self):
        return '%s -> %s' % (self.dado, self.proximo)
    
class ListaEncadeada:
    def __init__(self):
        self.cabeca=None
    def __repr__(self):
        return "["+str(self.cabeca)+"]"

def inserir_elementos(Lista, novo_dado):
    novo_nodo=NodoLista(novo_dado) #cria um novo nodo com o dado a ser armazenado.
    novo_nodo.proximo=Lista.cabeca #Faz com que o novo seja ca cabeça da Lista
    Lista.cabeca=novo_nodo #Faz com que a cabeça da lista referencie novo nodo.
    
def remover(self, valor):
    if self.cabeca.valor==valor:
          self.cabeca=self.cabeca.proximo
    else:
         corrente=self.cabeca
         anterior=None
         while corrente and corrente.dado!=valor:
              anterior=corrente
              corrente=corrente.proximo
         if corrente:
              anterior.proximo=corrente.proximo
         else:
              anterior.proximo=None


def main1():
    lista= ListaEncadeada()
    print("Lista vazia:",lista)
    inserir_elementos(lista,5)
    print("Lista contém único elemento:", lista)
    inserir_elementos(lista,10)
    print("Inserindo um novo elemento:",lista)
    inserir_elementos(lista,29)
    print("Inserindo um novo elemento:",lista)
    

main1()
remover(30)
        
