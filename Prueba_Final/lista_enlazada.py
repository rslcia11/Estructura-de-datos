class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.sig = None
        self.ant = None

class Cola:
    def __init__(self):
        self.frente = None
        self.final = None
        self.tam = 0

    def vacia(self):
        return self.tam == 0

    def meter(self, item):
        nuevo = Nodo(item)
        if self.vacia():
            self.frente = self.final = nuevo
        else:
            nuevo.ant = self.final
            self.final.sig = nuevo
            self.final = nuevo
        self.tam += 1

    def sacar(self):
        if self.vacia():
            raise IndexError("Cola vacía")
        item = self.frente.dato
        self.frente = self.frente.sig
        if self.frente:
            self.frente.ant = None
        else:
            self.final = None
        self.tam -= 1
        return item

    def ver(self):
        if self.vacia():
            raise IndexError("Cola vacía")
        return self.frente.dato

    def __len__(self):
        return self.tam

    def __str__(self):
        if self.vacia():
            return "Cola vacía"
        actual = self.frente
        items = []
        while actual:
            items.append(str(actual.dato))
            actual = actual.sig
        return " -> ".join(items)

# Prueba de funcionalidad
def probar_cola():
    cola = Cola()
    
    print("Metiendo items: 1, 2, 3, 4, 5")
    for i in range(1, 6):
        cola.meter(i)
    print("Cola:", cola)
    print("Tamaño:", len(cola))
    
    print("\nSacando dos items")
    print("item:", cola.sacar())
    print("item:", cola.sacar())
    print("Cola después de sacar items:", cola)
    
    print("\nViendo el frente")
    print("Frente:", cola.ver())
    
    print("\nMetiendo 6 y 7")
    cola.meter(6)
    cola.meter(7)
    print("Cola después de meter items:", cola)
    
    print("\nSacando todos los items restantes")
    while not cola.vacia():
        print("Item:", cola.sacar())
    
    print("\nIntentando sacar de cola vacía")
    try:
        cola.sacar()
    except IndexError as e:
        print("Error:", str(e))

if __name__ == "__main__":
    probar_cola()

