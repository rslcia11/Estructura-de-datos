# Función para buscar el mayor o menor elemento en un arreglo
def buscar_elemento(arreglo):
    mayor = max(arreglo)
    menor = min(arreglo)
    return mayor, menor

# Algoritmo de Bubble Sort
def bubble_sort(arreglo):
    n = len(arreglo)
    for i in range(n):
        for j in range(0, n-i-1):
            if arreglo[j] > arreglo[j+1]:
                arreglo[j], arreglo[j+1] = arreglo[j+1], arreglo[j]  # Intercambiar
    return arreglo

# Algoritmo de Selection Sort
def selection_sort(arreglo):
    n = len(arreglo)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arreglo[j] < arreglo[min_idx]:
                min_idx = j
        # Intercambiar el mínimo con el primer elemento no ordenado
        arreglo[i], arreglo[min_idx] = arreglo[min_idx], arreglo[i]
    return arreglo

# Ejemplo de uso
arreglo = [64, 25, 12, 22, 11]

# Buscar el mayor y menor
mayor, menor = buscar_elemento(arreglo)
print(f"El mayor elemento es: {mayor}")
print(f"El menor elemento es: {menor}")

# Ordenar el arreglo con Bubble Sort
sorted_bubble = bubble_sort(arreglo.copy())
print(f"Arreglo ordenado con Bubble Sort: {sorted_bubble}")

# Ordenar el arreglo con Selection Sort
sorted_selection = selection_sort(arreglo.copy())
print(f"Arreglo ordenado con Selection Sort: {sorted_selection}")
