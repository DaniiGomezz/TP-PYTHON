"""
Ejercicio 1: “Weird Algorithm”
Considera un algoritmo que toma como entrada un entero positivo n. Si n es par, el algoritmo
lo divide por dos, y si n es impar, el algoritmo lo multiplica por tres y le suma uno. El
algoritmo repite esto hasta que n sea uno. Por ejemplo, la secuencia para el valor 3 es la
siguiente:
3 ➝ 10 ➝ 5 ➝ 16 ➝ 8 ➝ 4 ➝ 2 ➝ 1
Tu tarea es simular la ejecución del algoritmo para un valor dado de n.
Input:
La única línea de entrada contiene un entero n.
Output:
Imprime una línea que contenga todos los valores de n durante la ejecución del algoritmo.
Constraints:
1 < n < 10
6
"""

numeroPositivo = int(input("ingrese un numero positivo: "))
# definimos una función llamada parEimpar que toma un número positivo como entrada.
def parEimpar(numeroPositivo):
    # Inicializa una lista con el número positivo inicial como su único elemento.
    par_impar_secuencia = [numeroPositivo]

    # Mientras el número positivo sea mayor que 1, realiza lo siguiente:
    while numeroPositivo > 1:
        # Si el número positivo es par pasa a dividirse entre 2.
        if numeroPositivo % 2 == 0:
            numeroPositivo //= 2
        # Si el número positivo es impar pasa a multiplicar por 3 y le suma 1.
        else:
            numeroPositivo = numeroPositivo * 3 + 1
        # Agrega el nuevo valor de numeroPositivo a la lista.
        par_impar_secuencia.append(numeroPositivo)
    
    # Retorna la lista que contiene la secuencia de los números generados.
    return par_impar_secuencia

# Imprime la secuencia de números resultante al llamar a la función parEimpar con el númeroPositivo ingresado por el usuario.

print(parEimpar(numeroPositivo))
assert parEimpar(3) == [3, 10, 5, 16, 8, 4, 2, 1], "Error en el caso de prueba"
