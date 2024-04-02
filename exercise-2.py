"""Ejercicio 2: “Missing Number”
Se te dan todos los números entre 1 a “n” excepto uno. Tu tarea es encontrar el número que
falta.

Input:
El primer parámetro contiene la cantidad de elementos del array.
El segundo parámetro contiene “n” números. Cada número es único y está entre 1 y n
(inclusive).
Output:
Retornar el número que falta.
"""
# Solicita al usuario que ingrese cuántos elementos habrá en la lista
n = int(input("Ingrese cuántos elementos habrá en la lista: "))

# Solicita al usuario que ingrese los números faltantes separados por comas
numeros = input("Ingrese los números faltantes separados por comas, por ejemplo: 2, 3, 4: ")

# Divide la cadena de números ingresada por el usuario en una lista de cadenas utilizando la coma como separador,
# luego convierte cada cadena en la lista en un entero y crea una lista de enteros.
numeros = [int(x) for x in numeros.split(",")]

# Define una función llamada 'encontrar_numero_faltante' que toma dos parámetros, 'n' y 'numeros'.
def encontrar_numero_faltante(n, numeros):
    # Calcula la suma total utilizando la fórmula de la sumatoria.
    sumatoria = n * (n + 1) // 2
    # Calcula la suma de los números dados por el usuario.
    suma_numeros = sum(numeros)
    # Calcula el número faltante restando la suma de los números dados de la suma total esperada.
    numero_perdido = sumatoria - suma_numeros
    
    return numero_perdido

# Imprime el número faltante llamando a la función 'encontrar_numero_faltante' con los parámetros 'n' y 'numeros'.
print("El número que falta es:", encontrar_numero_faltante(n, numeros))