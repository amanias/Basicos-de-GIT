''' Ejemplos de Estructuras de Control'''
n_num1 = 15
n_num2 = 10
if n_num1 > n_num2: print(n_num1 , "es mayor que" , n_num2)

# IF...ELSE abreviado
a = 2
b = 330
print("A" if a > b else "B")

# Operador ternario
num = 12
var = "par" if (num % 2 == 0) else "impar"
print("par" if (num % 2 == 0) else "impar")

for x in range(6): print(x)
for x in range(2, 6): print(x)
for x in range(2, 30, 3): print(x)

miTupla = ("manzana", "banana", "cereza")
print(miTupla[1])
print(miTupla[-3])
print("manzana" in miTupla)

tupla1 = ("a", "b" , "c")
tupla2 = (1, 2, 3)
tupla3 = tupla1 + tupla2
print(tupla3)

# Quitar valores de un diccionario
peliculas = {"Love Actually": "Richard Curtis", "Kill Bill": "Tarantino", "Amélie": "Jean-Pierre Jeunet"}
print(peliculas)
peliculas.pop("Love Actually")
print(peliculas)

# Crear un diccionario a partir de dos listas:
lista_claves=["nombre", "edad"]
lista_valores=["Angel", 43]
diccionario = list(zip(lista_claves , lista_valores))
print(diccionario)
diccionario = tuple(zip(lista_claves , lista_valores))
print(diccionario)
diccionario = dict(zip(lista_claves , lista_valores))
print(diccionario)

# Eliminar el último elemento insertado:
miDiccionario = { "brand": "Ford", "model": "Mustang", "year": 1964 }
miDiccionario.popitem()
print(miDiccionario)

# Eliminar un elemento
miDiccionario = { "brand": "Ford", "model": "Mustang", "year": 1964 }
miDiccionario.pop("brand")
print(miDiccionario)
del miDiccionario["year"]
print(miDiccionario)

# La palabra clave clear() vacía el diccionario: 
miDiccionario = { "brand": "Ford", "model": "Mustang", "year": 1964 }
miDiccionario.clear()
print(miDiccionario)

# Crear un Conjunto
mi_conjunto3 = set(("Angel", "Sara", "Pilar"))
print(mi_conjunto3)
mi_conjunto3.add("Alberto")
print(mi_conjunto3)
mi_conjunto3.update({"Albertos", "amanias"})
print(mi_conjunto3)
mi_conjunto3.remove("Albertos")
print(mi_conjunto3)
mi_conjunto3.discard("Alberto")
mi_conjunto3.discard("Alberto") # Si el elemento no existe no genera error cmo REMOVE
print(mi_conjunto3)

# Unión de conjuntos
# El método union() devuelve un nuevo conjunto con todos los elementos de ambos conjuntos:
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3)

set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set1.update(set2)
print(set1)

# Funciones con argumentos variables
# Me crea una tupla de nombre "otros"
def varios(param1, param2, *otros):
    for val in otros:
        print (val)
        
varios(1, 2)
varios(1, 2, 3)
varios(1, 2, 3, 4)
varios(1, 2, 3, 4, 7)

""" También se puede preceder el nombre del último parámetro con **,
en cuyo caso en lugar de una tupla se utilizaría un diccionario.
Las claves de este diccionario serían los nombres de los parámetros indicados al llamar a la función
y los valores del diccionario, los valores asociados a estos parámetros. """

def varios(param1, param2, **otros):
    for i in otros.items():
        print(i)
varios(1, 2, tercero = 3, cuarto = 8)

# --------------------------- 
#---------------------------------------
#ARGUMENTOS VARIABLES EN FUNCIONES. EL ARGUMENTO CON * SERÁ UNA TUPLA
# PYTHON NO TIENE SOBRECARGA DE FUNCIONES
#---------------------------------------
def listarNombres(*nombres):
    for nombre in nombres:
        print(nombre)
        
listarNombres('Juan', 'Karla', 'María', 'Ernesto')
listarNombres('Laura', 'Carlos')

#--------------------------------------- 
# hACER LO MISMO PERO PASANDO DICCIONARIOS COMO ARGUMENTOS. KWARGS 
def listarTerminos(**KWARGS):
    for clave, valor in KWARGS.items():
            print(f'{clave}: {valor}')
    
listarTerminos(IDE='Integrated Developement Environment', PK='Primary Key')
listarTerminos(DBMS='Database Management System')

def mi_funcion(nombre, apellido):
    print('saludos desde mi función')
    print(f'Nombre: {nombre}, Apellido: {apellido}')

    # Sería como imprimir así:
    print('Nombre:', nombre, ', Apellido:', apellido)
    
mi_funcion('Juan', 'Perez')
mi_funcion('Karla','Lara')