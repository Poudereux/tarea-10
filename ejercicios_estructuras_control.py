"""
Programación I - Grado en Business Analytics (UFV)
Ejercicios de estructuras de control
Autor: Miguel Poudereux

Cada ejercicio incluye el algoritmo en pseudocódigo (comentario) justo antes
de su implementación en Python, que sigue la misma estructura.
"""

# ============================================================
# 1. BIFURCACIONES (if / elif / else)
# ============================================================

'''
Algoritmo: Signo de un número
Entrada: numero (número)
Salida: texto ("positivo", "negativo" o "cero")
Desarrollo:
    SI numero > 0 ENTONCES
        resultado <- "positivo"
    SINO SI numero < 0 ENTONCES
        resultado <- "negativo"
    SINO
        resultado <- "cero"
    FIN SI
    DEVOLVER resultado
'''
def signo_numero(numero):
    """Devuelve si un número es positivo, negativo o cero."""
    if numero > 0:
        resultado = "positivo"
    elif numero < 0:
        resultado = "negativo"
    else:
        resultado = "cero"
    return resultado


'''
Algoritmo: Año bisiesto
Entrada: anio (entero)
Salida: True si es bisiesto, False si no
Desarrollo:
    SI anio es divisible entre 400 ENTONCES
        resultado <- True
    SINO SI anio es divisible entre 100 ENTONCES
        resultado <- False
    SINO SI anio es divisible entre 4 ENTONCES
        resultado <- True
    SINO
        resultado <- False
    FIN SI
    DEVOLVER resultado
'''
def es_bisiesto(anio):
    """Determina si un año es bisiesto."""
    if anio % 400 == 0:
        resultado = True
    elif anio % 100 == 0:
        resultado = False
    elif anio % 4 == 0:
        resultado = True
    else:
        resultado = False
    return resultado


'''
Algoritmo: El mayor de tres números
Entrada: a, b, c (números)
Salida: el mayor de los tres
Desarrollo:
    SI a >= b Y a >= c ENTONCES
        mayor <- a
    SINO SI b >= a Y b >= c ENTONCES
        mayor <- b
    SINO
        mayor <- c
    FIN SI
    DEVOLVER mayor
'''
def mayor_de_tres(a, b, c):
    """Devuelve el mayor de tres números sin usar max()."""
    if a >= b and a >= c:
        mayor = a
    elif b >= a and b >= c:
        mayor = b
    else:
        mayor = c
    return mayor


'''
Algoritmo: Categoría de envío según el peso
Entrada: peso_kg (número)
Salida: categoría (texto)
Desarrollo:
    SI peso_kg <= 1 ENTONCES
        categoria <- "Sobre"
    SINO SI peso_kg <= 5 ENTONCES
        categoria <- "Paquete pequeño"
    SINO SI peso_kg <= 20 ENTONCES
        categoria <- "Paquete grande"
    SINO
        categoria <- "Voluminoso"
    FIN SI
    DEVOLVER categoria
'''
def categoria_envio(peso_kg):
    """Clasifica un envío según su peso en kilos."""
    if peso_kg <= 1:
        categoria = "Sobre"
    elif peso_kg <= 5:
        categoria = "Paquete pequeño"
    elif peso_kg <= 20:
        categoria = "Paquete grande"
    else:
        categoria = "Voluminoso"
    return categoria


# ============================================================
# 2. ITERACIONES (for / while)
# ============================================================

'''
Algoritmo: Suma de pares entre 1 y n
Entrada: n (entero)
Salida: suma de los pares entre 1 y n
Desarrollo:
    suma <- 0
    PARA i DESDE 1 HASTA n HACER
        SI i es divisible entre 2 ENTONCES
            suma <- suma + i
        FIN SI
    FIN PARA
    DEVOLVER suma
'''
def suma_pares(n):
    """Suma los números pares entre 1 y n."""
    suma = 0
    for i in range(1, n + 1):
        if i % 2 == 0:
            suma = suma + i
    return suma


