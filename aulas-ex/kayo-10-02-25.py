import heapq
class Grafo:

    def __init__(self):
        self.adjacencia={}
    
    def adiciona_aresta(self, u, v, peso):
        if u not in self.adjacencia:
            self.adjacencia[u]=[]
        if v not in self.adjacencia:
            self.adjacencia[v]=[]
        
        self.adjacencia[u].append((v,peso))
        self.adjacencia[v].append((u,peso))

    """def exibirGrafo(self):
        for u,i in self.adjacencia.items():
            print(f'{u} -> {", ".join(i)}')"""
    def dijkstra(self, origem):
        
        distancias = {vertice:float('inf') for vertice in self.adjacencia}
        distancias [origem]=0
        caminho = {vertice:None for vertice in self.adjacencia}
        fila_prioridade = [(0, origem)]

        while fila_prioridade:
            dist_atual,vertice_atual = heapq.heappop(fila_prioridade)

            if dist_atual > distancias[vertice_atual]:
                continue
            for vizinho, peso in self.adjacencia[vertice_atual]:
                distancia = dist_atual + peso
                if distancia < distancias[vizinho]:
                    distancias[vizinho] = distancia
                    caminho[vizinho] = vertice_atual
                    heapq.heappush(fila_prioridade,(distancia,vizinho))


mapa=Grafo()

mapa.adiciona_aresta('Planura','Colombia',10)
mapa.adiciona_aresta('Planura','Frutal',27)
mapa.adiciona_aresta('Planura','Pirajuba',29)
mapa.adiciona_aresta('Colombia','Barretos',48)
mapa.adiciona_aresta('Colombia','Planura',10)
mapa.adiciona_aresta('Frutal','Planura',27)
mapa.adiciona_aresta('Frutal','Fronteira',47)

'''
mapa.exibirGrafo()
'''