import heapq

def buscar_en_anchura_costo_uniforme(grafo, inicio, objetivo):
    cola_prioridad = [(0, inicio)]
    visitados = set()

    while cola_prioridad:
        costo, nodo = heapq.heappop(cola_prioridad)

        if nodo in visitados:
            continue

        visitados.add(nodo)

        if nodo == objetivo:
            return costo

        for vecino, costo_vecino in grafo[nodo].items():
            if vecino not in visitados:
                nuevo_costo = costo + costo_vecino
                heapq.heappush(cola_prioridad, (nuevo_costo, vecino))

# Ejemplo de grafo ponderado
grafo = {
    'A': {'B': 1, 'C': 3},
    'B': {'A': 1, 'D': 2, 'E': 4},
    'C': {'A': 3, 'F': 2},
    'D': {'B': 2},
    'E': {'B': 4, 'F': 1},
    'F': {'C': 2, 'E': 1}
}

inicio = 'A'
objetivo = 'F'

costo_minimo = buscar_en_anchura_costo_uniforme(grafo, inicio, objetivo)
print("Costo mínimo:", costo_minimo)

