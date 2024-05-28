# Declaración de la clase '"Tarea"
# Atributos privados como la "Descripción" de la tarea y el "Estado" de esta si pendiente o completada.
# Cuenta con sus constructor y destructor del objeto "Tarea"

class Tarea():

    # Constructor al que se le pasa la "Descripción" de la tarea a realizar que queda como "Pendiente".
    def __init__(self, descripcion):
        self.__strDescripcion = descripcion
        self.__isPendiente = True
    
    # Destructor de la tarea
    def __del__(self):
        # print("Limpiando la tarea eliminada")
        pass

    # Obtener la descripción de la tarea del atributo privado "strDescripcion"
    def get_descripcion(self):
        return self.__strDescripcion

    # Obtener el estado de la tarea del atributo privado "isPendiente".
    def get_isPendiente(self):
        return self.__isPendiente

    # Imprime la tarea y su estado.
    def __str__(self):
        estado = "Pendiente" if self.__isPendiente else "Completada"
        return f"La tarea '{self.__strDescripcion}' está {estado}."
    
    # Completar la tarea
    def completar(self):
        self.__isPendiente = False