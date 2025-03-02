import heapq
import matplotlib.pyplot as plt
import networkx as nx
import random
import time

class Grafo:
    def __init__(self, dirigido=False):
        self.grafo = {}
        self.dirigido = dirigido

    def agregar_nodo(self, nodo):
        if nodo not in self.grafo:
            self.grafo[nodo] = {}

    def agregar_arista(self, desde_nodo, hasta_nodo, peso):
        self.agregar_nodo(desde_nodo)
        self.agregar_nodo(hasta_nodo)
        self.grafo[desde_nodo][hasta_nodo] = peso
        if not self.dirigido:
            self.grafo[hasta_nodo][desde_nodo] = peso

    def obtener_vecinos(self, nodo):
        return list(self.grafo[nodo].keys())

    def obtener_peso(self, desde_nodo, hasta_nodo):
        return self.grafo[desde_nodo][hasta_nodo]

def distancia_euclidiana(a, b):
    return ((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2) ** 0.5

class HeuristicaAdaptativa:
    def __init__(self, heuristica_base):
        self.heuristica_base = heuristica_base
        self.correcciones = {}
        self.tasa_aprendizaje = 0.1

    def __call__(self, a, b):
        clave = (a, b)
        estimacion_base = self.heuristica_base(a, b)
        correccion = self.correcciones.get(clave, 1.0)
        return estimacion_base * correccion

    def actualizar(self, a, b, costo_real):
        clave = (a, b)
        costo_estimado = self(a, b)
        error = costo_real - costo_estimado
        self.correcciones[clave] = self.correcciones.get(clave, 1.0) + self.tasa_aprendizaje * error / costo_estimado

class AprendizajeQ:
    def __init__(self, grafo):
        self.valores_q = {}
        self.tasa_aprendizaje = 0.1
        self.factor_descuento = 0.9
        self.grafo = grafo

    def obtener_valor_q(self, estado, accion):
        return self.valores_q.get((estado, accion), 0.0)

    def actualizar(self, estado, accion, recompensa, siguiente_estado):
        q_actual = self.obtener_valor_q(estado, accion)
        max_siguiente_q = max([self.obtener_valor_q(siguiente_estado, siguiente_accion) for siguiente_accion in self.grafo.obtener_vecinos(siguiente_estado)])
        nuevo_q = q_actual + self.tasa_aprendizaje * (recompensa + self.factor_descuento * max_siguiente_q - q_actual)
        self.valores_q[(estado, accion)] = nuevo_q

def a_estrella(grafo, inicio, meta, h, aprendizaje_q=None):
    conjunto_abierto = []
    heapq.heappush(conjunto_abierto, (0, inicio))
    vino_de = {}
    puntaje_g = {inicio: 0}
    puntaje_f = {inicio: h(inicio, meta)}

    while conjunto_abierto:
        actual = heapq.heappop(conjunto_abierto)[1]

        if actual == meta:
            camino = []
            while actual in vino_de:
                camino.append(actual)
                actual = vino_de[actual]
            camino.append(inicio)
            return camino[::-1]

        for vecino in grafo.obtener_vecinos(actual):
            puntaje_g_tentativo = puntaje_g[actual] + grafo.obtener_peso(actual, vecino)

            if vecino not in puntaje_g or puntaje_g_tentativo < puntaje_g[vecino]:
                vino_de[vecino] = actual
                puntaje_g[vecino] = puntaje_g_tentativo
                puntaje_f[vecino] = puntaje_g[vecino] + h(vecino, meta)
                
                if aprendizaje_q:
                    valor_q = aprendizaje_q.obtener_valor_q(actual, vecino)
                    puntaje_f[vecino] += valor_q
                
                heapq.heappush(conjunto_abierto, (puntaje_f[vecino], vecino))

    return None

def crear_grafo_ciudades(num_ciudades=10, distancia_maxima=100):
    grafo = Grafo()
    ciudades = [(random.randint(0, distancia_maxima), random.randint(0, distancia_maxima)) for _ in range(num_ciudades)]
    
    for i, ciudad in enumerate(ciudades):
        grafo.agregar_nodo(ciudad)
        for j, otra_ciudad in enumerate(ciudades):
            if i != j:
                distancia = distancia_euclidiana(ciudad, otra_ciudad)
                if distancia < distancia_maxima / 2:  # Conectar solo ciudades cercanas
                    grafo.agregar_arista(ciudad, otra_ciudad, distancia)
    
    return grafo, ciudades

def visualizar_grafo(grafo, camino=None):
    G = nx.Graph()
    for nodo in grafo.grafo:
        G.add_node(nodo)
        for vecino, peso in grafo.grafo[nodo].items():
            G.add_edge(nodo, vecino, weight=peso)

    pos = {nodo: nodo for nodo in G.nodes()}
    nx.draw(G, pos, with_labels=False, node_color='lightblue', node_size=500)
    
    if camino:
        aristas_camino = list(zip(camino, camino[1:]))
        nx.draw_networkx_edges(G, pos, edgelist=aristas_camino, edge_color='r', width=2)

    nx.draw_networkx_labels(G, pos, {nodo: f"{nodo}" for nodo in G.nodes()})
    etiquetas_aristas = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=etiquetas_aristas)

    plt.title("Mapa de Ciudades con Ruta Óptima")
    plt.axis('off')
    plt.show()

