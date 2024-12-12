class Nodo:
    def __init__(self, cancion):
        self.cancion = cancion  # Almacena el nombre de la canción
        self.siguiente = None  # Apunta al siguiente nodo

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def agregar(self, cancion):
        nuevo_nodo = Nodo(cancion)
        if not self.cabeza:  # Lista vacía
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo
        print(f"Canción '{cancion}' agregada a la playlist.")

    def eliminar(self, cancion):
        if not self.cabeza:
            print("La playlist está vacía.")
            return

        if self.cabeza.cancion == cancion:  # Eliminar la cabeza
            self.cabeza = self.cabeza.siguiente
            print(f"Canción '{cancion}' eliminada de la playlist.")
            return

        actual = self.cabeza
        while actual.siguiente and actual.siguiente.cancion != cancion:
            actual = actual.siguiente

        if actual.siguiente:  # Nodo encontrado
            actual.siguiente = actual.siguiente.siguiente
            print(f"Canción '{cancion}' eliminada de la playlist.")
        else:
            print(f"Canción '{cancion}' no encontrada en la playlist.")

    def buscar(self, cancion):
        actual = self.cabeza
        while actual:
            if actual.cancion == cancion:
                print(f"Canción '{cancion}' encontrada en la playlist.")
                return True
            actual = actual.siguiente
        print(f"Canción '{cancion}' no encontrada en la playlist.")
        return False

    def mostrar(self):
        if not self.cabeza:
            print("La playlist está vacía.")
            return
        actual = self.cabeza
        print("Playlist:")
        while actual:
            print(f"- {actual.cancion}")
            actual = actual.siguiente

def menu():
    playlist = ListaEnlazada()
    while True:
        print("Sistema de Gestión de Playlist")
        print("1. Agregar canción")
        print("2. Eliminar canción")
        print("3. Buscar canción")
        print("4. Mostrar playlist")
        print("5. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            cancion = input("Ingrese el nombre de la canción: ")
            playlist.agregar(cancion)
        elif opcion == "2":
            cancion = input("Ingrese el nombre de la canción a eliminar: ")
            playlist.eliminar(cancion)
        elif opcion == "3":
            cancion = input("Ingrese el nombre de la canción a buscar: ")
            playlist.buscar(cancion)
        elif opcion == "4":
            playlist.mostrar()
        elif opcion == "5":
            print("Saliendo del sistema. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    menu()
