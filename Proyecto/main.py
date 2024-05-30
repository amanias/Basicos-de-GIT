# Librería que contiene la definición de la clase "ListaDeTareas".
from lista_de_tareas import ListaDeTareas

# Librería por compatibilidad de Sistemas Operativos.
from sistema_operativo import limpiar_pantalla

# Presentamos las opciones del menú.
def menu_opciones():
    limpiar_pantalla()        
    print("--- Menú de Tareas ---\n")
    print("1.- Agregar una nueva tarea.")
    print("2.- Marcar una tarea como completada.")
    print("3.- Mostrar todas las tareas.")
    print("4.- Eliminar una tarea.")
    print("5.- Salir de la aplicación.")
    opcion = input("\nSelecciona tu opción: ")
    limpiar_pantalla()
    return opcion

# Manjemoas las opciones del menú.
def menu_funcionamiento(opcion, lista):
    if opcion == "1":
        lista.agregar_tarea()
    elif lista.numero_de_tareas() == 0:
        print("¡No hay tareas en la lista!!!")
    elif opcion == "2":
        lista.completar_tarea()
    elif opcion == "3":
        lista.mostrar_tareas()
    elif opcion == "4":
        lista.eliminar_tarea()

# Manejo de la aplicación.
def menu():
    lista_de_tareas = ListaDeTareas()
    # Se presenta el menú hasta se seleccione la opción de "Salir".
    while True:
        try:
            opcion = menu_opciones()
            if opcion == "5":
                print("Saliendo del programa...")
                break
            elif opcion in ["1", "2", "3", "4"]:
                menu_funcionamiento(opcion, lista_de_tareas)
            else:
                print(f"¡Opción '{opcion}' no válida!!!\n\nPor favor, selecciona una opción del 1 al 5.")
            input("\n\nPulsa la tecla 'Enter' para continuar...")
        except:
            pass
            # except (EOFError, KeyboardInterrupt) 
            # print("No se puede salir de la App interrumpiendo el programa.")

# Comienza la Ejecución del Programa.
if __name__ == "__main__":
    menu()