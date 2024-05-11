# a, b, c = map(int, input("Introduzca los números: ").split())
# print(f"Los números son: {a} {b} {c}")

# lista = list()
# conjunto = set()

# longitudLista = int(input("Tamaño de la lista: "))
# longitudConjunto = int(input("Tamaño del conjunto: "))

# for i in range(0, longitudLista):
#     lista.append(input("Elemento de la lista"))
# print(lista)

# for i in range(0, longitudConjunto):
#     conjunto.add(input("Elemento del conjunto"))
# print(conjunto)

List = list(map(int, input("Introduzca los elementos de la lista:").split()))
Set = set(map(int, input("Introduzca los elementos del Set: ").split()))
print(List)
print(Set)