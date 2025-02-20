import time
import random

class NodoAVL:
    def __init__(self, prioridad, paciente):
        self.prioridad = prioridad
        self.paciente = paciente
        self.izquierda = None
        self.derecha = None
        self.altura = 1

class ArbolAVL:
    def __init__(self):
        self.raiz = None

    def altura(self, nodo):
        if not nodo:
            return 0
        return nodo.altura

    def balance(self, nodo):
        if not nodo:
            return 0
        return self.altura(nodo.izquierda) - self.altura(nodo.derecha)

    def actualizar_altura(self, nodo):
        if not nodo:
            return
        nodo.altura = 1 + max(self.altura(nodo.izquierda), self.altura(nodo.derecha))

    def rotar_derecha(self, y):
        x = y.izquierda
        T2 = x.derecha
        x.derecha = y
        y.izquierda = T2
        self.actualizar_altura(y)
        self.actualizar_altura(x)
        return x

    def rotar_izquierda(self, x):
        y = x.derecha
        T2 = y.izquierda
        y.izquierda = x
        x.derecha = T2
        self.actualizar_altura(x)
        self.actualizar_altura(y)
        return y

    def insertar(self, prioridad, paciente):
        def _insertar(nodo, prioridad, paciente):
            if not nodo:
                return NodoAVL(prioridad, paciente)
            if prioridad < nodo.prioridad:
                nodo.izquierda = _insertar(nodo.izquierda, prioridad, paciente)
            else:
                nodo.derecha = _insertar(nodo.derecha, prioridad, paciente)

            self.actualizar_altura(nodo)
            balance = self.balance(nodo)

            if balance > 1:
                if prioridad < nodo.izquierda.prioridad:
                    return self.rotar_derecha(nodo)
                else:
                    nodo.izquierda = self.rotar_izquierda(nodo.izquierda)
                    return self.rotar_derecha(nodo)
            if balance < -1:
                if prioridad > nodo.derecha.prioridad:
                    return self.rotar_izquierda(nodo)
                else:
                    nodo.derecha = self.rotar_derecha(nodo.derecha)
                    return self.rotar_izquierda(nodo)
            return nodo

        self.raiz = _insertar(self.raiz, prioridad, paciente)

    def eliminar(self, prioridad):
        def _eliminar(nodo, prioridad):
            if not nodo:
                return nodo
            if prioridad < nodo.prioridad:
                nodo.izquierda = _eliminar(nodo.izquierda, prioridad)
            elif prioridad > nodo.prioridad:
                nodo.derecha = _eliminar(nodo.derecha, prioridad)
            else:
                if not nodo.izquierda:
                    return nodo.derecha
                elif not nodo.derecha:
                    return nodo.izquierda
                temp = self.obtener_nodo_valor_minimo(nodo.derecha)
                nodo.prioridad = temp.prioridad
                nodo.paciente = temp.paciente
                nodo.derecha = _eliminar(nodo.derecha, temp.prioridad)

            self.actualizar_altura(nodo)
            balance = self.balance(nodo)

            if balance > 1:
                if self.balance(nodo.izquierda) >= 0:
                    return self.rotar_derecha(nodo)
                else:
                    nodo.izquierda = self.rotar_izquierda(nodo.izquierda)
                    return self.rotar_derecha(nodo)
            if balance < -1:
                if self.balance(nodo.derecha) <= 0:
                    return self.rotar_izquierda(nodo)
                else:
                    nodo.derecha = self.rotar_derecha(nodo.derecha)
                    return self.rotar_izquierda(nodo)
            return nodo

        self.raiz = _eliminar(self.raiz, prioridad)

    def obtener_nodo_valor_minimo(self, nodo):
        actual = nodo
        while actual.izquierda:
            actual = actual.izquierda
        return actual

    def buscar(self, prioridad):
        def _buscar(nodo, prioridad):
            if not nodo or nodo.prioridad == prioridad:
                return nodo
            if prioridad < nodo.prioridad:
                return _buscar(nodo.izquierda, prioridad)
            return _buscar(nodo.derecha, prioridad)

        return _buscar(self.raiz, prioridad)

    def recorrido_inorden(self):
        def _inorden(nodo):
            if nodo:
                yield from _inorden(nodo.izquierda)
                yield (nodo.prioridad, nodo.paciente)
                yield from _inorden(nodo.derecha)

        return list(_inorden(self.raiz))

