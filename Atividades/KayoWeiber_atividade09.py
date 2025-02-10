class GrafoMapaCidade:
    def __init__(self):
        self.adjacencia = {}

    def adicionar_locais(self, local):
        if local not in self.adjacencia:
            self.adjacencia[local] = []

    def adicionar_cruzamento(self, origem, destino):
        if origem in self.adjacencia and destino in self.adjacencia:
            self.adjacencia[origem].append(destino)
            self.adjacencia[destino].append(origem)  

    def exibir_grafo(self):
        for local, vizinhos in self.adjacencia.items():
            print(f"{local} -> {', '.join(vizinhos)}")
        print("")

    def buscar_profundidade(self, inicio, visitados=None):
        if visitados is None:
            visitados = set()
        visitados.add(inicio)
        print(inicio, end=" ")
        for vizinho in self.adjacencia[inicio]:
            if vizinho not in visitados:
                self.buscar_profundidade(vizinho, visitados)

    def busca_largura(self, inicio):
        visitado = set()
        fila = [inicio]
        visitado.add(inicio)
        while fila:
            vertice = fila.pop(0)
            print(vertice, end=" ")
            for vizinho in self.adjacencia[vertice]:
                if vizinho not in visitado:
                    visitado.add(vizinho)
                    fila.append(vizinho)

    def encontrar_caminho_bfs(self, inicio, destino):
        
        if inicio not in self.adjacencia or destino not in self.adjacencia:
            return None

        fila = [(inicio, [inicio])]
        visitado = set()

        while fila:
            vertice, caminho = fila.pop(0)
            if vertice == destino:
                return caminho

            for vizinho in self.adjacencia[vertice]:
                if vizinho not in visitado:
                    visitado.add(vizinho)
                    fila.append((vizinho, caminho + [vizinho]))
        return None  

    def contar_regioes_desconectadas(self):
        visitados = set()
        regioes = 0
        for local in self.adjacencia:
            if local not in visitados:
                self.buscar_profundidade(local, visitados)
                regioes += 1
        return regioes



mapa = GrafoMapaCidade()
ruas = [
    "R. Anacleto Felicio do Carmo", "R. Zico Lopes", "R. Tupaciguara",
    "R. Dr. Sandoval Henrique de Sá", "R. Araguari", "R. Patrocinio", "R. João Januário"
]

for rua in ruas:
    mapa.adicionar_locais(rua)

def adicionar_ligacoes():
    cruzamentos = [
        ("R. Zico Lopes", "R. João Januário"), ("R. Zico Lopes", "R. Dr. Sandoval Henrique de Sá"),
        ("R. Zico Lopes", "R. Tupaciguara"), ("R. Zico Lopes", "R. Araguari"),
        ("R. Anacleto Felicio do Carmo", "R. João Januário"), ("R. Anacleto Felicio do Carmo", "R. Dr. Sandoval Henrique de Sá"),
        ("R. Anacleto Felicio do Carmo", "R. Tupaciguara"), ("R. Anacleto Felicio do Carmo", "R. Araguari"),
        ("R. Patrocinio", "R. João Januário"), ("R. Patrocinio", "R. Dr. Sandoval Henrique de Sá"),
        ("R. Patrocinio", "R. Tupaciguara"), ("R. Patrocinio", "R. Araguari"),
        ("R. João Januário", "R. Anacleto Felicio do Carmo"), ("R. Dr. Sandoval Henrique de Sá", "R. Anacleto Felicio do Carmo"),
        ("R. Tupaciguara", "R. Anacleto Felicio do Carmo"), ("R. Araguari", "R. Anacleto Felicio do Carmo"),
        ("R. João Januário", "R. Patrocinio"), ("R. Dr. Sandoval Henrique de Sá", "R. Patrocinio"),
        ("R. Tupaciguara", "R. Patrocinio"), ("R. Araguari", "R. Patrocinio")
    ]

    for origem, destino in cruzamentos:
        mapa.adicionar_cruzamento(origem, destino)

adicionar_ligacoes()

print("Mapa da Cidade (Grafo):")
mapa.exibir_grafo()

print("Busca em Profundidade (DFS) a partir de 'R. João Januário':")
mapa.buscar_profundidade("R. João Januário")
print("\n")

print("Busca em Largura (BFS) a partir de 'R. João Januário':")
mapa.busca_largura("R. João Januário")
print("\n")

inicio = "R. João Januário"
destino = "R. Araguari"
caminho = mapa.encontrar_caminho_bfs(inicio, destino)
if caminho:
    print(f"Menor caminho de '{inicio}' até '{destino}': {caminho}")
else:
    print(f"Não há caminho entre '{inicio}' e '{destino}'.")

print(f"\nNúmero de regiões desconectadas na cidade: {mapa.contar_regioes_desconectadas()}")
