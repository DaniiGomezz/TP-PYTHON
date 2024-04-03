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

# Solicitamos al usuario que ingrese el número de fila y resta 1 para ajustar el índice.
fila = int(input("Ingrese el número de fila: ")) - 1 

# Solicitamos al usuario que ingrese el número de columna y resta 1 para ajustar el índice.
columna = int(input("Ingrese el número de columna: ")) - 1  


# Definimos una función llamada 'obtener_numero' que toma tres parámetros: 'matriz', 'fila' y 'columna'.
def obtener_numero(matriz, fila, columna):
    
    # Comprobamos que los numeros ingresados sean positivos
    if fila <= 0:
        return "Error, debes ingresar un número positivo"
    if columna <= 0:
        return "Error, debes ingresar un número positivo"
    
    
    # Comprueba si la fila o columna están fuera de los límites de la matriz.
    if fila < 0 or fila >= 5 or columna < 0 or columna >= 5:
        return "La posición está fuera de los límites de la matriz."
    else:
        # Obtiene el número en la posición especificada por 'fila' y 'columna'.
        numero = matriz[fila, columna]
        return numero

# Llama a la función 'obtener_numero' con los parámetros dados y almacena el resultado.
resultado = obtener_numero(matriz, fila, columna)

# Imprime el número obtenido y su posición en la matriz.
print(f"El número en la posición ({fila + 1}, {columna + 1}) es: {resultado}")

assert obtener_numero(5, 2) == 18, "Error en el caso de prueba"