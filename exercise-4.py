'''Ejercicio 4: “Palindrome Reorder”
Dada una cadena de caracteres, tu tarea es reorganizar los caracteres de la cadena de manera
que puedas formar un palíndromo. Si no es posible formar un palíndromo, debes indicarlo.
Input:
El único parámetro contiene una cadena de caracteres de longitud n ( 1 ≤ n ≤ 10^6 ). La
cadena solo contiene letras minúsculas del alfabeto inglés.
Output:
Retorna una cadena que represente un palíndromo formado reorganizando los caracteres de la
cadena de entrada. Si no es posible formar un palíndromo, retorna "NO SOLUTION".'''

# Importamos Counter de la librería collections
def palindrome_reorder(s):
    # Inicialización del diccionario para contar la frecuencia de cada caracter
    char_count = {}
    
    # Conteo de la frecuencia de cada caracter en la cadena
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1
    
    # Variables para contar caracteres impares y almacenar el carácter impar
    odd_count = 0
    odd_char = ''
    
    # Construcción de la mitad del palíndromo
    half_palindrome = ''
    for char, count in char_count.items():
        if count % 2 != 0:
            odd_count += 1
            odd_char = char
        half_palindrome += char * (count // 2)
    
    # Verificación de la posibilidad de formar un palíndromo
    if odd_count > 1:
        return "NO SOLUTION"
    
    # Formación del palíndromo
    else:
        return half_palindrome + odd_char + half_palindrome[::-1]

cadena = "aabbc"
print(palindrome_reorder(cadena.lower())) 

assert palindrome_reorder("aabbc") == "abcba", "Error en el casode prueba"
assert palindrome_reorder("aan") == "ana", "Error en el casode prueba"

print("todos los casos de pruebas se jecutaron correctamente")
