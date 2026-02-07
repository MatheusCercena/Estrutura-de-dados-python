import timeit

def soma(n):
    soma = 0
    for i in range(n + 1):
        soma += i
    return soma

print("Rodando")
tempo = timeit.timeit(lambda: soma(100))
print(f"O tempo total de execução foi {tempo} ms")

def soma2(n):
    return (n * (n+1))/2

print("Rodando")
tempo = timeit.timeit(lambda: soma2(100))
print(f"O tempo total de execução foi {tempo} ms")

def soma3(n):
    return n

print("Rodando")
tempo = timeit.timeit(lambda: soma3(100))
print(f"O tempo total de execução foi {tempo} ms")