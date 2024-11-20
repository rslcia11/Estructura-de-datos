# Función para ordenar un arreglo usando Bubble Sort
def bubble_sort(arreglo):
    n = len(arreglo)
    
    # Recorremos el arreglo 
    for i in range(n):
        intercambiado = False 
        
        # Recorremos el arreglo desde el principio
        for j in range(0, n-i-1):
            if arreglo[j] > arreglo[j+1]:
                arreglo[j], arreglo[j+1] = arreglo[j+1], arreglo[j]
                intercambiado = True
        if not intercambiado:
            break
    
    return arreglo

# Ejemplo de uso 
arreglo = [12, 45, 23, 78, 34, 9]
ordenado = bubble_sort(arreglo)

print("Arreglo ordenado:", ordenado)
