# Declaración de la clase '"ListaDeTareas".
# Cuenta con su constructor y destructor del objeto "ListaDeTareas".

from tarea import Tarea

class ListaDeTareas():

    # Constructor de una "Lista de Tareas" vacía.
    def __init__(self):
        self.__lista_de_tareas = list()
        # Saber el número de Tareas en la Lista.
        self.__longitud = 0
    
    # Destructor de la Lista de Tareas
    def __del__(self):
        # print("Limpiando la la lista de tareas.")
        pass

    # Número de tareas que contiene la lista.
    # Sería el método GET del atributo privado.
    def numero_de_tareas(self):
        return len(self.__lista_de_tareas)

    # Agregar una nueva tarea:
    # Permitir al usuario agregar una nueva tareaa a la ista de tareas.
    def agregar_tarea(self):
        descripcion = input("Descripción de la tarea: ")
        tarea = Tarea(descripcion)
        self.__lista_de_tareas.append(tarea)
        self.__longitud += 1
        print("\nTarea agregada.")

    # Marcar una tarea como completada:
    # Permitir al usuario marcar una tarea como completada.
    # Se le pasa su posición en la lista de tareas.
    def completar_tarea(self):
        self.mostrar_tareas()
        try:
            indice = int(input("\nIntroduce el número de la tarea completada: "))
            # Manejamos una fila no una cola por lo que NO se accede por el final
            # if 0 < indice <= len(self.__lista_de_tareas):
            if 0 < indice <= self.__longitud:
                tarea = self.__lista_de_tareas[indice - 1]
                if tarea.get_is_pendiente():
                    tarea.completar()
                    print(f"\nTarea '{tarea.get_descripcion()}' completada.")
                else:
                    print(f"\n¡Tarea '{tarea.get_descripcion()}' ya estaba completada!")
            else:
                raise ValueError
        except (ValueError, IndexError, KeyboardInterrupt):
            print("\n¡Introduce un número de índice de tarea válido!")
    
    # Mostrar todas las tareas:
    # Permitir al usuario imprimir en pantalla todas las tareas numeradas.
    # Se muestra su descripción y estado como (completada o pendiente).
    def mostrar_tareas(self):
        print("--- Listado de Tareas ---\n")
        # Controlado por el menu principal no haría falta.
        if not self.__longitud:
            print("No hay tareassss en la lista.")
        else:
            for indice, tarea in enumerate(self.__lista_de_tareas, 1):
                print(f"{indice}.- {tarea}")
    
    # Eliminar una tarea:
    # Permitir al usuario eliminar una tarea de la lista dada su posición.
    def eliminar_tarea(self):
        self.mostrar_tareas()
        try:
            indice = int(input("\nIntroduce el número de la tarea a eliminar: "))
            if 0 < indice <= self.__longitud:
                tarea = self.__lista_de_tareas.pop(indice - 1)
                print(f"\nTarea '{tarea.get_descripcion()}' eliminada.")
                self.__longitud -= 1
            else:
                raise ValueError
        except (ValueError, IndexError, KeyboardInterrupt):
            print("\n¡Introduce un número de índice de tarea válido!")

# Probar que todo funciona como debe.
def main():
    mi_lista_tareas = ListaDeTareas()
    print(mi_lista_tareas.numero_de_tareas())
    mi_lista_tareas.mostrar_tareas()
    mi_lista_tareas.agregar_tarea()
    print(mi_lista_tareas.numero_de_tareas())
    mi_lista_tareas.mostrar_tareas()
    mi_lista_tareas.agregar_tarea()
    print(mi_lista_tareas.numero_de_tareas())
    mi_lista_tareas.completar_tarea()
    print(mi_lista_tareas.numero_de_tareas())
    mi_lista_tareas.mostrar_tareas()    
    mi_lista_tareas.eliminar_tarea()
    print(mi_lista_tareas.numero_de_tareas())
    mi_lista_tareas.mostrar_tareas()
    del mi_lista_tareas

if __name__ == "__main__":
    main()