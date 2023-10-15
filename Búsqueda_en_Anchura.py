from collections import deque

def buscar_en_anchura(grafo, inicio, objetivo):
    visitados = set()
    cola = deque([(inicio, [inicio])])

    while cola:
        nodo, camino = cola.popleft()
        if nodo == objetivo:
            return camino
        if nodo not in visitados:
            visitados.add(nodo)
            for vecino in grafo[nodo]:
                if vecino not in visitados:
                    cola.append((vecino, camino + [vecino]))

# Ejemplo de grafo no dirigido
grafo = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

inicio = 'A'
objetivo = 'F'

camino = buscar_en_anchura(grafo, inicio, objetivo)
print("Camino encontrado:", camino)

