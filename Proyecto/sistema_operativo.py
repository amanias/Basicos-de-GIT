# Librería necesaria por compatibilidad de sistemas.
from os import name as sistema_operativo
from os import system as comando_sistema

# Limpiar la pantalla en diferentes sistemas operativos
def limpiar_pantalla():

    if sistema_operativo == 'nt':  # Windows
        comando_sistema('cls')
    else:  # Unix/Linux/Mac
        comando_sistema('clear')

if __name__ == "__main__":
    limpiar_pantalla()