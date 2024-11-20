# Función para encontrar el valor máximo y mínimo de un arreglo
def encontrar_max_min(arreglo):
    # Comprobamos si el arreglo no está vacío
    if not arreglo:
        return None, None  # Si el arreglo está vacío, retornamos None

    maximo = arreglo[0]
    minimo = arreglo[0]

    # Recorremos el arreglo para encontrar los valores máximo y mínimo
    for num in arreglo:
        if num > maximo:
            maximo = num
        elif num < minimo:
            minimo = num

    return maximo, minimo

# Ejemplo de 
arreglo = [12, 45, 23, 78, 34, 9]
maximo, minimo = encontrar_max_min(arreglo)

print(f"Max = {maximo}, Min = {minimo}")
