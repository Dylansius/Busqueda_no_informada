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
profundidad_maxima = 3

camino = buscar_en_profundidad_limitada(grafo, inicio, objetivo, profundidad_maxima)
if camino:
    print("Camino encontrado:", camino)
else:
    print("No se encontro un camino dentro de la profundidad maxima.")