'''
Algoritmo: Factorial con bucle
Entrada: n (entero >= 0)
Salida: n!
Desarrollo:
    resultado <- 1
    PARA i DESDE 2 HASTA n HACER
        resultado <- resultado * i
    FIN PARA
    DEVOLVER resultado      (0! = 1 porque el bucle no se ejecuta)
'''
def factorial_iterativo(n):
    """Calcula n! usando un bucle (versión iterativa)."""
    resultado = 1
    for i in range(2, n + 1):
        resultado = resultado * i
    return resultado


'''
Algoritmo: Contar vocales de una palabra
Entrada: palabra (texto)
Salida: número de vocales
Desarrollo:
    contador <- 0
    vocales <- "aeiou"
    palabra <- palabra en minúsculas
    PARA CADA letra EN palabra HACER
        SI letra está en vocales ENTONCES
            contador <- contador + 1
        FIN SI
    FIN PARA
    DEVOLVER contador
'''
def contar_vocales(palabra):
    """Cuenta las vocales de una palabra, sin distinguir mayúsculas."""
    contador = 0
    vocales = "aeiou"
    palabra = palabra.lower()
    for letra in palabra:
        if letra in vocales:
            contador = contador + 1
    return contador


'''
Algoritmo: Tabla de multiplicar
Entrada: numero (entero)
Salida: (por pantalla) las líneas "numero x i = producto" de i = 1 a 10
Desarrollo:
    PARA i DESDE 1 HASTA 10 HACER
        MOSTRAR numero + " x " + i + " = " + (numero * i)
    FIN PARA
'''
def tabla_multiplicar(numero):
    """Imprime la tabla de multiplicar de un número, del 1 al 10."""
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")


# ============================================================
# 3. FUNCIONES
# ============================================================

'''
Algoritmo: Promedio de una lista de números
Entrada: numeros (lista de números)
Salida: media aritmética
Desarrollo:
    suma <- 0
    PARA CADA numero EN numeros HACER
        suma <- suma + numero
    FIN PARA
    promedio <- suma / cantidad de elementos de numeros
    DEVOLVER promedio
'''
def calcular_promedio(numeros):
    """Calcula la media aritmética de una lista de números."""
    suma = 0
    for numero in numeros:
        suma = suma + numero
    promedio = suma / len(numeros)
    return promedio


'''
Algoritmo: Texto en mayúsculas y número de palabras
Entrada: frase (texto)
Salida: frase en mayúsculas, número de palabras
Desarrollo:
    mayusculas <- frase en mayúsculas
    palabras <- separar frase por espacios
    cantidad <- número de elementos de palabras
    DEVOLVER mayusculas, cantidad
'''
def analizar_frase(frase):
    """Devuelve la frase en mayúsculas junto con su número de palabras."""
    mayusculas = frase.upper()
    palabras = frase.split()
    cantidad = len(palabras)
    return mayusculas, cantidad


'''
Algoritmo: Validar contraseña
Entrada: contrasena (texto), longitud_minima (entero, por defecto 8)
Salida: True si longitud(contrasena) >= longitud_minima, False si no
Desarrollo:
    SI longitud de contrasena >= longitud_minima ENTONCES
        valida <- True
    SINO
        valida <- False
    FIN SI
    DEVOLVER valida
'''
def validar_contrasena(contrasena, longitud_minima=8):
    """Comprueba si una contraseña alcanza la longitud mínima exigida."""
    if len(contrasena) >= longitud_minima:
        valida = True
    else:
        valida = False
    return valida


'''
Algoritmo: Celsius a Fahrenheit
Entrada: celsius (número)
Salida: grados Fahrenheit
Desarrollo:
    fahrenheit <- celsius * 9 / 5 + 32
    DEVOLVER fahrenheit
'''
def celsius_a_fahrenheit(celsius):
    """Convierte una temperatura de Celsius a Fahrenheit."""
    fahrenheit = celsius * 9 / 5 + 32
    return fahrenheit


'''
Algoritmo: Fahrenheit a Celsius
Entrada: fahrenheit (número)
Salida: grados Celsius
Desarrollo:
    celsius <- (fahrenheit - 32) * 5 / 9
    DEVOLVER celsius
'''
def fahrenheit_a_celsius(fahrenheit):
    """Convierte una temperatura de Fahrenheit a Celsius."""
    celsius = (fahrenheit - 32) * 5 / 9
    return celsius


