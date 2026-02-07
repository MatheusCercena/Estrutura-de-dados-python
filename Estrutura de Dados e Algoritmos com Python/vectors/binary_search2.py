import random
import timeit

from ordered_vector import *
from unnordered_vector import *
import numpy as np


def inserir_ordenado():
    vetor_ordenado = VetorOrdenadoCrescenteInt(1000)
    for _ in range(1000):
        vetor_ordenado.inserir(round(random.random(), 4))

def inserir_nao_ordenado():
    vetor_nao_ordenado = VetorNaoOrdenadoInt(1000)
    for _ in range(1000):
        vetor_nao_ordenado.inserir(round(random.random(), 4))

# print(timeit.timeit(lambda: inserir_nao_ordenado(), number=3))
# print(timeit.timeit(lambda: inserir_ordenado(), number=3))

vetor_ordenado = VetorOrdenadoCrescenteIntDadosPadrao()
vetor_nao_ordenado = VetorNaoOrdenadoIntDadosPadrao()


print(timeit.timeit(lambda: vetor_ordenado.pesquisar_binario(9999), number=1000))

print(timeit.timeit(lambda: vetor_nao_ordenado.pesquisar(9999), number=1000))

