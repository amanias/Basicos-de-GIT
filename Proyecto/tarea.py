# Declaración de la clase '"Tarea"
# Atributos privados como la "Descripción" de la tarea y el "Estado" de esta si pendiente o completada.
# Cuenta con sus constructor y destructor del objeto "Tarea"

class Tarea:

    # Constructor al que se le pasa la "Descripción" de la tarea a realizar que queda como "Pendiente".
    def __init__(self, descripcion):
        self.__str_descripcion = descripcion
        self.__is_pendiente = True

    # Destructor de la tarea.
    def __del__(self):
        # print("Limpiando la tarea eliminada.")
        pass

    # Obtener la descripción de la tarea del atributo privado "strDescripcion".
    def get_descripcion(self):
        return self.__str_descripcion

    # Imprime la tarea y su estado.
    def get_is_pendiente(self):
        return self.__is_pendiente

    # Imprime la tarea junto con su estado.
    def __str__(self):
        estado = "Pendiente" if self.__is_pendiente else "Completada"
        return f"La tarea '{self.__str_descripcion}' está {estado}."

    # Completar la tarea.
    def completar(self):
        self.__is_pendiente = False

# Probar que todo funciona como debe.
def main():
    mi_tarea = Tarea("Agua")
    print(mi_tarea)
    print("Descripción: ", mi_tarea.get_descripcion())
    print("Estado Pendiente?: ", mi_tarea.get_is_pendiente())
    mi_tarea.completar()
    print(mi_tarea)
    print("Descripción: ", mi_tarea.get_descripcion())
    print("Estado Pendiente?: ", mi_tarea.get_is_pendiente())
    del mi_tarea

if __name__ == "__main__":
    main()