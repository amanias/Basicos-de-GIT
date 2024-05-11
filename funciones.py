# def f(**args):
#     print(args)

# f()
# f(a=1)

# def f(a, *b, c):
#     ''' Algo hace'''
#     print(a, b, c)

# f(1, c=2)
# f(1, 10, c=100)
# f(1, 10, 2, 4, c=100)

# la = [1, 2, 3, 4, 5]
# lb = list('abcde')
# lc = list('ABCD')

# print(la)
# print(lb)
# print(lc)

# zipList = list(zip(la, lb, lc))
# print(zipList)

# a, b, c = zip(*zipList)
# print (a, b, c)

# def log(*args, prefijo= "LOG", separador="|"):
#     print(prefijo+":", *args, sep=separador)

# log(4, 5, 6)
# log(4, 5, 6, "HOLA")
# log(4, 5, 6, "HOLA", separador=";")
# log(4, 5, 6, prefijo="HOLA")
# log("mierda", "culo")

print (True + 2)