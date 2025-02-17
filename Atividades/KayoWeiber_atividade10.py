import heapq

class Grafo:
    def __init__(self): 
        self.vertices = {}
    
    def adicionar_aresta(self, u, v, peso):
        if u not in self.vertices:
            self.vertices[u] = []
        if v not in self.vertices:
            self.vertices[v] = []
        self.vertices[u].append((v, peso))
    
        if u != v: 
            self.vertices[v].append((u, peso))

    def dijkstra(self, inicio):
        distancias = {v: float('inf') for v in self.vertices}
        distancias[inicio] = 0
        pq = [(0, inicio)]
        
        while pq:
            dist_atual, vertice = heapq.heappop(pq)
            if dist_atual > distancias[vertice]:
                continue
            if vertice not in self.vertices: 
                continue
            for vizinho, peso in self.vertices[vertice]:
                distancia = dist_atual + peso
                if distancia < distancias[vizinho]:
                    distancias[vizinho] = distancia
                    heapq.heappush(pq, (distancia, vizinho))
        
        return distancias
    
    def prim(self):
        mst = []
        visitados = set()
        arestas = []
        
        if not self.vertices:
            return mst
        
        inicio = next(iter(self.vertices))
        visitados.add(inicio)
        if inicio not in self.vertices:
            return mst
        for v, peso in self.vertices[inicio]:
            heapq.heappush(arestas, (peso, inicio, v))
        
        while arestas:
            peso, u, v = heapq.heappop(arestas)
            if v not in visitados:
                visitados.add(v)
                mst.append((u, v, peso))
                if v not in self.vertices:
                    continue
                for vizinho, peso in self.vertices[v]:
                    if vizinho not in visitados:
                        heapq.heappush(arestas, (peso, v, vizinho))
        
        return mst
    
    def kruskal(self):
        arestas = []
        for u in self.vertices:
            for v, peso in self.vertices[u]:
                arestas.append((peso, u, v))
        
        arestas_unicas = set()
        arestas_filtradas = []
        for peso, u, v in arestas:
            if (u, v) not in arestas_unicas and (v, u) not in arestas_unicas:
                arestas_unicas.add((u, v))
                arestas_filtradas.append((peso, u, v))
                
        arestas_filtradas = sorted(arestas_filtradas)
        
        pai = {v: v for v in self.vertices}
        
        def find(v):
            if pai[v] != v:
                pai[v] = find(pai[v])
            return pai[v]
        
        def union(v1, v2):
            raiz1 = find(v1)
            raiz2 = find(v2)
            if raiz1 != raiz2:
                pai[raiz2] = raiz1
        
        mst = []
        for peso, u, v in arestas_filtradas:
            if find(u) != find(v):
                union(u, v)
                mst.append((u, v, peso))
        
        return mst

grafo = Grafo()
grafo.adicionar_aresta('A', 'B', 1)
grafo.adicionar_aresta('A', 'C', 3)
grafo.adicionar_aresta('B', 'C', 1)
grafo.adicionar_aresta('B', 'D', 4)
grafo.adicionar_aresta('C', 'D', 1)

distancias_dijkstra = grafo.dijkstra('A')
mst_prim = grafo.prim()
mst_kruskal = grafo.kruskal()

print("Dijkstra:", distancias_dijkstra)
print("Prim:", mst_prim)
print("Kruskal:",mst_kruskal)
