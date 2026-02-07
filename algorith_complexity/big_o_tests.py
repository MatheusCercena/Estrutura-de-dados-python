from big_o_4_funcoes_exemplo import *
import numpy as np
from timeit import timeit
import matplotlib.pyplot as plt

n = np.linspace(1, 10, 50)

# O(5)
# tempo_constant = timeit(lambda: constant(n))
# print(f'tempo constant = {tempo_constant}s')

# O(n)
# tempo_linear = timeit(lambda: linear(n))
# print(f'tempo linear = {tempo_linear}s')

# O(2n)
# tempo_linear2 = timeit(lambda: linear2(n))
# print(f'tempo linearX2 = {tempo_linear2}s')

# O(n**2)
# tempo_quadratic = timeit(lambda: quadratic(n))
# print(f'tempo quadratic = {tempo_quadratic}s')

labels = ['constant', 'linear', 'linear2', 'quadratic']
resultados = {label: [] for label in labels}

for valor in n:
    resultados['constant'].append(timeit(lambda: constant(n), number=1000))
    resultados['linear'].append(timeit(lambda: linear(n), number=1000))
    resultados['linear2'].append(timeit(lambda: linear2(n), number=1000))
    resultados['quadratic'].append(timeit(lambda: quadratic(n), number=1000))

plt.figure(figsize=(10,8))
plt.ylim(0, 100)
for label in labels:
    plt.plot(n, resultados[label], label=label)

plt.ylim(0, max(resultados['linear2']) * 2)
plt.legend()
plt.ylabel('Runtime')
plt.xlabel('n')
plt.title('Análise de Complexidade Assintótica')
plt.grid(True)
plt.show()



