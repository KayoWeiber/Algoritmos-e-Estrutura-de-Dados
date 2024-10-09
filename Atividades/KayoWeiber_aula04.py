class Nodo:
    def __init__(self, dado, proximo=None):
        self.dado=dado
        self.proximo=proximo
class ListaEncadeada:
    def __init__(self):
        self.cabeca=None
    def insere(self, valor):
        novo_nodo=Nodo(valor)
        novo_nodo.proximo=self.cabeca
        self.cabeca=novo_nodo
    def imprime(self):
        corrente=self.cabeca
        while corrente:
            print(corrente.dado)
            corrente=corrente.proximo
    def buscar(self, valor):
        corrente=self.cabeca
        sts=False
        while corrente:
            if corrente.dado==valor:
                print(f"Valor encontrado: {valor}")
                sts=True
                break  
            corrente=corrente.proximo
        if not sts:
            print("Valor NÃO encontrado")
    def remover(self, valor):
        corrente=self.cabeca
        anterior=None
        if corrente and corrente.dado==valor:
            self.cabeca=corrente.proximo  
            print(f"Valor {valor} removido!")
            return
        while corrente and corrente.dado!=valor:
            anterior=corrente
            corrente=corrente.proximo
        if corrente:
            anterior.proximo=corrente.proximo  
            print(f"Valor {valor} removido!")
        else:
            print(f"Valor {valor} não encontrado para remover!")
    def alterar(self, valor):
        corrente=self.cabeca
        sts=False
        while corrente:
            if corrente.dado==valor:
                try:
                    novo_valor=int(input("Digite o novo valor a ser adicionado: "))
                    corrente.dado=novo_valor
                    print(f"Valor {valor} alterado para {novo_valor}")
                    sts=True
                except ValueError:
                    print("Por favor, insira um número válido.")
                break  
            corrente=corrente.proximo
        if not sts:
            print("Valor NÃO encontrado")
lista=ListaEncadeada()
while True:
    try:
        menu_principal=int(input("Menu:\n1-Inserir Valor\n2-Imprimir Valores\n3-Buscar valor\n4-Remover\n5-Alterar Valor\n6-Sair do Programa\nDigite a opção desejada: "))
        if menu_principal<1 or menu_principal>6:
            print("O Valor digitado não é válido")
        else:
            if menu_principal==1:
                while True:
                    try:
                        menu_inserir=int(input("menu\n 1-adionar valores\n2-sair"))
                        if menu_inserir<1 or menu_inserir>2:
                            print("O valor digitado não é válido")
                        else:
                            if menu_inserir==1:
                                valor_add=int(input("Digite o valor a ser adicionado: "))
                                lista.Insere(valor_add)
                                print(f"O valor {valor_add} foi adicionado com sucesso")
                            else:
                                break
                    except ValueError:
                        print("Digite o valor válido.")
    
    except ValueError:
        print("Valor digitado não é válido.")