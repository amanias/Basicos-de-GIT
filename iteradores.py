import random

def ordenar_lista(lista):
    ''' Devuelve una lista ordenada'''
    return sorted(lista)
def ordenar_lista_tuplas(lista):
    return list(enumerate(lista))

lista = (4, 5, 9, 3, 0, 6)
print("Lista: ", ordenar_lista(lista))
print("Tupla: ", ordenar_lista_tuplas(lista))

''' Manejar los objetos interables en los bucles FOR.'''
letras = list("abcdefghijklmnñopqrstuvwxyz")

for letra in letras:
    print(letra, end=" ")
print()

# Vamos a sacar el indice de cada letra con la dupla que me crea el ENUMERATE(secuencia)
for indice, letra in enumerate(letras):
    print(f"La letra {letra} está en la posición {indice}")

lista1 = letras[:9]
abcde = list(enumerate(lista1))
print("Primeras Letras: ", lista1)
print(abcde)
random.shuffle(lista1)
print("Primeras Letras Aleatorias: ", lista1)
print("Aleatorio Ordenada", list(sorted(enumerate(lista1, 20))))


lista2 = letras[9:18]
print("Letras del medio: ", lista2)
random.shuffle(lista2)
print("Letras del Medio Aleatorias: ", lista2)

lista3 = letras[18:]
print("Letras finales: ", lista3)
random.shuffle(lista3)
print("Letras Aleatorias Finales: ", lista3)

for a, b, c in zip(lista1, lista2, lista3):
    print(a+b+c, end=" ")

