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

camino = buscar_en_profundidad(grafo, inicio, objetivo)
print("Camino encontrado:", camino)

