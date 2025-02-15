import time
import random
import string

class Producto:
    def __init__(self, codigo, nombre, precio):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio

class NodoBST:
    def __init__(self, producto):
        self.producto = producto
        self.izquierda = None
        self.derecha = None

class ArbolBST:
    def __init__(self):
        self.raiz = None

    def insertar(self, producto):
        if not self.raiz:
            self.raiz = NodoBST(producto)
        else:
            self._insertar_recursivo(self.raiz, producto)

    def _insertar_recursivo(self, nodo, producto):
        if producto.codigo < nodo.producto.codigo:
            if nodo.izquierda is None:
                nodo.izquierda = NodoBST(producto)
            else:
                self._insertar_recursivo(nodo.izquierda, producto)
        else:
            if nodo.derecha is None:
                nodo.derecha = NodoBST(producto)
            else:
                self._insertar_recursivo(nodo.derecha, producto)

    def buscar(self, codigo):
        return self._buscar_recursivo(self.raiz, codigo)

    def _buscar_recursivo(self, nodo, codigo):
        if nodo is None or nodo.producto.codigo == codigo:
            return nodo
        if codigo < nodo.producto.codigo:
            return self._buscar_recursivo(nodo.izquierda, codigo)
        return self._buscar_recursivo(nodo.derecha, codigo)

    def eliminar(self, codigo):
        self.raiz = self._eliminar_recursivo(self.raiz, codigo)

    def _eliminar_recursivo(self, nodo, codigo):
        if nodo is None:
            return nodo
        if codigo < nodo.producto.codigo:
            nodo.izquierda = self._eliminar_recursivo(nodo.izquierda, codigo)
        elif codigo > nodo.producto.codigo:
            nodo.derecha = self._eliminar_recursivo(nodo.derecha, codigo)
        else:
            if nodo.izquierda is None:
                return nodo.derecha
            elif nodo.derecha is None:
                return nodo.izquierda
            temp = self._encontrar_minimo(nodo.derecha)
            nodo.producto = temp.producto
            nodo.derecha = self._eliminar_recursivo(nodo.derecha, temp.producto.codigo)
        return nodo

    def _encontrar_minimo(self, nodo):
        actual = nodo
        while actual.izquierda is not None:
            actual = actual.izquierda
        return actual

class SistemaInventario:
    def __init__(self):
        self.arbol = ArbolBST()
        self.lista_productos = []

    def agregar_producto(self, producto):
        self.arbol.insertar(producto)
        self.lista_productos.append(producto)

    def buscar_producto_bst(self, codigo):
        inicio = time.time()
        resultado = self.arbol.buscar(codigo)
        fin = time.time()
        return resultado, fin - inicio

    def buscar_producto_lista(self, codigo):
        inicio = time.time()
        for producto in self.lista_productos:
            if producto.codigo == codigo:
                fin = time.time()
                return producto, fin - inicio
        fin = time.time()
        return None, fin - inicio

    def eliminar_producto(self, codigo):
        self.arbol.eliminar(codigo)
        self.lista_productos = [p for p in self.lista_productos if p.codigo != codigo]

def generar_codigo():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))

def generar_nombre():
    return ''.join(random.choices(string.ascii_lowercase, k=10))

def main():
    sistema = SistemaInventario()
    
    # Generar datos de prueba
    num_productos = [100, 1000, 10000]
    
    for n in num_productos:
        print(f"\nPruebas con {n} productos:")
        
        # Generar productos
        for _ in range(n):
            codigo = generar_codigo()
            nombre = generar_nombre()
            precio = random.uniform(1.0, 1000.0)
            producto = Producto(codigo, nombre, precio)
            sistema.agregar_producto(producto)
        
        # Realizar búsquedas
        codigos_busqueda = [generar_codigo() for _ in range(100)]
        
        tiempo_bst = 0
        tiempo_lista = 0
        
        for codigo in codigos_busqueda:
            _, tiempo = sistema.buscar_producto_bst(codigo)
            tiempo_bst += tiempo
            
            _, tiempo = sistema.buscar_producto_lista(codigo)
            tiempo_lista += tiempo
        
        print(f"Tiempo promedio de búsqueda en BST: {tiempo_bst/100:.6f} segundos")
        print(f"Tiempo promedio de búsqueda en lista: {tiempo_lista/100:.6f} segundos")

if __name__ == "__main__":
    main()