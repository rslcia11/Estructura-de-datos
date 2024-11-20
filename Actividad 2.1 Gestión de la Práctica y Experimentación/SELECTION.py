# Función para ordenar un arreglo usando Selection Sort
def selection_sort(arreglo):
    n = len(arreglo)
    
    # Recorremos el arreglo completo
    for i in range(n):
        min_idx = i
        
        for j in range(i+1, n):
            if arreglo[j] < arreglo[min_idx]:
                min_idx = j
        
        arreglo[i], arreglo[min_idx] = arreglo[min_idx], arreglo[i]
    
    return arreglo

# Ejemplo de uso 
arreglo = [12, 45, 23, 78, 34, 9]
ordenado = selection_sort(arreglo)

print("Arreglo ordenado:", ordenado)
