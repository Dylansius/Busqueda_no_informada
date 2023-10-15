def buscar_bidireccional(grafo, inicio, objetivo):
    visitados_inicio = set()
    visitados_objetivo = set()
    cola_inicio = [inicio]
    cola_objetivo = [objetivo]

    while cola_inicio and cola_objetivo:
        if len(cola_inicio) <= len(cola_objetivo):
            actual = cola_inicio.pop(0)
            if actual in visitados_objetivo:
                return actual
            visitados_inicio.add(actual)
            for vecino in grafo[actual]:
                if vecino not in visitados_inicio:
                    cola_inicio.append(vecino)
        else:
            actual = cola_objetivo.pop(0)
            if actual in visitados_inicio:
                return actual
            visitados_objetivo.add(actual)
            for vecino in grafo[actual]:
                if vecino not in visitados_objetivo:
                    cola_objetivo.append(vecino)

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

punto_encuentro = buscar_bidireccional(grafo, inicio, objetivo)
if punto_encuentro:
    print("Punto de encuentro:", punto_encuentro)
else:
    print("No se encontro un punto de encuentro.")