# Crear el grafo de ciudades
grafo_ciudades, ciudades = crear_grafo_ciudades(num_ciudades=15)

# Inicializar la heurística adaptativa y aprendizaje Q
heuristica_adaptativa = HeuristicaAdaptativa(distancia_euclidiana)
aprendizaje_q = AprendizajeQ(grafo_ciudades)

# Ejecutar múltiples búsquedas para entrenar la heurística y aprendizaje Q
num_iteraciones = 50
for i in range(num_iteraciones):
    inicio = random.choice(ciudades)
    meta = random.choice(ciudades)
    while meta == inicio:
        meta = random.choice(ciudades)

    # A* estándar
    tiempo_inicio = time.time()
    camino_estandar = a_estrella(grafo_ciudades, inicio, meta, distancia_euclidiana)
    tiempo_estandar = time.time() - tiempo_inicio

    # A* con heurística adaptativa y aprendizaje Q
    tiempo_inicio = time.time()
    camino_optimizado = a_estrella(grafo_ciudades, inicio, meta, heuristica_adaptativa, aprendizaje_q)
    tiempo_optimizado = time.time() - tiempo_inicio

    # Actualizar heurística adaptativa y aprendizaje Q
    if camino_optimizado:
        for j in range(len(camino_optimizado) - 1):
            a, b = camino_optimizado[j], camino_optimizado[j+1]
            costo_real = grafo_ciudades.obtener_peso(a, b)
            heuristica_adaptativa.actualizar(a, b, costo_real)
            aprendizaje_q.actualizar(a, b, -costo_real, b)  # Usamos el costo negativo como recompensa

    print(f"Iteración {i + 1}:")
    print(f"  Tiempo A* estándar: {tiempo_estandar:.6f} segundos")
    print(f"  Tiempo A* optimizado: {tiempo_optimizado:.6f} segundos")
    print(f"  Mejora: {(tiempo_estandar - tiempo_optimizado) / tiempo_estandar * 100:.2f}%")

# Visualizar el resultado final
inicio = random.choice(ciudades)
meta = random.choice(ciudades)
while meta == inicio:
    meta = random.choice(ciudades)

camino_optimizado = a_estrella(grafo_ciudades, inicio, meta, heuristica_adaptativa, aprendizaje_q)
visualizar_grafo(grafo_ciudades, camino_optimizado)

print(f"\nRuta óptima final de {inicio} a {meta}:")
print(" -> ".join(str(ciudad) for ciudad in camino_optimizado))