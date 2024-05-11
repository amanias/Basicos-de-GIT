def indexador(objeto, indice):
    return objeto[indice]

try:
    resultado = indexador('Python', int(input("Dame el indice: ")))
except IndexError: # Captura IndexError
    resultado = 'Error de índice.'
except ValueError: # Captura TypeError
    resultado = 'El índice tiene que ser un número.'
else:
    print("Todo bien!!!")
finally:
    print("Siempre ejecutado haya o no excepciones!!!!")
    
print('Hemos salido del try-catch con el resultado: ', resultado)

# Creemos excepciones propias.
class miPropiaExcepcion(Exception):
    #Las excepciones heredan de Exception
    def __init__(self, valor):
        self.valor = valor
    def __str__(self):
        return str(self.valor)
try:
    raise(miPropiaExcepcion("He lanzado mi propia excepción"))
except miPropiaExcepcion:
    pass