# ============================================================
# 4. FUNCIONES RECURSIVAS
# ============================================================

'''
Algoritmo: Factorial recursivo
Entrada: n (entero >= 0)
Salida: n!
Desarrollo:
    SI n == 0 ENTONCES                  (caso base)
        resultado <- 1
    SINO                                (caso recursivo)
        resultado <- n * factorial_recursivo(n - 1)
    FIN SI
    DEVOLVER resultado
'''
def factorial_recursivo(n):
    """Calcula n! llamándose a sí misma (versión recursiva)."""
    if n == 0:
        resultado = 1
    else:
        resultado = n * factorial_recursivo(n - 1)
    return resultado


'''
Algoritmo: Sucesión de Fibonacci
Entrada: n (entero >= 0)
Salida: término n de la sucesión (0, 1, 1, 2, 3, 5, 8, ...)
Desarrollo:
    SI n == 0 ENTONCES                  (caso base 1)
        resultado <- 0
    SINO SI n == 1 ENTONCES             (caso base 2)
        resultado <- 1
    SINO                                (caso recursivo)
        resultado <- fibonacci(n - 1) + fibonacci(n - 2)
    FIN SI
    DEVOLVER resultado
'''
def fibonacci(n):
    """Devuelve el término n de la sucesión de Fibonacci."""
    if n == 0:
        resultado = 0
    elif n == 1:
        resultado = 1
    else:
        resultado = fibonacci(n - 1) + fibonacci(n - 2)
    return resultado


'''
Algoritmo: Suma recursiva de una lista
Entrada: numeros (lista de números)
Salida: suma de todos los elementos
Desarrollo:
    SI numeros está vacía ENTONCES      (caso base)
        resultado <- 0
    SINO                                (caso recursivo)
        resultado <- primer elemento + suma_lista(resto de la lista)
    FIN SI
    DEVOLVER resultado
'''
def suma_lista(numeros):
    """Suma los elementos de una lista de forma recursiva."""
    if len(numeros) == 0:
        resultado = 0
    else:
        resultado = numeros[0] + suma_lista(numeros[1:])
    return resultado


'''
Algoritmo: Invertir una cadena de texto
Entrada: texto (cadena)
Salida: texto invertido
Desarrollo:
    SI longitud de texto <= 1 ENTONCES  (caso base)
        resultado <- texto
    SINO                                (caso recursivo)
        resultado <- invertir_texto(texto sin su primer carácter) + primer carácter
    FIN SI
    DEVOLVER resultado
'''
def invertir_texto(texto):
    """Invierte una cadena de texto de forma recursiva."""
    if len(texto) <= 1:
        resultado = texto
    else:
        resultado = invertir_texto(texto[1:]) + texto[0]
    return resultado


# ============================================================
# 5. EXCEPCIONES (try / except)
# ============================================================

'''
Algoritmo: División segura
Entrada: a, b (números)
Salida: a / b, o "Error: división entre cero"
Desarrollo:
    INTENTAR
        resultado <- a / b
    SI OCURRE división entre cero ENTONCES
        resultado <- "Error: división entre cero"
    FIN INTENTAR
    DEVOLVER resultado
'''
def division_segura(a, b):
    """Divide dos números controlando la división entre cero."""
    try:
        resultado = a / b
    except ZeroDivisionError:
        resultado = "Error: división entre cero"
    return resultado


'''
Algoritmo: Convertir texto a entero
Entrada: texto (cadena)
Salida: el número entero, o "Error: no es un número"
Desarrollo:
    INTENTAR
        resultado <- convertir texto a entero
    SI OCURRE error de formato ENTONCES
        resultado <- "Error: no es un número"
    FIN INTENTAR
    DEVOLVER resultado
'''
def convertir_a_entero(texto):
    """Convierte un texto a entero controlando el error de formato."""
    try:
        resultado = int(texto)
    except ValueError:
        resultado = "Error: no es un número"
    return resultado


