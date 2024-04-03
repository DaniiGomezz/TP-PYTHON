# Importamos la libreria numpy
import numpy as np

# Creamos una matriz utilizando la biblioteca NumPy.
matriz = np.array([
    [1, 2, 9, 10, 25],
    [4, 3, 8, 11, 24],
    [5, 6, 7, 12, 23],
    [16, 15, 14, 13, 22],
    [17, 18, 19, 20, 21]
])

# Definimos una función llamada obtener_numero que toma dos parámetros: fila y columna.
def number_spiral(fila, columna):
    # Comprueba si la fila o columna están fuera de los límites de la matriz.
    if fila < 1 or fila > 5 or columna < 1 or columna > 5:
        return "La posición está fuera de los límites de la matriz."
    else:
        # Obtiene el número en la posición especificada por fila y columna y le resta 1 para ajustar el indice.
        numero = matriz[fila - 1, columna - 1]
        return numero

# Solicitamos al usuario que ingrese el número de fila y columna.
fila = int(input("Ingrese el número de fila (1-5): ")) 
columna = int(input("Ingrese el número de columna (1-5): ")) 

# Llama a la función obtener_numero con los parámetros dados y almacena el resultado.
resultado = number_spiral(fila, columna)

# Imprime el número obtenido y su posición en la matriz.
print(f"El número en la posición ({fila}, {columna}) es: {resultado}")

# Test
assert number_spiral(2, 2) == 3, "Error en el caso deprueba"
assert number_spiral(5, 2) == 18, "Error en el caso de prueba"
assert number_spiral(3, 5) == 23, "Error en el caso de prueba"

print("todos los casos de prueba pasaron correctamente")
