''' Manejar Diccionarios'''
claves = ("Nombre", "Apellidos", "Edad")
valores = ("Alberto", "Mañas Carrete", 55)
diccionario = dict(zip(claves, valores))

print("Diccionario: ", diccionario)

# Recorrido del diccionario por el Metodo antiguo
# for elemento in diccionario:
#     print(f"{elemento}: {diccionario[elemento]}.")

print("Claves: ", diccionario.keys())
for clave in diccionario.keys():
    print(clave, end=" ")
print()

print("Valores: ", diccionario.values())
for valor in diccionario.values():
    print(valor, end=" ")
print()

print("Tuplas (Clave, Valor): ", diccionario.items())
for clave, valor in diccionario.items():
    print(f"{clave}: {valor}.")