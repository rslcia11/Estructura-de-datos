# TRABAJO GRUPAL DE WILSON MARTINEZ Y FABIAN CAMPOVERDE 
import heapq
from typing import Dict, List, Tuple

def dijkstra(grafo: Dict[str, Dict[str, int]], inicio: str) -> Tuple[Dict[str, int], Dict[str, str]]:
    # Inicializar distancias y predecesores
    distancias = {nodo: float('infinity') for nodo in grafo}
    distancias[inicio] = 0
    predecesores = {nodo: None for nodo in grafo}
    
    # Cola de prioridad para seleccionar el nodo con la distancia mínima
    cola_prioridad = [(0, inicio)]
    
    while cola_prioridad:
        distancia_actual, nodo_actual = heapq.heappop(cola_prioridad)
        
        # Si ya encontramos una distancia más corta, ignoramos este camino
        if distancia_actual > distancias[nodo_actual]:
            continue
        
        # Explorar los vecinos del nodo actual
        for vecino, peso in grafo[nodo_actual].items():
            distancia = distancia_actual + peso
            
            # Si encontramos un camino más corto al vecino, actualizamos
            if distancia < distancias[vecino]:
                distancias[vecino] = distancia
                predecesores[vecino] = nodo_actual
                heapq.heappush(cola_prioridad, (distancia, vecino))
    
    return distancias, predecesores

def imprimir_camino(predecesores: Dict[str, str], inicio: str, fin: str) -> None:
    camino = []
    actual = fin
    while actual:
        camino.append(actual)
        actual = predecesores[actual]
    camino.reverse()
    
    print(f"Camino más corto de {inicio} a {fin}: {' -> '.join(camino)}")

# Caso de prueba
grafo = {
    'A': {'B': 4, 'C': 2},
    'B': {'A': 4, 'C': 1, 'D': 5},
    'C': {'A': 2, 'B': 1, 'D': 8, 'E': 10},
    'D': {'B': 5, 'C': 8, 'E': 2, 'F': 6},
    'E': {'C': 10, 'D': 2, 'F': 3},
    'F': {'D': 6, 'E': 3}
}

nodo_inicio = 'A'
distancias, predecesores = dijkstra(grafo, nodo_inicio)

print(f"Distancias más cortas desde el nodo {nodo_inicio}")
for nodo, distancia in distancias.items():
    print(f"A {nodo}: {distancia}")
    imprimir_camino(predecesores, nodo_inicio, nodo)
print()