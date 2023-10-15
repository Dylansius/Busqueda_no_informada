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

def buscar_en_profundidad(grafo, nodo, objetivo, visitados=None):
    if visitados is None:
        visitados = set()
    visitados.add(nodo)

    if nodo == objetivo:
        return [nodo]

    for vecino in grafo[nodo]:
        if vecino not in visitados:
            camino = buscar_en_profundidad(grafo, vecino, objetivo, visitados)
            if camino:
                return [nodo] + camino

    return []

def buscar_en_profundidad_limitada(grafo, nodo, objetivo, profundidad, visitados=None):
    if profundidad < 0:
        return None

    if visitados is None:
        visitados = set()

    visitados.add(nodo)

    if nodo == objetivo:
        return [nodo]

    for vecino in grafo[nodo]:
        if vecino not in visitados:
            camino = buscar_en_profundidad_limitada(grafo, vecino, objetivo, profundidad - 1, visitados)
            if camino:
                return [nodo] + camino

    return None

def buscar_en_grafos(grafo, inicio, objetivo, estrategia):
    if estrategia == "anchura":
        return buscar_en_anchura(grafo, inicio, objetivo)
    elif estrategia == "profundidad":
        return buscar_en_profundidad(grafo, inicio, objetivo)
    elif estrategia == "profundidad_limitada":
        return buscar_en_profundidad_limitada(grafo, inicio, objetivo, profundidad_maxima)
    else:
        return None

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
estrategia = "profundidad"

camino = buscar_en_grafos(grafo, inicio, objetivo, estrategia)
if camino:
    print("Camino encontrado:", camino)
else:
    print("No se encontro un camino.")