'''
Algoritmo: Acceso seguro a una lista
Entrada: lista (lista), posicion (entero)
Salida: elemento de esa posición, o "Error: posición fuera de rango"
Desarrollo:
    INTENTAR
        resultado <- elemento de lista en posicion
    SI OCURRE posición fuera de rango ENTONCES
        resultado <- "Error: posición fuera de rango"
    FIN INTENTAR
    DEVOLVER resultado
'''
def obtener_elemento(lista, posicion):
    """Accede a una posición de una lista controlando el error de rango."""
    try:
        resultado = lista[posicion]
    except IndexError:
        resultado = "Error: posición fuera de rango"
    return resultado


'''
Algoritmo: Calculadora con control de errores
Entrada: texto_a, texto_b (cadenas), operacion ("suma" o "division")
Salida: resultado numérico, o un mensaje de error según el caso
Desarrollo:
    INTENTAR
        a <- convertir texto_a a número decimal
        b <- convertir texto_b a número decimal
        SI operacion == "suma" ENTONCES
            resultado <- a + b
        SINO SI operacion == "division" ENTONCES
            resultado <- a / b
        SINO
            resultado <- "Error: operación no válida"
        FIN SI
    SI OCURRE error de formato ENTONCES
        resultado <- "Error: valor no numérico"
    SI OCURRE división entre cero ENTONCES
        resultado <- "Error: división entre cero"
    FIN INTENTAR
    DEVOLVER resultado
'''
def calculadora_segura(texto_a, texto_b, operacion):
    """Suma o divide dos textos numéricos controlando los errores posibles."""
    try:
        a = float(texto_a)
        b = float(texto_b)
        if operacion == "suma":
            resultado = a + b
        elif operacion == "division":
            resultado = a / b
        else:
            resultado = "Error: operación no válida"
    except ValueError:
        resultado = "Error: valor no numérico"
    except ZeroDivisionError:
        resultado = "Error: división entre cero"
    return resultado


# ============================================================
# PRUEBAS (con los ejemplos del enunciado)
# ============================================================
if __name__ == "__main__":
    assert signo_numero(-5) == "negativo" and signo_numero(0) == "cero"
    assert signo_numero(3) == "positivo"
    assert es_bisiesto(2024) and not es_bisiesto(1900) and es_bisiesto(2000)
    assert mayor_de_tres(4, 9, 2) == 9 and mayor_de_tres(7, 7, 3) == 7
    assert categoria_envio(0.5) == "Sobre" and categoria_envio(15) == "Paquete grande"
    assert categoria_envio(3) == "Paquete pequeño" and categoria_envio(25) == "Voluminoso"
    assert suma_pares(10) == 30 and suma_pares(1) == 0
    assert factorial_iterativo(5) == 120 and factorial_iterativo(0) == 1
    assert contar_vocales("Programacion") == 5 and contar_vocales("xyz") == 0
    tabla_multiplicar(3)
    assert calcular_promedio([4, 8, 6]) == 6.0
    assert analizar_frase("hola que tal") == ("HOLA QUE TAL", 3)
    assert validar_contrasena("abc123") is False and validar_contrasena("abc123", 5) is True
    assert celsius_a_fahrenheit(0) == 32.0 and fahrenheit_a_celsius(32) == 0.0
    assert factorial_recursivo(5) == 120 and factorial_recursivo(0) == 1
    assert fibonacci(6) == 8 and fibonacci(0) == 0
    assert suma_lista([1, 2, 3, 4]) == 10 and suma_lista([]) == 0
    assert invertir_texto("python") == "nohtyp" and invertir_texto("a") == "a"
    assert division_segura(10, 0) == "Error: división entre cero"
    assert division_segura(10, 2) == 5.0
    assert convertir_a_entero("42") == 42
    assert convertir_a_entero("hola") == "Error: no es un número"
    assert obtener_elemento([1, 2, 3], 1) == 2
    assert obtener_elemento([1, 2, 3], 9) == "Error: posición fuera de rango"
    assert calculadora_segura("10", "0", "division") == "Error: división entre cero"
    assert calculadora_segura("abc", "2", "suma") == "Error: valor no numérico"
    assert calculadora_segura("4", "2", "suma") == 6.0
    print("\nTodas las pruebas han pasado correctamente.")
