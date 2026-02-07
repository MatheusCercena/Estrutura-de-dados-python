import numpy as np

class VetorOrdenadoCrescenteInt:
    def __init__(self, capacidade, dados_padrao = True):
        self.capacidade = capacidade
        self.ultima_posicao = -1
        self.valores = np.zeros(self.capacidade, dtype=int)
        self.valores = np.linspace(1, 100_000, 100_000) if dados_padrao == True else self.valores

    def imprime(self):
        if self.ultima_posicao == -1:
            print('A lista está vazia')
        else:
            for i in range(self.ultima_posicao + 1):
                print(f'Pos {i} = {self.valores[i]}')

    def inserir(self, valor_a_inserir):
        if self.ultima_posicao == self.capacidade -1:
            print('Capacidade máxima atingida')
            return
        self.ultima_posicao += 1
        for i in range(self.ultima_posicao + 1):
            if i == self.ultima_posicao:
                self.valores[i] = valor_a_inserir
                break
            if valor_a_inserir <= self.valores[i]:
                for j in range(self.ultima_posicao, i, -1):
                    self.valores[j] = self.valores[j-1]
                self.valores[i] = valor_a_inserir
                break


    def pesquisa_linear(self, valor_a_encontrar):
        for i in range(self.ultima_posicao + 1):
            if self.valores[i] == valor_a_encontrar:
                return i
        return -1

    def pesquisar_binario(self, valor_a_encontrar):
        ponto_inicial = 0
        ponto_final = self.ultima_posicao

        while True:
            ponto_central = round((ponto_inicial + ponto_final) / 2)
            if valor_a_encontrar == self.valores[ponto_central]:
                return ponto_central
            elif ponto_inicial == ponto_final - 1:
                return -1
            elif valor_a_encontrar < self.valores[ponto_central]:
                ponto_final = ponto_central
            elif valor_a_encontrar > self.valores[ponto_central]:
                ponto_inicial = ponto_central


    def excluir(self, valor_a_excluir):
        posicao_do_valor = self.pesquisa_linear(valor_a_excluir)
        if posicao_do_valor == -1:
            return -1
        else:
            for i in range(posicao_do_valor, self.ultima_posicao):
                self.valores[i] = self.valores[i + 1]
            self.ultima_posicao -= 1
            return None


class VetorOrdenadoCrescenteIntDadosPadrao:
    def __init__(self):
        self.capacidade = 100_000
        self.ultima_posicao = 99_999
        self.valores = np.linspace(1, 100_000, 100_000)

    def imprime(self):
        if self.ultima_posicao == -1:
            print('A lista está vazia')
        else:
            for i in range(self.ultima_posicao + 1):
                print(f'Pos {i} = {self.valores[i]}')

    def inserir(self, valor_a_inserir):
        if self.ultima_posicao == self.capacidade - 1:
            print('Capacidade máxima atingida')
            return
        self.ultima_posicao += 1
        for i in range(self.ultima_posicao + 1):
            if i == self.ultima_posicao:
                self.valores[i] = valor_a_inserir
                break
            if valor_a_inserir <= self.valores[i]:
                for j in range(self.ultima_posicao, i, -1):
                    self.valores[j] = self.valores[j - 1]
                self.valores[i] = valor_a_inserir
                break

    def pesquisa_linear(self, valor_a_encontrar):
        for i in range(self.ultima_posicao + 1):
            if self.valores[i] == valor_a_encontrar:
                return i
        return -1

    def pesquisar_binario(self, valor_a_encontrar):
        ponto_inicial = 0
        ponto_final = self.ultima_posicao

        while True:
            ponto_central = round((ponto_inicial + ponto_final) / 2)
            if valor_a_encontrar == self.valores[ponto_central]:
                return ponto_central
            elif ponto_inicial == ponto_final - 1:
                return -1
            elif valor_a_encontrar < self.valores[ponto_central]:
                ponto_final = ponto_central
            elif valor_a_encontrar > self.valores[ponto_central]:
                ponto_inicial = ponto_central

    def excluir(self, valor_a_excluir):
        posicao_do_valor = self.pesquisa_linear(valor_a_excluir)
        if posicao_do_valor == -1:
            return -1
        else:
            for i in range(posicao_do_valor, self.ultima_posicao):
                self.valores[i] = self.valores[i + 1]
            self.ultima_posicao -= 1
            return None

# vetor = VetorOrdenadoCrescenteInt(5)
# vetor.imprime()
# vetor.inserir(6)
# vetor.inserir(3)
# vetor.inserir(9)
# vetor.inserir(15)
# vetor.inserir(13)
# vetor.imprime()
# vetor.inserir(62)
#
# print(vetor.excluir(9))
# vetor.imprime()
#
# vetor.inserir(9)
# vetor.imprime()