class ColaHospital:
    def __init__(self):
        self.arbol_avl = ArbolAVL()

    def agregar_paciente(self, prioridad, paciente):
        self.arbol_avl.insertar(prioridad, paciente)
        print(f"Paciente {paciente} agregado con prioridad {prioridad}")

    def eliminar_paciente(self, prioridad):
        nodo = self.arbol_avl.buscar(prioridad)
        if nodo:
            self.arbol_avl.eliminar(prioridad)
            print(f"Paciente {nodo.paciente} con prioridad {prioridad} eliminado")
        else:
            print(f"No se encontró paciente con prioridad {prioridad}")

    def obtener_siguiente_paciente(self):
        if self.arbol_avl.raiz:
            mayor_prioridad = self.arbol_avl.obtener_nodo_valor_minimo(self.arbol_avl.raiz)
            print(f"Siguiente paciente: {mayor_prioridad.paciente} (Prioridad: {mayor_prioridad.prioridad})")
            self.arbol_avl.eliminar(mayor_prioridad.prioridad)
        else:
            print("No hay pacientes en la cola")

    def mostrar_cola(self):
        cola = self.arbol_avl.recorrido_inorden()
        if cola:
            print("Cola actual (Prioridad: Paciente):")
            for prioridad, paciente in cola:
                print(f"{prioridad}: {paciente}")
        else:
            print("La cola está vacía")

def ejecutar_prueba_rendimiento(n):
    arbol_avl = ArbolAVL()
    lista_ordenada = []

    # Prueba Árbol AVL
    tiempo_inicio = time.time()
    for _ in range(n):
        prioridad = random.randint(1, 100)
        arbol_avl.insertar(prioridad, f"Paciente{_}")
    tiempo_insercion_avl = time.time() - tiempo_inicio

    tiempo_inicio = time.time()
    for _ in range(n):
        prioridad = random.randint(1, 100)
        arbol_avl.buscar(prioridad)
    tiempo_busqueda_avl = time.time() - tiempo_inicio

    # Prueba Lista Ordenada
    tiempo_inicio = time.time()
    for _ in range(n):
        prioridad = random.randint(1, 100)
        lista_ordenada.append((prioridad, f"Paciente{_}"))
        lista_ordenada.sort(key=lambda x: x[0])
    tiempo_insercion_lista = time.time() - tiempo_inicio

    tiempo_inicio = time.time()
    for _ in range(n):
        prioridad = random.randint(1, 100)
        next((x for x in lista_ordenada if x[0] == prioridad), None)
    tiempo_busqueda_lista = time.time() - tiempo_inicio

    print(f"\nResultados de la Prueba de Rendimiento (n={n}):")
    print(f"Árbol AVL - Inserción: {tiempo_insercion_avl:.6f}s, Búsqueda: {tiempo_busqueda_avl:.6f}s")
    print(f"Lista Ordenada - Inserción: {tiempo_insercion_lista:.6f}s, Búsqueda: {tiempo_busqueda_lista:.6f}s")

def main():
    cola_hospital = ColaHospital()

    while True:
        print("\n1. Agregar paciente")
        print("2. Eliminar paciente")
        print("3. Obtener siguiente paciente")
        print("4. Mostrar cola")
        print("5. Ejecutar prueba de rendimiento")
        print("6. Salir")

        opcion = input("Ingrese su opción: ")

        if opcion == '1':
            prioridad = int(input("Ingrese la prioridad del paciente: "))
            paciente = input("Ingrese el nombre del paciente: ")
            cola_hospital.agregar_paciente(prioridad, paciente)
        elif opcion == '2':
            prioridad = int(input("Ingrese la prioridad a eliminar: "))
            cola_hospital.eliminar_paciente(prioridad)
        elif opcion == '3':
            cola_hospital.obtener_siguiente_paciente()
        elif opcion == '4':
            cola_hospital.mostrar_cola()
        elif opcion == '5':
            n = int(input("Ingrese el número de operaciones para la prueba de rendimiento: "))
            ejecutar_prueba_rendimiento(n)
        elif opcion == '6':
            print("Saliendo del programa.")
            break
        else:
            print("Opción inválida. Por favor, intente de nuevo.")

if __name__ == "__main__":
    main()