# Librería que contiene la definición de la clase Tareas.
# import moduloTareas as Tareas
from moduloTareas import Tarea

# Librería por compatibilidad de Sistemas Operativos.
from moduloSistemaOperativo import limpiar_pantalla

# Listas de Tareas
lista_tareas = []

# Agregar una nueva tarea:
# Permitir al usuario agregar una nueva tareaa a la ista de tareas.
def agregar_tarea():
    descripcion = input("Descripción de la tarea: ")
    tarea = Tarea(descripcion)
    lista_tareas.append(tarea)
    print("\nTarea agregada.")  

# Marcar una tarea como completada:
# Permitir al usuario marcar una tarea como completada.
# Se le pasa su posición en la lista de tareas.
def completar_tarea():
    mostrar_tareas()
    try:
        indice = int(input("\nIntroduce el número de la tarea completada: "))
        # Manejamos una fila no una cola por lo que NO se accede por el final
        if indice > 0:  
            tarea = lista_tareas[indice - 1]
            if tarea.get_isPendiente():
                tarea.completar()
                print(f"\nTarea '{tarea.get_descripcion()}' completada.")
            else:
                print(f"\n¡Tarea '{tarea.get_descripcion()}' ya estaba completada!!!")
        else:
            raise ValueError
    except (ValueError, IndexError):
        print("\n¡Introduce un número de índice de tarea válido!!!")

# Mostrar todas las tareas:
# Permitir al usuario imprimir en pantalla todas las tareas numeradas.
# Se muestra su descripción y estado como (completada o pendiente).
def mostrar_tareas():
    for indice, tarea in enumerate(lista_tareas, 1):
        print(f"{indice}.- {tarea}")

# Eliminar una tarea:
# Permitir al usuario eliminar una tarea de la lista dada su posición.
def eliminar_tarea():
    mostrar_tareas()
    try:
        indice = int(input("\nIntroduce el número de la tarea a eliminar: "))
        # Manejamos una fila no una cola por lo que NO se accede por el final
        if indice > 0:  
            tarea = lista_tareas.pop(indice - 1)
            print(f"\nTarea '{tarea.get_descripcion()}' eliminada.")
            del tarea        
        else:
            raise ValueError
    except (ValueError, IndexError):
        print("\n¡Introduce un número de índice de tarea válido!!!")

# Presentar menú de opciones permitidas al usuario.
def menu():

    # Se presneta el menú hasta se seleccione la opción de "Salir".
    while True:

        # Evitamos interrupciones pueda mandar el usuario
        try:
            
            # Presnetamos las opciones del menú.
            limpiar_pantalla()        
            print("--- Menú de Tareas ---\n")
            print("1.- Agregar una nueva tarea.")
            print("2.- Marcar una tarea como completada.")
            print("3.- Mostrar todas las tareas.")
            print("4.- Eliminar una tarea.")
            print("5.- Salir de la aplicación.")
            opcion = input("\nSelecciona tu opción: ")
            limpiar_pantalla()
            
            # Manjemoas las Opciones del menú
            if opcion == "5":
                print("Saliendo del programa...")
                break
            elif opcion == "1":
                agregar_tarea()
            elif not lista_tareas:
                print("No hay tareas en la lista.")
            elif opcion == "2":
                completar_tarea()
            elif opcion == "3":
                mostrar_tareas()       
            elif opcion == "4":
                eliminar_tarea() 
            else:
                print("¡Opción no válida!!!\n\nPor favor, selecciona una opción del 1 al 5.")
            input("\n\nPulsa la tecla 'Enter' para continuar...")
        
        except:
            pass
            # except (EOFError, KeyboardInterrupt) 
            # print("No se puede salir interrumpiendo el programa.")

# Comienza la Ejecución del Programa.
if __name__ == "__main__":
    menu()