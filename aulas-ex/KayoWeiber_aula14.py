'''

class GrafoDirecionado:

    def __init__(self):
        self.adjacencia={}

    def adicionar_vertice(self,vertice):
        if vertice not in self.adjacencia:
            self.adjacencia[vertice]=[]

    def adicionar_aresta(self,origem,destino):
        if origem in self.adjacencia and destino in self.adjacencia:
            self.adjacencia[origem].append(destino)

    def exibir_grafo(self):
        for vertice,vizinhos in self.adjacencia.items():
            print(f"{vertice} -> {','.join(vizinhos)}")

grafo= GrafoDirecionado() #criando grafo

vertices=["v0","v1","V2","v3","v4"] #adicionando vertices

for v in vertices:
    grafo.adicionar_vertice(v)


#adicionando arestas
grafo.adicionar_aresta("v0","v1") #e0
grafo.adicionar_aresta("v0","v3") #e3
grafo.adicionar_aresta("v1","v0") #e6
grafo.adicionar_aresta("v1","v2") #e1
grafo.adicionar_aresta("v2","v3") #e2
grafo.adicionar_aresta("v2","v4") #e4
grafo.adicionar_aresta("v3","v4") #e5



#exibindo o grafo
grafo.exibir_grafo()
'''
class GrafoDirecionado:

    def __init__(self):
        self.adjacencia={}

    def adicionar_vertice(self,vertice):
        if vertice not in self.adjacencia:
            self.adjacencia[vertice]=[]

    def adicionar_aresta(self,vertice1,vertice2):
        if vertice1 in self.adjacencia and vertice2 in self.adjacencia:
            self.adjacencia[vertice1].append(vertice2)
            self.adjacencia[vertice2].append(vertice1)

    def exibir_grafo(self):
        for vertice,vizinhos in self.adjacencia.items():
            print(f"{vertice} -> {','.join(vizinhos)}")

grafo= GrafoDirecionado() #criando grafo

vertices=["v0","v1","V2","v3","v4"] #adicionando vertices

for v in vertices:
    grafo.adicionar_vertice(v)


#adicionando arestas
grafo.adicionar_aresta("v0","v1") #e0
grafo.adicionar_aresta("v0","v3") #e3
grafo.adicionar_aresta("v1","v0") #e6
grafo.adicionar_aresta("v1","v2") #e1
grafo.adicionar_aresta("v2","v3") #e2
grafo.adicionar_aresta("v2","v4") #e4
grafo.adicionar_aresta("v3","v4") #e5



#exibindo o grafo
grafo.exibir_grafo()