class Item:
    def __init__(self, codigo, nome, quantidade,):
        self.codigo=codigo
        self.nome=nome
        self.quantidade=quantidade
        self.esquerda=None
        self.direita=None
class ArvoreProdutos:
    def __init__(self):
        self.raiz=None
    def inserir(self, codigo, nome, quantidade,):
        if self.buscar (codigo)is not None:
            print("Erro!! Produto já cadastrado")
            return
        novo_produto=Item(codigo, nome, quantidade,)
        print("Produto cadastrado com sucesso!")
        if self.raiz is None:
            self.raiz=novo_produto
            return
        atual=self.raiz
        while True:
            if codigo<atual.codigo:
                if atual.esquerda is None:
                    atual.esquerda=novo_produto
                    break
                atual=atual.esquerda
            else:
                if atual.direita is None:
                    atual.direita=novo_produto
                    break
                atual=atual.direita      
    def buscar(self, codigo):
        atual=self.raiz
        while atual is not None:
            if codigo==atual.codigo:
                return atual
            elif codigo<atual.codigo:
                atual=atual.esquerda
            else:
                atual=atual.direita
        return None
    def excluir(self, codigo):
        self.raiz=self.excluirRecursivo(self.raiz, codigo)
    def excluirRecursivo(self, no, codigo):
        if no is None:
            return no  
        if codigo<no.codigo:
            no.esquerda=self.excluirRecursivo(no.esquerda, codigo)
        elif codigo>no.codigo:
            no.direita=self.excluirRecursivo(no.direita, codigo)
        else:
            if no.esquerda is None:
                return no.direita
            elif no.direita is None:
                return no.esquerda  
            temp=self.encontrarMinimo(no.direita)
            no.codigo=temp.codigo
            no.nome=temp.nome
            no.quantidade=temp.quantidade
            no.direita=self.excluirRecursivo(no.direita, temp.codigo)
        return no
    def encontrarMinimo(self, no):
        atual=no
        while atual.esquerda is not None:
            atual=atual.esquerda
        return atual
    def ordenarPorNome(self, produto):
        return produto.nome
    def emOrdem(self, no, produtos):
        if no is not None:
            self.emOrdem(no.esquerda, produtos)
            produtos.append(no)
            self.emOrdem(no.direita, produtos)
    def exibirOrdemAlfabetica(self):
        produtos=[]
        self.emOrdem(self.raiz, produtos)
        produtos.sort(key=self.ordenarPorNome)
        return produtos
    def exibirOrdemInversa(self):
        produtos=[]
        self.emOrdem(self.raiz, produtos)
        produtos.sort(key=self.ordenarPorNome, reverse=True)
        return produtos 
    def em_ordem(self):
        self._em_ordem_recursivo(self.raiz)

    def _em_ordem_recursivo(self, no_atual):
        if no_atual:
            self._em_ordem_recursivo(no_atual.esquerda)
            print(no_atual.codigo, no_atual.nome, no_atual.quantidade)
            self._em_ordem_recursivo(no_atual.direita)
    def exibir_ordem_alfabetica(self):
        produtos = []
        self.emOrdem(self.raiz, produtos)
        produtos.sort(key=self.ordenar_por_nome)
        return produtos
    def exibirHierarquiaRecursivo(self, no, nivel):
        if no is None:
            return ""
        resultado="  " * nivel + f"Código: {no.codigo}, Nome: {no.nome}\n"
        resultado+=self.exibirHierarquiaRecursivo(no.esquerda, nivel + 1)
        resultado+=self.exibirHierarquiaRecursivo(no.direita, nivel + 1)
        return resultado
    def preOrdem(self):
        produtos=[]
        self.preOrdemRecursivo(self.raiz, produtos)
        return produtos
    def preOrdemRecursivo(self, no, produtos):
        if no is not None:
            produtos.append(no)
            self.preOrdemRecursivo(no.esquerda, produtos)
            self.preOrdemRecursivo(no.direita, produtos)
    def posOrdem(self):
        produtos=[]
        self.posOrdemRecursivo(self.raiz, produtos)
        return produtos
    def posOrdemRecursivo(self, no, produtos):
        if no is not None:
            self.posOrdemRecursivo(no.esquerda, produtos)
            self.posOrdemRecursivo(no.direita, produtos)
            produtos.append(no)
def menu():
    print("Menu:\n1-Cadastrar Produto\n2-Remover Produto\n3-Buscar Produto\n4-Percorrer a Árvore\n5-Atualizar quantidade\n6-Relatório Geral\n7-sair\nDigite o item que deseja: ")
    return input("Escolha uma opção: ")
def main():
    armazem=ArvoreProdutos()
    while True:
        try:
                opcao=menu()
                if opcao=="1":
                    codigo=int(input("Digite o código do produto: "))
                    nome=input("Digite o nome do produto: ")
                    quantidade=int(input("Digite a quantidade: "))
                    armazem.inserir(codigo, nome, quantidade)
                elif opcao=="2":
                    codigo=int(input("Digite o código do produto a ser removido: "))
                    armazem.excluir(codigo)
                    print("Produto removido com sucesso!")
                elif opcao=="3":
                    codigo=int(input("Digite o código do produto: "))
                    produto=armazem.buscar(codigo)
                    if produto:
                        print(f"\nProduto encontrado:")
                        print(f"Código: {produto.codigo}")
                        print(f"Nome: {produto.nome}")
                        print(f"Quantidade: {produto.quantidade}")
                    else:
                        print("Produto não encontrado!")   
                elif opcao=="4":
                    print("\nQual tipo de percurso:")
                    print("1. Pré-ordem")
                    print("2. Em-ordem")
                    print("3. Pós-ordem")
                    sub_opcao=input("Escolha uma opção: ")
                    if sub_opcao=="1":
                        produtos=armazem.preOrdem()
                        print("\nPercurso em Pré-ordem:")
                        for p in produtos:
                            print(f"Código: {p.codigo} - Nome: {p.nome} - Qtd: {p.quantidade}")
                    elif sub_opcao=="2":
                        produtos=armazem.em_ordem()
                    elif sub_opcao=="3":
                        produtos=armazem.posOrdem()
                        print("\nPercurso em Pós-ordem:")
                        for p in produtos:
                            print(f"Código: {p.codigo} - Nome: {p.nome} - Qtd: {p.quantidade}")
                    else:
                        print("Opção inválida!")  
                elif opcao=="5":
                    codigo=int(input("Digite o código do produto: "))
                    produto=armazem.buscar(codigo)
                    if produto:
                        nova_qtd=int(input("Digite a nova quantidade: "))
                        produto.quantidade=nova_qtd
                        print("Quantidade atualizada com sucesso!")
                    else:
                        print("Produto não encontrado!")
                elif opcao=="6":
                    print("\nRelatório Geral")
                    produtos=armazem.exibirOrdemAlfabetica()
                    valor_total=0
                    print("\nProdutos em estoque:")
                    for p in produtos:
                        print(f"Código: {p.codigo} | Nome: {p.nome} | Qtd: {p.quantidade}")
                elif opcao=="7":
                    print("Programa encerrado")
                    break  
                else:
                    print("Opção inválida!")
        except ValueError:
            print("Erro: valor inválido!")

main()