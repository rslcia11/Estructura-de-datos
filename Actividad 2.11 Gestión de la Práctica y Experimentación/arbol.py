class Nodo:
    def __init__(self, valor):
        # Cada nodo tiene un valor, un hijo izquierdo y un hijo derecho
        self.valor = valor
        self.izquierda = None
        self.derecha = None

class ArbolBinario:
    def __init__(self, raiz):
        # El árbol binario tiene una raíz
        self.raiz = raiz
    
    def evaluar(self, nodo=None):
        # Si no se pasa un nodo, empezamos desde la raíz
        if nodo is None:
            nodo = self.raiz
        
        # Si el nodo es un operando (número), devolvemos su valor
        if nodo.izquierda is None and nodo.derecha is None:
            return float(nodo.valor)
        
        # Evaluamos recursivamente los operandos izquierdo y derecho
        izquierda = self.evaluar(nodo.izquierda)
        derecha = self.evaluar(nodo.derecha)
        
        # Aplicamos el operador dependiendo del valor del nodo
        if nodo.valor == '+':
            return izquierda + derecha
        elif nodo.valor == '-':
            return izquierda - derecha
        elif nodo.valor == '*':
            return izquierda * derecha
        elif nodo.valor == '/':
            return izquierda / derecha
        else:
            raise ValueError(f"Operador no soportado: {nodo.valor}")

# Crear el árbol binario para la expresión (3 + (2 * 5))
nodo_raiz = Nodo('+')
nodo_raiz.izquierda = Nodo('3')
nodo_raiz.derecha = Nodo('*')
nodo_raiz.derecha.izquierda = Nodo('2')
nodo_raiz.derecha.derecha = Nodo('5')

# Crear el árbol binario
arbol = ArbolBinario(nodo_raiz)

# Evaluar la expresión
resultado = arbol.evaluar()
print(f"Resultado de la expresión (3 + (2 * 5)): {resultado}")


# Crear otro ejemplo: Expresión (10 - (3 + 2))
nodo_raiz2 = Nodo('-')
nodo_raiz2.izquierda = Nodo('10')
nodo_raiz2.derecha = Nodo('+')
nodo_raiz2.derecha.izquierda = Nodo('3')
nodo_raiz2.derecha.derecha = Nodo('2')

# Crear el árbol binario
arbol2 = ArbolBinario(nodo_raiz2)

# Evaluar la expresión
resultado2 = arbol2.evaluar()
print(f"Resultado de la expresión (10 - (3 + 2)): {resultado2}")


# Crear otro ejemplo: Expresión (6 / (2 + 3))
nodo_raiz3 = Nodo('/')
nodo_raiz3.izquierda = Nodo('6')
nodo_raiz3.derecha = Nodo('+')
nodo_raiz3.derecha.izquierda = Nodo('2')
nodo_raiz3.derecha.derecha = Nodo('3')

# Crear el árbol binario
arbol3 = ArbolBinario(nodo_raiz3)

# Evaluar la expresión
resultado3 = arbol3.evaluar()
print(f"Resultado de la expresión (6 / (2 + 3)): {resultado3}")
