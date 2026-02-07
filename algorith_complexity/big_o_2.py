import timeit


def lista1():
    lista = []
    for i in range(100):
        lista += [i]
    return lista

tempo = timeit.timeit(lambda: lista1())
print(f"O tempo foi {tempo}ms")


def lista2():
    return range(100)

tempo = timeit.timeit(lambda: lista2())
print(f"O tempo foi {tempo}ms")