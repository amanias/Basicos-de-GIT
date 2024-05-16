from math import pi

def area(radio):
    if type(radio) not in [float, int]:
        raise TypeError("Unicamente se permiten entrar valores positivos enteros o reales.")
    if radio < 0:
        raise ValueError("No se permiten valores negativos.")
    areaCirculo = pi*(radio**2)
    return areaCirculo

valores = [1, 3, 0, -1, -3, 2+3j, True, 'hola']

# for valor in valores:
#     areaCalculada = area(valor)
#     print(f"El área del círculo de radio {valor} es: {areaCalculada}")
