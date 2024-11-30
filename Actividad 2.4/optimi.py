# Código Original
def encontrar_duplicados(lista):
    duplicados = []
    for i in range(len(lista)):
        for j in range(i + 1, len(lista)):
            if lista[i] == lista[j] and lista[i] not in duplicados:
                duplicados.append(lista[i])
    return duplicados



# Código Optimizado
def encontrar_duplicados_optimizado(lista):
    vistos = set()
    duplicados = set()
    for numero in lista:
        if numero in vistos:
            duplicados.add(numero)
        else:
            vistos.add(numero)
    return list(duplicados)

# Ejemplo de uso y comparación
numeros = [1, 2, 3, 2, 4, 5, 1]

print("Código Original:")
print(encontrar_duplicados(numeros))  # Salida esperada: [2, 1]

print("\nCódigo Optimizado:")
print(encontrar_duplicados_optimizado(numeros))  # Salida esperada: [1, 2]
