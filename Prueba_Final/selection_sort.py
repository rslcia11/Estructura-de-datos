import random
import timeit

def mystery_original(arr):
    """Algoritmo original"""
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr

def optimized_selection_sort(arr):
    """Selection Sort optimizado con menos intercambios"""
    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        if min_idx != i:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

def count_swaps(func, arr):
    swaps = 0
    arr_copy = arr[:]
    
    def swap(i, j):
        nonlocal swaps
        arr_copy[i], arr_copy[j] = arr_copy[j], arr_copy[i]
        swaps += 1
    
    if func.__name__ == "mystery_original":
        for i in range(len(arr_copy)):
            for j in range(i, len(arr_copy)):
                if arr_copy[i] > arr_copy[j]:
                    swap(i, j)
    else:  # optimized_selection_sort
        for i in range(len(arr_copy)):
            min_idx = i
            for j in range(i+1, len(arr_copy)):
                if arr_copy[j] < arr_copy[min_idx]:
                    min_idx = j
            if min_idx != i:
                swap(i, min_idx)
    
    return arr_copy, swaps

def measure_performance(func, arr):
    result, swaps = count_swaps(func, arr)
    time = timeit.timeit(lambda: func(arr[:]), number=100) / 100  # Promedio de 100 ejecuciones
    return result, time, swaps

# Crear un array aleatorio más grande para pruebas
test_array = random.sample(range(10000), 1000)
print("Tamaño del array de prueba:", len(test_array))
print("Array original (primeros 10 elementos):", test_array[:10])

# Comparar rendimiento
result1, time1, swaps1 = measure_performance(mystery_original, test_array)
result2, time2, swaps2 = measure_performance(optimized_selection_sort, test_array)

print("\nResultados de rendimiento:")
print(f"Algoritmo original: {time1:.6f} segundos, {swaps1} intercambios")
print(f"Algoritmo optimizado: {time2:.6f} segundos, {swaps2} intercambios")
print(f"Mejora en intercambios: {swaps1/swaps2:.2f}x menos intercambios")

# Manejar el caso de división por cero
if time2 == 0:
    print("El algoritmo optimizado fue demasiado rápido para medir con precisión.")
else:
    print(f"Mejora en tiempo: {time1/time2:.2f}x más rápido")

# Verificar que ambos algoritmos producen el mismo resultado
print("\n¿Ambos algoritmos producen el mismo resultado ordenado?", result1 == result2)


