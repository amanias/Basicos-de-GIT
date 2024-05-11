''' Manejo de ficheros'''
import pickle
from pathlib import Path

def abrir_diccionario(nombre):
    ''' Abre un fichero que contiene un diccionario y lo carga'''
    fichero = open(nombre, "rb")
    datos = pickle.load(fichero)
    fichero.close()
    return datos

def grabar_diccionario(nombre_fichero, datos):
    ''' Graba un diccionario en un fichero'''
    fichero = open(nombre_fichero, "wb")
    pickle.dump(datos, fichero)
    fichero.close()

fichero_nombre = input("Introduce el nombre del archvo para cargar los datos: ")
path = Path(fichero_nombre)

if path.is_file():
    diccionario = abrir_diccionario(path) 
    print(diccionario, end="\n")
else:
    diccionario = {}
    print("El fichero no existe con lo que creamos uno por defecto.")
    diccionario["02880596F"] = 55
    grabar_diccionario(path, diccionario)