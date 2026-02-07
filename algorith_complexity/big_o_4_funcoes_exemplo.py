import numpy.typing as npt

def constant(n):
    return n[0]

def linear(n):
    list_n = []
    for i in n:
        list_n.append(i)
    return list_n

def linear2(n):
    list_n = []
    for i in n:
        list_n.append(i)
    for i in n:
        list_n.append(i)
    return list_n

def quadratic(n):
    list_n = []
    for i in n:
        for j in n:
            list_n.append(i)
    return list_n

