import numpy as np

class VetorNaoOrdenadoInt:
    def __init__(self, capacidade, dados_padrao = True):
        self.capacidade = capacidade
        self.ultima_posicao = -1
        self.valores = np.empty(capacidade, dtype=int)
        self.valores = np.linspace(1, 100_000, 100_000) if dados_padrao == True else self.valores

    #O(n)
    def imprime(self):
        if self.ultima_posicao == -1:
            print('A lista está vazia')
        else:
            for i in range(self.ultima_posicao + 1):
                print(f'Pos {i} = {self.valores[i]}')


    def inserir(self, valor_a_inserir):
        if self.ultima_posicao == self.capacidade:
            print('Capacidade máxima atingida')
        else:
            self.ultima_posicao += 1
            self.valores[self.ultima_posicao] = valor_a_inserir

    def pesquisar(self, valor_a_encontrar):
        for i in range(self.ultima_posicao+1):
            if self.valores[i] == valor_a_encontrar:
                return i
        return -1

    def excluir(self, valor_a_excluir):
        posicao_do_valor = self.pesquisar(valor_a_excluir)
        if posicao_do_valor == -1:
            return -1
        else:
            for i in range(posicao_do_valor, self.ultima_posicao):
                self.valores[i] = self.valores[i + 1]
            self.ultima_posicao -= 1
            return None

class VetorNaoOrdenadoIntDadosPadrao:
    def __init__(self):
        self.capacidade = 100_000
        self.ultima_posicao = 99_999
        self.valores = np.linspace(1, 100_000, 100_000)

    #O(n)
    def imprime(self):
        if self.ultima_posicao == -1:
            print('A lista está vazia')
        else:
            for i in range(self.ultima_posicao + 1):
                print(f'Pos {i} = {self.valores[i]}')


    def inserir(self, valor_a_inserir):
        if self.ultima_posicao == self.capacidade:
            print('Capacidade máxima atingida')
        else:
            self.ultima_posicao += 1
            self.valores[self.ultima_posicao] = valor_a_inserir

    def pesquisar(self, valor_a_encontrar):
        for i in range(self.ultima_posicao+1):
            if self.valores[i] == valor_a_encontrar:
                return i
        return -1

    def excluir(self, valor_a_excluir):
        posicao_do_valor = self.pesquisar(valor_a_excluir)
        if posicao_do_valor == -1:
            return -1
        else:
            for i in range(posicao_do_valor, self.ultima_posicao):
                self.valores[i] = self.valores[i + 1]
            self.ultima_posicao -= 1
            return None

# vetor = VetorNaoOrdenadoInt(5)
# vetor.imprime()
# vetor.inserir(6)
# vetor.imprime()
# print(vetor.pesquisar(6))
# print(vetor.pesquisar(3))
#
#
# vetor.inserir(3)
# vetor.inserir(9)
# vetor.inserir(15)
#
# vetor.imprime()
# vetor.excluir(15)
# vetor.imprime()
#
#
