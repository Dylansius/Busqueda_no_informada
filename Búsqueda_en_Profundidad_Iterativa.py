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
