miLista = [1,2,3,4,5,6,7]
print(miLista)

miLista2 = [2*elemento for elemento in miLista]
print(miLista2)

listaPares = [elemento for elemento in miLista if elemento%2==0]
print(listaPares)

a = ["a","b","c"]
b = [1,2,3]
c = [elemento1*elemento2 for elemento1 in a for elemento2 in b]
print(c)
d = [elemento1*elemento2 for elemento1 in a for elemento2 in b if elemento2!=2]
print(d)

matriz = [["a1", "a2", "a3"], ["b1", "b2", "b3"], ["c1", "c2", "c3"]]
print(matriz)
columna2 = [fila[1] for fila in matriz]
print(columna2)
diagonalMatriz = [matriz[i][i] for i in [0,1,2]]
print(diagonalMatriz)
diagonalMatriz2 = [matriz[i][i] for i in range(3)]
print(diagonalMatriz2)
matriz2 = [["a1", "a2", "a3"], ["b1"], ["c1", "c2", "c3", "c4"]]
longitudes = [len(fila) for fila in matriz2]
print(longitudes)
longitudes2 = [len(fila) for fila in matriz2 if len(fila)>2]
print(longitudes2)

losCuadrados = [elemento**2 for elemento in range(10)]
print(losCuadrados)

# Cómo copiar listas
la = [1,2,3]
laCopiaReferencia = la
laCopiaValores = la[:]
laCopiaValores2 = list(la)
la[2] = "yo"
print(la)
print(laCopiaReferencia)
print(laCopiaValores)
print(laCopiaValores2)
laInvertida = la[::-1]
print(laInvertida)

# Aislar una variable
import copy as copiar
la = [1,2,[31,32,33]]
lb = copiar.copy(la)
lc = copiar.deepcopy(la)
la[1]="yo"
la[2][2] = "yoyo"
print("Modificada en todos sus niveles: ", la)
print("Modificada en niveles profundos: ", lb)
print("No modifica los valores ni en los niveles profundos: ", lc)