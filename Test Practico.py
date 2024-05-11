# 1. Dados dos números, escriba un código Python para encontrar el máximo de estos dos números
# Ejemplos:
# Entrada: a=2, b=4
# Salida: 4
# -----------------------------------------------------------------------------------------------------------------------------------------------------------------
# Entrada: a=-2 b=-4
# Salida:-1

def maximo(*valores):
    return(max(*valores))

print(maximo(2, 4))
print(maximo(-1, -4))
print(maximo(4, 5, 9, 3, 0, 8, 6))
print(maximo(4, 5, 9, 3, 0, 18, 6))

# 2. Invertir palabras de una cadena dada.

def invertir_palabras(frase):
    print(frase)
    lista_palabras = frase.split()
    print(lista_palabras)
    # lista_palabras.reverse()
    # print(lista_palabras) # Pero se pierde la lista original pues se modifica sobre ella.
    lista_palabras_invertida = lista_palabras[::-1]
    print(lista_palabras_invertida)

invertir_palabras("El agua de mayo es todo un valor!")

# 3. Realizar una suma de los elementos de una tupla
def sumar_elementos(tupla):
    resultado = 0
    for e in tupla:
        resultado += e
    print("Suma de los elementos de la tupla: ", resultado)

sumar_elementos((4, 5, 9, 3, 0, 9, 6))

# 4. Escriba un código que calcule una suma de la lista de números proporcionados.
def sumar_elementos(lista):
    resultado = 0
    for e in lista:
        resultado += e
    print("Suma de los elementos de la lista: ", resultado)

sumar_elementos((4, 5, 9, 3, 0, 9, 6))

# 5. Escriba un código que desordene al azar una lista.
def barajar_elementos(lista):
    from random import shuffle
    shuffle(lista)
    print (lista)

barajar_elementos([4, 5, 9, 3, 0, 9, 6])

# 6. Escriba un código que pueda contar todas las palabras mayúsculas de un archivo.
# Contar las mayusculas de una cadena
def contar_mayusculas(cadena):
    resultado = 0
    for letra in cadena:
        if letra.isupper():
            resultado +=1
    print(f"La cadena '{cadena}' contiene {resultado} caracteres en mayúscula")

contar_mayusculas("Hoy es el día de los Chistes")
contar_mayusculas("Hoy es el AGUA DEL día de los Chistes")

# 10. Escribir un programa en Python para comprobar si un número es capicúa.
# Es decir, si se lee igual de derecha a izquierda que de izquierda a derecha.

def numero_capicua(numero): # El número llega como una cadena.
    numero_inverso = numero[::-1]
    if numero == numero_inverso:
        print("Tu número es capicua!")
    else:
        print("Va a ser que tu número no es capicua.")

numero_capicua(input("Introduce un número: "))

# 11. Escribir un algoritmo de ordenación para un conjunto de datos numéricos en Python.
def ordenar_numeros(*numeros):
    lista_numeros = list(numeros)
    lista_numeros_ordenada = lista_numeros[::-1] # Creo una copia de la original
    lista_numeros_ordenada.sort()
    print("Lista Original: ", lista_numeros)    
    print("Lista Ordenada: ", lista_numeros_ordenada)

ordenar_numeros(4, 5, 9, 3, 0, 9, 6)